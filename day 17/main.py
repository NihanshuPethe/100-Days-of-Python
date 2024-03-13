from question_model import Question
from data import question_data
from quiz_brain import Start_game

Question_Bank=[]
for item in question_data: #item is a dict
    object_of_question=Question(item["text"],item["answer"]) #make an object of question contain que and ans
    Question_Bank.append(object_of_question)
start_game=Start_game(Question_Bank)
keep_running=start_game.keep_running

while keep_running:
    start_game.run_game()
    keep_running=start_game.keep_running
