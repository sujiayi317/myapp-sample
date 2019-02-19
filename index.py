
# this is my app!
# login Form
'''quizgame.py a quiz game'''
import random


def read_answer():
    ans = input("Answer (A, B, C or D)").upper()
    while ans not in ['A', 'B', 'C', 'D']:
        print("Invalid input, try again")
        ans = input("Answer (A, B, C or D)").upper()
    return ord(ans) - 64


def ask_question(q, p):
    print()
    print("Category:", q[5])
    print("Difficulty:", q[6])
    print(q[0])
    for i in range(1, 5):
        print(chr(64 + i), q[p[i - 1]])


def play_game(totnum=5):
    lines = open('quiz.csv', encoding="utf-8").read().split('\n')
    # same as ....read().splitlines()
    questions = []
    for line in lines:
        questions.append(line.split('\t'))
    # print(line.split('\t'))

    score = 0
    #    rndlst=list(range(len(questions)))
    #    random.shuffle(rndlst)
    for i in range(totnum):
        # create a random permutation for the order of answers
        p = [1, 2, 3, 4]
        random.shuffle(p)

        # pick a random question for the list of questions
        q = random.choice(questions)  # questions[i]
        ask_question(q, p)
        ans = read_answer()

        if (p[ans - 1] == 1):  # test if the answer is correct.
            score = score + int(q[-1])  # increase the score by the difficulty level
            print("Correct! Your current score is: ", score)
        else:
            print("Wrong! The correct answer was: ", q[1])
    print("\nQuiz Finished! Your final score is", score)


play_game()
