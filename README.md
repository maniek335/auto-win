## Setup

1. Install Python 3.12
2. Open project in VS Code
3. Create virtual environment
   1. In VS Code use shortcut `CTRL + SHIFT + P`
   2. Run `Python: Create Environment...`
   3. Select `Venv`
   4. Select `Python 3.12`
   5. Select `requirements.txt`

## Development

Start the development application:

```powershell
python src/app.py
```

## Production

Build the application for production:

```powershell
python -m PyInstaller --clean --onefile --console --uac-admin --name auto-win src/app.py
```

Run the application:

```powershell
dist/auto-win.exe
```
