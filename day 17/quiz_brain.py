from question_model import Question
class Start_game:
    
    def __init__(self,question_bank) :
        self.questions_list=question_bank       #list of object
        self.score=0                         #defult do not need to pass
        self.question_number=1               #defult do not need to pass
        self.keep_running=True               #defult do not need to pass
    def still_run_the_game(self):
        if(self.question_number>len(self.questions_list)):
            self.keep_running=False
        else:
            self.keep_running=True

    def run_game(self):
        print(f"Your Score Is {self.score}")
        question = self.questions_list[self.question_number-1] #object of the question in the question list
        user_ans= input(f"Q {self.question_number} {question.text} True/False ? ")
        actual_ans=question.answer
        if (user_ans.lower()==actual_ans.lower()):
            print("Correct Answer ")
            self.score+=1
        else:
            print("Your Answer was Wrong ")
        print(f"Your score is {self.score}/{self.question_number}")
        self.question_number+=1
        Start_game.still_run_the_game(self)    
    
