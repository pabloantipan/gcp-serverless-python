from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_index():
    return {"Hey": "there!"}


@app.post("/scrape")
def trigger_scraping():
    return {"scraping": "yes!"}
