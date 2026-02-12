import sys
import uvicorn
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))


def runserver(host: str = "0.0.0.0", port: int = 8585, reload: bool = True):
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload
    )


def shell():
    import asyncio
    from main import app
    from core.database import db
    from core.telegram import telegram
    
    async def setup():
        await db.connect_db()
        await telegram.connect()
        return {
            'app': app,
            'db': db,
            'telegram': telegram
        }
    
    context = asyncio.run(setup())
    
    try:
        from IPython import embed
        embed(user_ns=context)
    except ImportError:
        import code
        code.interact(local=context)


def main():
    if len(sys.argv) < 2:
        print("Usage: python manage.py [command]")
        print("\nAvailable commands:")
        print("  runserver  - Run development server")
        print("  shell      - Start interactive shell")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "runserver":
        runserver()
    elif command == "shell":
        shell()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
