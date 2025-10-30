"""
Utility module for AI models precision and time analysis
Contains auxiliary functions for text processing and technical recommendations
"""

import time
import pandas as pd
from typing import Dict, Tuple

from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


def verify_substring(cadena_principal: str, subcadena: str, to_return: str) -> str:
    """
    Verifies if a substring is present in a main string.
    
    Args:
        cadena_principal (str): The string where to search
        subcadena (str): The substring to search for
        to_return (str): The value to return if the substring is found
        
    Returns:
        str: to_return if the substring is present, cadena_principal otherwise
    """
    if subcadena in cadena_principal:
        return to_return
    else:
        return cadena_principal


def normalize_variable_name(variable: str) -> str:
    """
    Normalizes meteorological variable names to standard names.
    
    Args:
        variable (str): Original variable name
        
    Returns:
        str: Normalized variable name
    """
    # Mapping of substrings to normalized names
    mappings = [
        ('pres', 'Presión Atmosférica'),
        ('rh', 'Humedad Relativa'),
        ('slp', 'Presión a Nivel del Mar'),
        ('solar_rad', 'Radiación Solar'),
        ('temp', 'Temperatura Ambiente'),
        ('uv', 'Índice UV'),
        ('vis', 'Visibilidad'),
        ('wind_gust_spd', 'Ráfagas de Viento'),
        ('wind_spd', 'Velocidad Promedio del Viento')
    ]
    
    for subcadena, nombre_normalizado in mappings:
        variable = verify_substring(variable, subcadena, nombre_normalizado)
        if variable == nombre_normalizado:
            break
    
    return variable


def create_llm_chat_model(model: str):
    """
    Creates an LLM chat model based on the model name.
    
    Args:
        model (str): Model name ('gpt', 'gpt-4o', 'llama1', 'llama2', etc.)
        
    Returns:
        Corresponding chat model instance
    """
    if model == "gpt":
        return ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    elif model == "gpt-4o":
        return ChatOpenAI(temperature=0, model=model)
    elif model == "llama1":
        return ChatOllama(model="llama3.1", temperature=0)
    elif model == "llama2":
        return ChatOllama(model="llama3.2:1b", temperature=0)
    elif model == "gemini-2.5-pro-exp-03-25":
        return ChatGoogleGenerativeAI(temperature=0, model=model)
    elif model == "gemini-2.0-flash-001":
        return ChatGoogleGenerativeAI(temperature=0, model=model)
    else:
        try:
            return ChatOllama(model=model, temperature=0)
        except:
            return ChatOpenAI(temperature=0, model=model)


