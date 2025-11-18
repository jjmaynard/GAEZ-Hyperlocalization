#!/usr/bin/env python3
"""
Startup script for GAEZ Soil Quality Index API.

Usage:
    python run_api.py                    # Run on default port 8000
    python run_api.py --port 8080        # Run on custom port
    python run_api.py --host 0.0.0.0     # Bind to all interfaces
    python run_api.py --reload           # Enable auto-reload (development)
"""

import argparse
import sys
import logging
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    import uvicorn
except ImportError:
    print("Error: uvicorn not installed.")
    print("Install requirements: pip install -r api/requirements.txt")
    sys.exit(1)


def setup_logging(log_level: str = "INFO"):
    """Setup logging configuration."""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def main():
    """Main entry point for API server."""
    parser = argparse.ArgumentParser(
        description="GAEZ Soil Quality Index API Server"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind to (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (default: 8000)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level (default: INFO)"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of worker processes (default: 1)"
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)

    logger.info("="*80)
    logger.info("GAEZ Soil Quality Index API")
    logger.info("="*80)
    logger.info(f"Host: {args.host}")
    logger.info(f"Port: {args.port}")
    logger.info(f"Workers: {args.workers}")
    logger.info(f"Reload: {args.reload}")
    logger.info(f"Log Level: {args.log_level}")
    logger.info("")
    logger.info(f"API Documentation: http://{args.host if args.host != '0.0.0.0' else 'localhost'}:{args.port}/docs")
    logger.info(f"Health Check: http://{args.host if args.host != '0.0.0.0' else 'localhost'}:{args.port}/health")
    logger.info("="*80)

    # Run server
    try:
        uvicorn.run(
            "api.main:app",
            host=args.host,
            port=args.port,
            reload=args.reload,
            workers=args.workers if not args.reload else 1,  # Workers don't work with reload
            log_level=args.log_level.lower(),
            access_log=True
        )
    except KeyboardInterrupt:
        logger.info("\nShutting down server...")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
