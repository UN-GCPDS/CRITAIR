"""
Setup script for importing modules from the src directory when running notebooks.
Add this at the beginning of notebooks to ensure proper module importing.
"""

import sys
import os
from pathlib import Path

def setup_imports():
    """
    Add the src directory to Python path for importing project modules.
    This function should be called at the beginning of each notebook.
    """
    # Get the project root directory (parent of notebooks directory)
    notebook_dir = Path.cwd()
    if notebook_dir.name == 'notebooks':
        project_root = notebook_dir.parent
    else:
        # If not in notebooks directory, assume current directory is project root
        project_root = notebook_dir
    
    src_path = project_root / 'src'
    
    if src_path.exists() and str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
        print(f"✅ Added {src_path} to Python path")
    else:
        print(f"⚠️  Source path {src_path} not found or already in path")

if __name__ == "__main__":
    setup_imports()