def recomendacion(model: str, info_poligono: dict) -> Tuple[Dict[str, str], Dict[str, float]]:
    """
    Generates technical recommendations for electrical infrastructure variables.
    
    Args:
        model (str): Name of the AI model to use
        info_poligono (dict): Polygon information with equipment and variables
        
    Returns:
        Tuple[Dict[str, str], Dict[str, float]]: Tuple with responses and execution times
    """
    
    template = """
    You are a technical expert in electrical infrastructure. Your objective is to provide recommendations and 
    regulatory guidelines based on the context provided to you. 

    Instructions for your response:
    1. Identify the variables and their values mentioned by the user.
    2. Review the regulatory context and historical information (chat_history) to understand applicable 
    standards or limits.
    3. Compare each variable value with the context standards, explaining whether it complies or not. 
    - If it doesn't comply, explain the risk or consequence and provide clear and actionable 
        recommendations (what to change, what to review, what to reinforce, etc.). Also always provide 
        a suggestion of the regulation to which it should conform and the value to which it should be adjusted.
    - If it complies, explain why it complies and what should be considered in the future (maintenance, 
        usage limits, etc.).
    4. Always provide a suggestion of the regulation to which the variable should conform.
    5. Always explicitly provide the value to which the variable should be adjusted or the range of values it should be in.
    6. Write your response in a clear, but conversational and close tone, without using an overly 
    rigid list. Structure the text in free paragraphs or bullet points to make it easier to understand.
    7. If there is ambiguity or lack of information, explain what additional information would be needed 
    to provide a more complete recommendation.

    Use the following context and conversation history to draft the recommendation:

    {context}

    {chat_history}

    Human: {human_input}

    Chatbot (RECOMMENDATION RESPONSE IN A SINGLE PARAGRAPH):
    """

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input", "context"], 
        template=template
    )
    
    # Crear modelo de chat
    llm_chat = create_llm_chat_model(model)
    
    # Configure embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    
    responses = {}
    times = {}
    
    # Variables that should be excluded from processing
    excluded_variables = [
        "ALTITUD_mean", "ALTITUD_median", "ALTITUD_min", "ALTITUD_max", "ALTITUD_std",
        "CORRIENTE_mean", "CORRIENTE_median", "CORRIENTE_min", "CORRIENTE_max", "CORRIENTE_std",
        "TIPO_1_count", "TIPO_2_count"
    ]
    
    for muestra in info_poligono.keys():
        tipo_equipo = info_poligono[muestra]["Tipo_de_equipo"]
        
        try:
            variables_recomendacion = pd.read_excel(f"arbol_decision_recomendaciones/variables_{tipo_equipo}.xlsx")
        except Exception as e:
            print(f"Error cargando archivo Excel para {tipo_equipo}: {e}")
            continue
            
        for variable in info_poligono[muestra]["top_5"].keys():
            variable_original = variable
            
            # Normalize variable name if not in the list
            if variable not in list(variables_recomendacion["Variables"]):
                variable = normalize_variable_name(variable)
                
            # Skip excluded variables
            if variable in excluded_variables:
                responses[f"{tipo_equipo}_{variable_original}_{variable}"] = "NA"
                times[f"{tipo_equipo}_{variable_original}_{variable}"] = "NA"
                continue
                
            try:
                # Search for variable information in Excel
                var_info = variables_recomendacion[variables_recomendacion["Variables"] == variable]
                if var_info.empty:
                    continue
                    
                # Get document and section
                try:
                    documento_buscar = var_info["Documento "].iloc[0]
                except:
                    documento_buscar = var_info["Documento"].iloc[0]
                    
                seccion_buscar = var_info["Normativa"].iloc[0]
                sugerencia = var_info["Sugerencia"].iloc[0]
                valor_variable = info_poligono[muestra]["top_5"][variable_original]

                # Configure memory and chain
                memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")
                chain = load_qa_chain(llm_chat, chain_type="stuff", memory=memory, prompt=prompt)
                
                # Load vectorstore
                vectorstore = Chroma(
                    persist_directory=f"embeddings_by_procces/{documento_buscar}",
                    embedding_function=embeddings
                )
                
                # Perform relevant documents search
                query_search = sugerencia + " " + seccion_buscar
                docs_variable = vectorstore.similarity_search(query_search, k=5)
                
                # Generate query for recommendation
                query_recommendation = f"Generate a recommendation for the variable {variable}, which has a value of {valor_variable}. {sugerencia}"
                
                # Execute chain and measure time
                init = time.time()
                response = chain({
                    "input_documents": docs_variable, 
                    "human_input": query_recommendation, 
                    "chat_history": memory
                }, return_only_outputs=False)
                end = time.time()

                response_text = response['output_text']
                
                # Store results
                key = f"{tipo_equipo}_{variable_original}_{variable}"
                responses[key] = response_text
                times[key] = end - init

                print(f"RESPONSE GENERATED FOR {key}")
                print(response_text)
                print("-" * 50)
                
            except Exception as e:
                print(f"Error procesando variable {variable}: {e}")
                continue
        
    return responses, times


# Additional auxiliary functions
def save_results_to_pickle(data: dict, filename: str) -> None:
    """
    Saves results in pickle format.
    
    Args:
        data (dict): Data to save
        filename (str): File name
    """
    import pickle
    with open(filename, "wb") as archivo:
        pickle.dump(data, archivo)


def load_results_from_pickle(filename: str) -> dict:
    """
    Loads results from pickle format.
    
    Args:
        filename (str): File name
        
    Returns:
        dict: Loaded data
    """
    import pickle
    with open(filename, 'rb') as archivo:
        return pickle.load(archivo)