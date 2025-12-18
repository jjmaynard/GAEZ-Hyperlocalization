"""
Vercel serverless function entry point for GAEZ API.
This file creates a handler that Vercel can use to run the FastAPI application.
"""

import sys
import os
from pathlib import Path

# Get the project root directory (parent of api/)
current_dir = Path(__file__).parent
project_root = current_dir.parent

# Add the US_scripts directory to the Python path
us_scripts_dir = project_root / "code" / "US_scripts"
sys.path.insert(0, str(us_scripts_dir))

# Set PYTHONPATH environment variable
os.environ['PYTHONPATH'] = str(us_scripts_dir) + ':' + os.environ.get('PYTHONPATH', '')

# Import the FastAPI app from the api module
from api.main import app

# Vercel expects a variable named 'app' or we use Mangum for AWS Lambda compatibility
try:
    from mangum import Mangum
    handler = Mangum(app, lifespan="off")
except ImportError:
    # If mangum is not available, export app directly
    handler = app

# Export both for compatibility
__all__ = ['app', 'handler']
