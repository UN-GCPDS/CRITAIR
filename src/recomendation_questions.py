# RECOMMENDATION QUESTIONS
# Questions related to electrical regulations and RETIE

recomendation_questions = [
    "¿Qué tipo de aislador se recomienda en zonas con alto nivel de contaminación?",
    "¿Qué estándares internacionales deben cumplir los aisladores utilizados en redes eléctricas?",
    "¿Qué aspectos considerar al seleccionar un aislador para una línea de transmisión?",
    "¿Qué materiales se recomiendan para postes eléctricos en zonas costeras?",
    "¿Cuáles son las distancias mínimas de seguridad para apoyos eléctricos?",
    "¿Qué pruebas deben realizarse para garantizar la calidad estructural de los apoyos?",
    "¿Cuándo es necesario utilizar fusibles tipo expulsion?",
    "¿Qué parámetros se deben considerar al seleccionar un fusible para una línea de 13.2 kV?",
    "¿Qué normativa regula el uso de dispositivos de protección contra sobretensiones en Colombia?",
    "¿Qué tipos de conductores se recomiendan para líneas aéreas de media tensión?",
    "¿Cuáles son las distancias mínimas entre conductores en líneas aéreas de media tensión?",
    "¿Qué características debe tener un sistema de puesta a tierra en líneas aéreas de media tensión?",
    "¿Qué especificaciones deben cumplir los conductores en instalaciones eléctricas residenciales?",
    "¿Qué medidas de protección son obligatorias en instalaciones eléctricas residenciales?",
    "¿Cómo afecta la contaminación ambiental a la operación de redes eléctricas aéreas?",
    "¿Qué normativas aplican al diseño de redes eléctricas en zonas con alta incidencia de rayos?",
    "¿Qué estrategias se recomiendan para reducir pérdidas técnicas en redes aéreas?",
    "¿Qué requisitos debe cumplir una instalación eléctrica para obtener la certificación RETIE?",
    "¿Qué sistemas eléctricos requieren diseño detallado según el RETIE?"
]

# Function to get the questions
def get_recomendation_questions():
    """
    Returns the list of recommendation questions related to electrical regulations.
    
    Returns:
        list: List of strings with the questions
    """
    return recomendation_questions

# Function to get a specific question by index
def get_question_by_index(index):
    """
    Returns a specific question by its index.
    
    Args:
        index (int): Question index (0-based)
        
    Returns:
        str: The question at the specified index
        
    Raises:
        IndexError: If the index is out of valid range
    """
    if 0 <= index < len(recomendation_questions):
        return recomendation_questions[index]
    else:
        raise IndexError(f"Index {index} out of range. Valid range: 0-{len(recomendation_questions)-1}")

# Function to get the total number of questions
def get_questions_count():
    """
    Returns the total number of available questions.
    
    Returns:
        int: Total number of questions
    """
    return len(recomendation_questions)