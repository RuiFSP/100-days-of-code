from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from cleaning_data import my_saved_list

question_bank = []


# for data in question_data - old version
# #  question_bank.append(Question(data["text"], data["answer"]))


for i in range(len(my_saved_list)):
    question_bank.append(Question(my_saved_list[i]['text'], my_saved_list[i]['answer']))

# new quiz brain object
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    if not quiz.still_has_questions():
        print("You have completed the quiz")
        print(f"You final score is {quiz.score}/{quiz.question_number}")
