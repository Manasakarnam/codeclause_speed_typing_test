import time
import random
def typing_test():
    words = ['python', 'programming', 'language', 'computer', 'science', 'algorithm', 'data', 'structure']
    score = 0
    print('Welcome to the Typing Test!')
    print('You will have to type as many words as you can in 30 seconds.')
    input('Press Enter to start.')
    start_time = time.time()
    while time.time() - start_time < 30:
        word = random.choice(words)
        print(word)
        user_input = input()
        if user_input == word:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct word was:', word)
    print('Time is up!')
    print('Your score is:', score)

typing_test()