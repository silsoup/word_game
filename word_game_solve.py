import random
import time
import pyglet

correct_sound = pyglet.media.load("C:/Users/Admin/future_lab/word_game_problem/word_game/assets/good.wav", streaming=False)
incorrect_sound = pyglet.media.load("C:/Users/Admin/future_lab/word_game_problem/word_game/assets/bad.wav", streaming=False)

start_time = time.time()
words = []

def wordLoad():
    file_path = 'C:/Users/Admin/future_lab/word_game_problem/word_game/data/word.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            words.append(word)
    return words

def quiz_game(words, correct_sound, incorrect_sound, start_time):
    correctAnswer = 0
    wrongAnswer = 0

    for trial in range(5):
        givenWord = random.choice(words)
        print(f"*Question {trial + 1}")
        print(givenWord)
        userAnswer = input("Your answer: ")
        if givenWord == userAnswer:
            correct_sound.play()
            print("Correct\n")
            correctAnswer += 1
        else:
            incorrect_sound.play()
            print("Wrong\n")
            wrongAnswer += 1

    end_time = time.time()
    total_time = end_time - start_time
    time.sleep(1)

    if correctAnswer >= 3:
        print("Good job")
    else:
        print("Try again")
    print(f"***퀴즈 종료, 총 걸린 시간: {total_time:.2f}초, 문제 맞춘 갯수: {correctAnswer}")

words = wordLoad()
quiz_game(words, correct_sound, incorrect_sound, start_time)
