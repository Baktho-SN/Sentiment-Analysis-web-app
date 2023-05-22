import joblib  # for loading model pickle file
import numpy as np  # for array conversion
import emoji # for emojis
from textblob import TextBlob # to find polrity score

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()  # instance of FastAPI class

# loads the ML model and count vectorizer
model = joblib.load(open("models/sentiment-analysis-model.pkl", "rb"))
c_vect = joblib.load(open("models/sa-countvect.pkl", "rb"))

# sets the templates folder for the app
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Function to render base.html at route '/' as a get request

    __Args__:
        - __request (Request)__: request in path operation that will return a template

    __Returns__:
        - __TemplateResponse__: render `base.html`
    """
    return templates.TemplateResponse("base.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    review: str = Form(...),
):
    """
    Function to predict sentiment of the review
    and shows the result by rendering base.html at route '/predict'

    Args:
    - __request (Request)__: request in path operation that will return a template
    - __review (str)__: review text

    Returns:
    - __TemplateResponse__: render `base.html`
    """

    rev = [review]  # str -> [str]
    blob = TextBlob(rev[0]) 
    result = blob.sentiment.polarity # polarity score

    data = c_vect.transform(rev).toarray()  # to convert the text to a matrix of token counts
    prediction = model.predict(data)  # prediction using naive bayes model
    print(prediction)
    
    output = (
        "This is most probably a positive review!"
        if prediction == 1 and result > -0.3
        else "This might most likely be a negative review..."
    )

    custom_emoji = (
        emoji.emojize(":grinning_face:")
        if prediction == 1 and result > -0.3
        else emoji.emojize(":face_without_mouth:")
    )

    return templates.TemplateResponse(
        "base.html", context={"prediction": output,"custom_emoji":custom_emoji, "request": request}
    )
