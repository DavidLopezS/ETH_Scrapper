import schedule, time, threading
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.utils.scrapper import fetch_and_process_data 

app = FastAPI()

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule.every(5).minutes.do(fetch_and_process_data)
schedule_thread = threading.Thread(target=run_scheduler, daemon=True)
schedule_thread.start()

@app.post("/trigger")
def trigger_scraping():
    try:
        fetch_and_process_data()
        return JSONResponse(content={"message": "Data fetched and processed successfully."}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": f"An error occurred: {e}"}, status_code=500)
