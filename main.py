from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI(title="House Price Prediction API")

# Load trained model
model = joblib.load("house_price_model.pkl")

# Template directory
templates = Jinja2Templates(directory="templates")


# ==============================
# HOME PAGE (HTML)
# ==============================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": None
        }
    )


# ==============================
# WEB PREDICTION (HTML FORM)
# ==============================
@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    area: float = Form(...),
    bedrooms: int = Form(...),
    bathrooms: int = Form(...)
):
    # Predict (original scale from model)
    prediction = model.predict([[area, bedrooms, bathrooms]])[0]

    # OPSI 2: konversi ke rupiah ribuan (x 1.000)
    prediction_real = prediction * 1_000

    result = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "price": f"Rp {prediction_real:,.0f}".replace(",", ".")
    }

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )


# ==============================
# API PREDICTION (JSON - SWAGGER)
# ==============================
@app.post("/api/predict")
def api_predict(
    area: float,
    bedrooms: int,
    bathrooms: int
):
    prediction = model.predict([[area, bedrooms, bathrooms]])[0]

    # OPSI 2: konversi ke rupiah ribuan (x 1.000)
    prediction_real = prediction * 1_000

    return {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "predicted_price": round(prediction_real),
        "predicted_price_rupiah": f"Rp {prediction_real:,.0f}".replace(",", ".")
    }
