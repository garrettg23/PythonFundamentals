# Skeletal Structure for Quick Game

# ------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------")  #line break, prints line break then prints each key then iterates through.
        print(key)
        for i in options[question_num - 1]:    #nested for loop to print only first list for first question and so on.
                                               #question_num -1 gives 0. So only prints the correct option set for the question.
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)    #adds to list of guesses. tracks guesses basically

        correct_guesses += check_answer(questions.get(key),guess)    #adds a 1 everytime you answer correct. from check ans function.
        question_num += 1     #increments question num by 1. in outer for loop

    display_score(correct_guesses, guesses)    #outside of loop when done, arguments are correct guesses and all guesses.
# ------------------------
def check_answer(answer , guess):

    if answer == guess:
        print("CORRECT!")
        return 1      #return 1 for 1 point.
    else:
        print("WRONG!")
        return 0      #returns 0 points
# ------------------------
def display_score(correct_guesses, guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")
    print("Answers: ", end="")   #no new line for each answer
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)    #prints percentage
    print("You scored "+str(correct_guesses)+" points! Your grade is "+ str(score)+ "%!")




# ------------------------
def play_again():

    response = input("Do you want to play again? (Yes or No): ").upper()

    if response == "YES":
        return True
    else:
        return False



#set of questions... Key value pair, with key being question value being the correct answer.
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ":"C",
    "Is the earth round?: ":"A"
}
# 2d list to capture all the answer options. List of tuples would also work.
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. The Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. WTF is earth"]]

new_game()
while play_again():   #after new game then asks if the user wants to play again. If they say anything other then yes, it ends
    new_game()

print("Cya bitch!")