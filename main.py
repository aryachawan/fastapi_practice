from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.userinput import UserInput
from model.predict import predict_output,MODEL_VERSION,model
from schema.prediction_response import PredictionResponse

app = FastAPI()
     
@app.get("/")
def home():
    return {'message':'Insurance premium prediction API'}


@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'version':MODEL_VERSION
    }


@app.post("/predict",response_model=PredictionResponse)
def predict_premium(data: UserInput):
    user_input = {
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200,content={'response': prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))