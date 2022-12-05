# add a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow then to answer
# tell them if they are right or wrong
# show the final result wje  quiz is completed

quiz = {
    "question1": {
        "question": "Who is the father of computer ?",
        "answer": "Charles Babbage"
    },
    "question2": {
        "question": "Who is the father of Geometry?",
        "answer": "Euclid"
    },
    "question3": {
        "question": "Which of the following is not associated with the UNO?",
        "answer": "ASEAN"
    },
    "question4": {
        "question": "Who invented the BALLPOINT PEN?",
        "answer": "Biro Brothers"
    },
    "question5": {
        "question": "Which scientist discovered the radioactive element radium?",
        "answer": "Marie Curie"
    },
    "question6": {
        "question": "Hitler party which came into power in 1933 is known as ?",
        "answer": "Nazi Party"
    },
    "question7": {
        "question": "Ecology deals with ?",
        "answer": "Relation between organisms and their environment"
    },
    "question8": {
        "question": "Hamid Karzai was chosen president of Afghanistan in ?",
        "answer": "2002"
    },
    "question9": {
        "question": "Durand Cup is associated with the game of ?",
        "answer": "Football"
    },
}


score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer ?")

    if answer.lower() == value['answer'].lower():
        print('-------------------------   CORRECT!!!!!!  ---------------------------')
        score += 1
        print(f"Your score is {score}")
        print("")
        print("")
    else:
        print('-------------------------   WRONG!!!!!!  ---------------------------')
        print("The answer is: " + value['answer'])
        print(f"Your score is {score}")
        print("")
        print("")
        break;

        

print("You got " + str(score) + " cout of 9 questions correctly")

correct_percentage = int(score // 9 * 100)
print("The correct percentage is " + correct_percentage + "%");