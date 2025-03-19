from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]

def a_function(a,b):
    Question(a,b)

for a in question_data:
    question=a["text"]
    answer=a["answer"]
    qa_pair=Question(question,answer)
    question_bank.append(qa_pair)
    # question_bank.append(Question(a["text"],a["answer"]))

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"you final score is {quiz.score}/{quiz.question_no}")

