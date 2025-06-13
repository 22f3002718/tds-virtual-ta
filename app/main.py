from fastapi import FastAPI
from pydantic import BaseModel
from app.qa_engine import generate_answer

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: str = None  # Optional base64 image

@app.post("/")
async def answer_question(req: QuestionRequest):
    answer, links = generate_answer(req.question)
    return {
        "answer": answer,
        "links": [{"url": l["url"], "text": l["title"]} for l in links]
    }
    