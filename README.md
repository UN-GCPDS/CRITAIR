# CRITAIR - AI Model Precision and Time Analysis

This project analyzes the precision and response times of different AI models using structured and unstructured questions related to Colombian electrical regulations (RETIE).

## Initial Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd critair
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install python-dotenv langchain langchain-openai langchain-google-genai langchain-community langchain-experimental pandas numpy matplotlib seaborn httpx tabulate openpyxl chromadb
```

### 3. Configure environment variables

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and complete with your real keys:
   ```
   OPENAI_API_KEY=your-openai-key-here
   GOOGLE_API_KEY=your-google-key-here
   ```

3. (Optional) Set up Python path for development:
   ```bash
   source setup_env.sh
   ```

### 4. Get API Keys

- **OpenAI API Key**: Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Google API Key** (for Gemini): Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

## Project Structure

```
critair/
├── .env.example              # Environment variables template
├── .env                      # Environment variables (not included in git)
├── .gitignore               # Files excluded from repository
├── requirements.txt         # Project dependencies
├── setup_env.sh             # Environment setup script
├── PRIVATE_DATA.md          # Privacy and confidentiality notice
├── README.md               # This file
├── notebooks/              # Jupyter notebooks
│   ├── setup_imports.py     # Import configuration helper
│   ├── probes_times_precision.ipynb     # Main analysis notebook
│   └── Get_The_Best_Model_using_BertScore.ipynb  # BertScore evaluation
├── results/                # Evaluation results and reports
│   ├── README.md           # Results documentation
│   ├── metadata.json       # Experiment metadata
│   ├── config.py          # Results configuration
│   ├── analyze_results.py  # Analysis and visualization script
│   ├── tables/            # Results in CSV format
│   │   ├── unstructured_data_results.csv
│   │   ├── structured_data_results.csv
│   │   └── recommendations_results.csv
│   └── reports/           # Generated reports and visualizations
└── src/                    # Source code modules
    ├── __init__.py         # Package initialization
    ├── tools.py            # LangChain tools for document querying
    ├── utils.py            # Modular utility functions
    ├── unstructured_questions.py   # Questions for RAG analysis
    ├── structured_questions.py    # Questions for DataFrame analysis
    └── recomendation_questions.py # Questions for recommendations
```

## Usage

1. Navigate to the notebooks directory: `cd notebooks/`
2. Open the main notebook `probes_times_precision.ipynb`
3. Run the first cell to load environment variables and all imports
4. Run the other cells according to your specific analysis

### Available Notebooks

- **`probes_times_precision.ipynb`**: Main analysis notebook for precision and time evaluation
- **`Get_The_Best_Model_using_BertScore.ipynb`**: Comprehensive BertScore evaluation system

## Analysis Types

- **Unstructured Questions**: RAG analysis with normative documents
- **Structured Questions**: DataFrame analysis with pandas
- **Recommendation Questions**: Contextualized RETIE evaluation

## Supported Models

- OpenAI GPT (3.5-turbo, 4o)
- Google Gemini (2.0-flash, 2.5-pro)
- Ollama (llama3.1, llama3.2, qwen2.5, deepseek-r1)

## Source Code Modules (`src/`)

### `utils.py` - Modular Utilities
Contains auxiliary functions for data processing and analysis:
- `verify_substring()`: Substring verification in text
- `normalize_variable_name()`: Normalization of meteorological variable names
- `create_llm_chat_model()`: LLM chat model creation
- `recomendacion()`: Technical recommendation generation for infrastructure
- `save_results_to_pickle()`, `load_results_from_pickle()`: Pickle file management

### `tools.py` - LangChain Tools
Specialized tools for querying Colombian normative documents including RETIE chapters, resolutions, and technical standards.

### Question Modules
- `unstructured_questions.py`: Questions for RAG analysis with regulatory documents
- `structured_questions.py`: Questions for DataFrame analysis with pandas agents
- `recomendation_questions.py`: Contextualized RETIE evaluation questions

### `__init__.py` - Package Configuration
Package initialization with version information and module descriptions.

## 📊 Results and Analysis

The `results/` directory contains comprehensive evaluation results and analysis tools:

### Key Findings
- **Best Overall Performance**: GPT-3.5 Turbo (consistent across all categories)
- **Best Open Source**: Llama 3.2:1b (excellent speed-quality balance)
- **Fastest Response**: GPT-3.5 Turbo (2.23s average for recommendations)
- **Highest Accuracy**: GPT-3.5 Turbo (0.9847 BertScore for unstructured data)

### Results Categories
1. **Unstructured Data (RAG)**: Document analysis with regulatory texts
2. **Structured Data (DataFrames)**: Tabular data processing with pandas agents  
3. **Technical Recommendations**: Contextualized RETIE evaluations

### Analysis Tools
- `analyze_results.py`: Generate visualizations and summary statistics
- CSV tables with raw results for each category
- Comprehensive metadata and configuration files

For detailed results, see `/results/README.md`

## 🔒 Data Privacy and Confidentiality

### CHEC Private Data
**IMPORTANT**: The data used in the structured analysis comes from CHEC (Centrales Eléctricas de Nariño) company and contains confidential operational information.

#### ❌ Not Included in Repository:
- `Tabla_General.csv` - Transformer event data
- Any files in paths containing `Dashboard_Criticidad` or `Dashboard_CHEC`
- Analysis results containing real CHEC data
- Files with sensitive electrical infrastructure information

#### ✅ Functionality without Private Data:
The notebook is designed to work without private data:
- **Automatic detection**: Verifies if data is available
- **Example data**: Creates synthetic data for demonstration
- **Informative messages**: Explains when private data is missing
- **Complete analysis**: All functions work with example data

#### 🛡️ For Users with Authorized Access:
If you have legitimate access to CHEC data:
1. Place `Tabla_General.csv` in the specified path
2. The notebook will automatically detect real data
3. **DO NOT SHARE** results containing real data
4. Respect CHEC confidentiality policies

## 🔐 General Security

- **NEVER** commit the `.env` file with your real keys
- **NEVER** upload confidential CHEC data to the repository
- Keys and private data are included in `.gitignore`
- Use the `.env.example` file as reference for configuration
- Always review which files you're about to commit before pushing