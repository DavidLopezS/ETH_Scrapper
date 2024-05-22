import schedule
from fastapi import FastAPI
from app.utils.scrapper import fetch_and_process_data 

app = FastAPI()

try:
    print("TEST")
    schedule.every(5).minutes.do(fetch_and_process_data)
except Exception as e:
    print(f"Something went wrong: {e}")