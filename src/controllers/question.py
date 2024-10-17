from sqlalchemy import func
from models.question import Question
from utils.database import session

# Handler for /api/questions/common
def getCommonHandler():
    questions = session.query(Question.text).all()
    return questions
