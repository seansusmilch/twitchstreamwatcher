if (!(Test-Path .\secrets.py)) {
    python .\setup.py
}
.\skream\Scripts\activate.ps1
python .\watchStream.py