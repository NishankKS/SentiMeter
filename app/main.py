# Importing FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Used for caching
from functools import lru_cache
from pyabsa import AspectPolarityClassification as APC

app = FastAPI()

# Adding Middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@lru_cache
def init():
    """initializer
    Method used to initialize Sentiment Classifier based on DistillBert.

    Returns:
        model: SentimentClassifier
    """
    return APC.SentimentClassifier('multilingual', auto_device=True,
                                   cal_perplexity=True)


classifier = init()


@app.get("/")
def home():
    """Testing FASTAPI
    """
    return {"message": "Hello world!"}


@app.post("/sentiment")
async def getSentiment(info: Request):
    req_info = await info.json()
    text = list(req_info['text'])

    sentiment = classifier.predict(text, save_result=True, print_result=True,
                                   ignore_error=True, pred_sentiment=True)

    return {
        "Response": "Success",
        "aspect": sentiment[0]['aspect'],
        "sentiment": sentiment[0]['sentiment']
    }


@app.post("/aspect")
async def getAspect(info: Request):
    req_info = await info.json()
    text = list(req_info['text'])
    aspects = req_info['aspect']

    for aspect in aspects:
        text[0] = text[0].replace(aspect, f'[B-ASP]{aspect}[E-ASP]')

    sentiment = classifier.predict(text, save_result=True, print_result=True,
                                   ignore_error=True, pred_sentiment=True)

    return {
        "Response": "Success",
        "aspect": sentiment[0]['aspect'],
        "sentiment": sentiment[0]['sentiment']
        }
