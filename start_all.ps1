# Start Reflex frontend (Conda)
Start-Process powershell -ArgumentList "conda activate PipStop; cd `"$PWD`"; reflex run" -NoNewWindow

# Start FastAPI backend (venv)
Start-Process powershell -ArgumentList "cd `"$PWD\Backend`"; ..\venv\Scripts\Activate.ps1; uvicorn Backend.main:app --reload --port 8000" -NoNewWindow

Write-Host "✅ Both Reflex frontend and FastAPI backend are starting!"
