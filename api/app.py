"""
Alternative entry point that directly imports from the existing API structure.
"""
import sys
import os
from pathlib import Path

# Setup paths
base_path = Path(__file__).parent.parent
sys.path.insert(0, str(base_path / "code" / "US_scripts"))

# Import FastAPI app
try:
    from api.main import app
    
    # For Vercel serverless
    try:
        from mangum import Mangum
        handler = Mangum(app, lifespan="off")
    except ImportError:
        handler = app
        
except ImportError as e:
    # Fallback simple app if imports fail
    from fastapi import FastAPI
    app = FastAPI()
    
    @app.get("/")
    def root():
        return {"error": f"Import failed: {str(e)}", "path": str(base_path)}
    
    handler = app
