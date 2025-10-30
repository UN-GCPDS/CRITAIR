# CRITAIR Project Configuration

# Python Path Configuration
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Project Information
export CRITAIR_VERSION="1.0.0"
export CRITAIR_PROJECT_ROOT="$(pwd)"

echo "✅ CRITAIR environment configured"
echo "📁 Project root: $CRITAIR_PROJECT_ROOT"
echo "🐍 Python path includes: $(pwd)/src"