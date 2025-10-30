# STRUCTURED QUESTIONS
# Questions related to transformer event data analysis

structured_questions = [
    "¿Cúantas interrupciones hubo entre el año 2019 y el año 2023?",
    "¿Cuántas interrupciones hubo en el municipio de Manzanares entre el año 2020 y el año 2022?",
    "¿Cuantas interrupciones en transformadores se han dado a partir del año 2022?",
    "¿Cúal ha sido la causa de interrupción más frecuente en el año 2023?",
    "¿Cúal ha sido la duración promedio de las interrupciones en el último año?",
    "¿Cúal ha sido la duración promedio de las interrupciones en el departamento de Caldas en el último año?",
    "¿Cúal ha sido la duración promedio de las interrupciones en interruptores entre el año 2020 y 2023?",
    "¿Cúal ha sido el promedio del SAIDI y SAIFI en el municipio de San josé?",
    "¿Cúal ha sido el promedio del SAIDI y SAIFI antes del año 2022?",
    "¿Cúal ha sido el promedio del SAIDI y SAIFI en tramos de red en el último año?",
    "Dime los 3 municipios en los que más se han presentado interrupciones en el último año.",
    "Dime los 3 municipios en los que menos se han presentado interrupciones en el último año.",
    "¿Cúal ha sido el municipio que históricamente ha tenido un mayor promedio de SAIDI y SAIFI?",
    "¿Cúal ha sido el municipio que históricamente ha tenido un menor promedio de SAIDI y SAIFI?",
    "¿Cúal es el tipo de equipo en el que más se presentan interrupciones en el departamento de Caldas?",
    "¿Cúal ha sido el tipo de equipo en el que menos se han presentado interrupciones entre el año 2021 y 2023?",
    "¿Históricamente cúal ha sido la fecha en la que más se han presentado interrupciones?",
    "¿Históricamente cúal ha sido la fecha en la que menos se han presentado interrupciones?",
    "¿Hay algún tipo de equipo en el que no se halla presentado interrupciones en Villa María?"
]

# Function to get structured questions
def get_structured_questions():
    """
    Returns the list of structured questions related to electrical event data analysis.
    
    Returns:
        list: List of strings with the questions
    """
    return structured_questions

# Function to get a specific question by index
def get_structured_question_by_index(index):
    """
    Returns a specific structured question by its index.
    
    Args:
        index (int): Question index (0-based)
        
    Returns:
        str: The question at the specified index
        
    Raises:
        IndexError: If the index is out of valid range
    """
    if 0 <= index < len(structured_questions):
        return structured_questions[index]
    else:
        raise IndexError(f"Index {index} out of range. Valid range: 0-{len(structured_questions)-1}")

# Function to get the total number of structured questions
def get_structured_questions_count():
    """
    Returns the total number of available structured questions.
    
    Returns:
        int: Total number of structured questions
    """
    return len(structured_questions)

# Function to get questions by category
def get_questions_by_category():
    """
    Returns questions organized by thematic categories.
    
    Returns:
        dict: Dictionary with categories as keys and question lists as values
    """
    categories = {
        "general_interruptions": [
            structured_questions[0],  # interruptions 2019-2023
            structured_questions[1],  # interruptions Manzanares
            structured_questions[2],  # transformer interruptions
            structured_questions[3]   # most frequent cause 2023
        ],
        "interruption_duration": [
            structured_questions[4],  # average duration last year
            structured_questions[5],  # average duration Caldas
            structured_questions[6]   # average duration switches
        ],
        "saidi_saifi_indicators": [
            structured_questions[7],  # SAIDI SAIFI San José
            structured_questions[8],  # SAIDI SAIFI before 2022
            structured_questions[9]   # SAIDI SAIFI network sections
        ],
        "municipality_analysis": [
            structured_questions[10], # 3 municipalities most interruptions
            structured_questions[11], # 3 municipalities fewest interruptions
            structured_questions[12], # municipality highest SAIDI SAIFI historical
            structured_questions[13]  # municipality lowest SAIDI SAIFI historical
        ],
        "equipment_and_dates": [
            structured_questions[14], # equipment type most interruptions Caldas
            structured_questions[15], # equipment type fewest interruptions 2021-2023
            structured_questions[16], # date most interruptions historical
            structured_questions[17], # date fewest interruptions historical
            structured_questions[18]  # equipment without interruptions Villa María
        ]
    }
    return categories