import uvicorn
from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = FastAPI()



@app.post("/sentiment")
async def get_sentiment(text: str):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(text)
    sentiment = None
    if result["compound"] >= 0.05:
        sentiment = "Positive"
    elif result["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return f"The sentiment of the text is: {sentiment} and the Score is: {round(result['compound'], 2)}"

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)