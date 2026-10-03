from fastapi import FastAPI, HTTPException
from serving.predict import predict

app = FastAPI()

@app.post("/predict")
def post_predict(body: dict):
    result = predict(body)
    if result is None:
        raise HTTPException(status_code=422, detail="sqft and bedrooms are required.")
    return result
