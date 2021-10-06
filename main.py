from app import app
import schedule
import time
from config import load_config

# load config
config = load_config("config.yaml")
interval = config["interval"]

def job():
    try:
        app(config)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    job() # test
    schedule.every(interval).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
