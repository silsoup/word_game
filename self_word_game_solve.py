#Preparation - import moules
## 단어장에서 랜덤출력
import random
## 효과음
import pyglet

## 퀴즈 푸는 시간 측정 모듈
import time
start_time = time.time()

# 소리 파일 로드
correct_sound = pyglet.media.load("C:/Users/Admin/future_lab/word_game_problem/word_game/assets/good.wav", streaming=False)
incorrect_sound = pyglet.media.load("C:/Users/Admin/future_lab/word_game_problem/word_game/assets/bad.wav", streaming=False)


#단어장 파일 불러오기
# word.txt 파일 경로
file_path = 'C:/Users/Admin/future_lab/word_game_problem/word_game/data/word.txt'

# 단어를 저장할 리스트
words = []

# 파일을 읽고 단어를 리스트에 추가
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 공백과 오른쪽 뉴라인 캐릭터 제거
        word = line.strip()
        # 단어를 리스트에 추가
        words.append(word)

# 결과 출력 (확인용)
#print(words)

#정답과 오답 갯수 초기화
correctAnswer =0
wrongAnswer =0

# 퀴즈 코드 실행
for trial in range(5):
    # 단어 랜덤출력
    givenWord = random.choice(words)
    print(f"*Question{trial+1}")
    print(givenWord)
    #사용자의 입력 받기
    userAnswer = input("Your answer:")
    if givenWord==userAnswer:
        correct_sound.play()
        print("Correct\n")
        correctAnswer = correctAnswer+1
    else:
        incorrect_sound.play()
        print("Wrong\n")        
        wrongAnswer = wrongAnswer+1
# 마지막 경고음을 듣기 위한 휴식
end_time = time.time()  # 게임 종료 시간 기록
total_time = end_time - start_time  # 총 걸린 시간 계산 
time.sleep(1) 

# 합격 불합격 판단하기
if correctAnswer>=3:
    print("Good job")
else:
    print("Try again")
print(f"***퀴즈 종료, 총 걸린 시간: {total_time:.2f}초, 문제 맞춘 갯수: {correctAnswer}")
