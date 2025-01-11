import uvicorn
import tempfile
import shutil
import os
import warnings
import logging


from logging.handlers import RotatingFileHandler
from fastapi import FastAPI, File, UploadFile,Form, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse,FileResponse , JSONResponse,HTMLResponse



from src_v1.help import audio_basic_process

warnings.filterwarnings("ignore")

app=FastAPI(title="Fritzband",
    description="FastAPI",
    version="0.115.4")


# Allow all origins (replace * with specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 




@app.get("/")
async def root():

  return {"Fast API":"API is working"}




logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)



@app.post("/audio_classification_lstm_mfcc")
async def audio_classification_lstm_mfcc(audio_file: UploadFile = File(...)):
    try:
        logger.info(f"input data send to the script ******************************")
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        # Create a temporary file path
        temp_file_path = os.path.join(temp_dir,audio_file.filename)

        # Write the uploaded file content to the temporary file
        with open(temp_file_path, "wb") as temp_file:
            shutil.copyfileobj(audio_file.file, temp_file)

            
        reports=audio_basic_process(temp_file_path)

        # Clean up: Remove the temporary directory and its contents
        shutil.rmtree(temp_dir)

    except Exception as e:

        logger.info(f"Error message {e}")
        return {"status":0,"Message":f"Exception error:{e}"}
    
    else:

        logger.info(f"Return output {reports} ******************************")  
        return   {"status":1,"class_details": reports}
        
            





if __name__=="__main__":
    
    uvicorn.run("app:app",host="0.0.0.0", port=8000, reload=True)
