# CRITAIR Results Configuration
# =========================

# File naming conventions
UNSTRUCTURED_FILE = "unstructured_data_results.csv"
STRUCTURED_FILE = "structured_data_results.csv"
RECOMMENDATIONS_FILE = "recommendations_results.csv"

# Report settings
CHART_DPI = 300
CHART_FORMAT = "png"
REPORT_FORMAT = "pdf"

# Analysis parameters
TOP_N_MODELS = 10
BALANCE_THRESHOLD = 20.0  # Models with balance > this are considered poor

# Colors for visualizations
CATEGORY_COLORS = {
    'Unstructured': '#2E86AB',      # Blue
    'Structured': '#A23B72',       # Magenta  
    'Recommendations': '#F18F01'   # Orange
}

# Model groupings for analysis
MODEL_PROVIDERS = {
    'OpenAI': ['gpt-3.5 turbo', 'gpt 4o'],
    'Google': ['Gemini 2.0', 'Gemini 2.5'],
    'Meta': ['Llama 3.1:8b', 'Llama 3.2:1b'],
    'Alibaba': ['Qwen 2.5:1.5b', 'Qwen 2.5:7b'],
    'DeepSeek': ['DeepSeek-r1:7b', 'DeepSeek-r1:1.5b']
}