from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run-script/")
async def run_script(file: UploadFile = File(...)):
    contents = await file.read()
    path = "/tmp/script.py"
    with open(path, "wb") as f:
        f.write(contents)
    # Ensure the script is run in a safe, isolated environment
    result = subprocess.run(["python", path], capture_output=True, text=True)
    os.remove(path) 
    return {"stdout": result.stdout, "stderr": result.stderr}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6006)
