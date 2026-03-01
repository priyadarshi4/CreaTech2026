from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from optimizer.cycle_optimizer import optimize_cycle

app = FastAPI()

templates = Jinja2Templates(directory="api/templates")


# Dashboard UI
@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# AI Prediction API
@app.post("/predict")
def predict(
    temperature: float,
    humidity: float,
    w_c_ratio: float,
    cement_type: int,
    curing_time: int
):

    data = [
        temperature,
        humidity,
        w_c_ratio,
        cement_type,
        curing_time
    ]

    result = optimize_cycle(data)

    return result