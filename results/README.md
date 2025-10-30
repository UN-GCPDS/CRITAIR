# CRITAIR Results

This directory contains the results from the AI models evaluation using BertScore methodology.

## 📁 Directory Structure

```
results/
├── README.md                           # This file
├── tables/                            # Results tables in CSV format
│   ├── unstructured_data_results.csv  # Results for unstructured questions (RAG)
│   ├── structured_data_results.csv    # Results for structured questions (DataFrames)
│   └── recommendations_results.csv    # Results for technical recommendations
└── reports/                           # Generated reports and visualizations
    └── (PDF reports will be placed here)
```

## 📊 Results Summary

### Unstructured Data Analysis (RAG)
- **Best BertScore**: GPT-3.5 Turbo (0.9847)
- **Fastest Response**: Llama 3.2:1b (9.43s)
- **Best Balance**: GPT-3.5 Turbo (11.72)

### Structured Data Analysis (DataFrames)
- **Best BertScore**: GPT-3.5 Turbo (0.9562)
- **Fastest Response**: Llama 3.2:1b (3.05s)
- **Best Balance**: GPT-3.5 Turbo (3.24)

### Technical Recommendations
- **Best BertScore**: Gemini 2.5 (0.8232)
- **Fastest Response**: GPT-3.5 Turbo (2.23s)
- **Best Balance**: GPT-3.5 Turbo (3.00)

## 📈 Key Metrics

- **BertScore**: Semantic similarity score (0-1, higher is better)
- **Inference Time**: Average response time in seconds
- **Balance**: Combined metric considering both quality and speed

## 🏆 Overall Performance Rankings

### Top 3 Models by Category:

**Unstructured Data (RAG):**
1. GPT-3.5 Turbo - Excellent accuracy with reasonable speed
2. Llama 3.2:1b - Good balance of speed and quality
3. Gemini 2.0 - Moderate performance across metrics

**Structured Data (DataFrames):**
1. GPT-3.5 Turbo - Superior accuracy and speed
2. GPT-4o - High accuracy with moderate speed
3. Gemini 2.5 - Reasonable performance for complex queries

**Technical Recommendations:**
1. GPT-3.5 Turbo - Best overall balance
2. Gemini 2.0 - Good quality with fast response
3. Llama 3.2:1b - Efficient processing with decent quality

## 📋 Data Notes

- All BertScore values use Spanish language baseline rescaling
- Times are measured in seconds (average across multiple runs)
- Balance metric = Inference Time / BertScore (lower is better)
- Negative BertScores indicate poor semantic alignment
- Results based on Colombian electrical regulations (RETIE) context

## 🔄 Reproducibility

These results were generated using:
- BertScore with Spanish language configuration
- Temperature = 0 for deterministic results
- Consistent evaluation methodology across all models
- Same dataset and evaluation criteria for all tests

For methodology details, see the main project notebooks in `/notebooks/`.