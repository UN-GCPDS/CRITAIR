# CRITAIR Makefile
# Automation for common project tasks

.PHONY: help setup analyze clean install test

help:
	@echo "CRITAIR - AI Models Evaluation Framework"
	@echo "========================================"
	@echo ""
	@echo "Available commands:"
	@echo "  setup     - Set up project environment"
	@echo "  install   - Install dependencies"
	@echo "  analyze   - Generate results analysis and visualizations"  
	@echo "  clean     - Clean generated files"
	@echo "  test      - Run basic import tests"
	@echo "  help      - Show this help message"

setup:
	@echo "🚀 Setting up CRITAIR environment..."
	chmod +x setup_env.sh
	cp .env.example .env
	@echo "✅ Setup complete!"
	@echo "📝 Remember to edit .env with your API keys"

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

analyze:
	@echo "📊 Generating results analysis..."
	cd results && python analyze_results.py
	@echo "✅ Analysis complete! Check results/reports/ for outputs"

clean:
	@echo "🧹 Cleaning generated files..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +
	rm -rf results/reports/*.png
	rm -rf results/reports/*.pdf
	@echo "✅ Cleanup complete!"

test:
	@echo "🧪 Running basic import tests..."
	cd notebooks && python setup_imports.py
	@echo "✅ Import tests passed!"

requirements:
	@echo "📋 Generating requirements.txt..."
	pip freeze > requirements.txt
	@echo "✅ Requirements updated!"

structure:
	@echo "📁 Project structure:"
	@echo "critair/"
	@find . -type f -name ".*" -prune -o -print | head -20 | sed 's|[^/]*/|  |g'