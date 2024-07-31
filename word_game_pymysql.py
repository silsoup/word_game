#Preparation - import moules
from datetime import datetime

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
time.sleep(1) 

#시간 기록
end_time = time.time()  # 게임 종료 시간 기록
total_time = end_time - start_time  # 총 걸린 시간 계산 
current_time = datetime.now().strftime("%H:%M:%S")

# 합격 불합격 판단하기
if correctAnswer>=3:
    print("Good job")
else:
    print("Try again")
print(f"***퀴즈 종료, 총 걸린 시간: {total_time:.2f}초, 문제 맞춘 갯수: {correctAnswer}")
print("+++++++++++++++result++++++++++++++++")
print("정답 갯수 | 걸린 시간 | 등록 시간 | 등수")

# DB connection
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='silsoup', passwd='0000', db='games_db', charset='utf8')

# DB 테이블과 연결하여 sql문 실행을 위한 객체
cursor = conn.cursor()

# INSERT INTO *TABLE NAME* 잊지말자... DB이름 아니고 table 이름이다
INSERT_SQL = "INSERT INTO wordgame(corr_cnt, exe_time, reg_date) VALUES (%s, %s, %s);"
cursor.execute(INSERT_SQL, (correctAnswer, total_time, current_time))
conn.commit()

# Retrieve the rank for the latest entry
RANK_SQL = """
SELECT id, rank() over (order by corr_cnt DESC, exe_time ASC) AS irank 
FROM wordgame 
ORDER BY id DESC 
LIMIT 1;
"""
cursor.execute(RANK_SQL)
latest_entry = cursor.fetchone()
latest_id = latest_entry[0]
latest_rank = latest_entry[1]

# Update the table with the rank
UPDATE_SQL = "UPDATE wordgame SET irank = %s WHERE id = %s;"
cursor.execute(UPDATE_SQL, (latest_rank, latest_id))
conn.commit()

# 등수 계산 함수
def get_ranked_game_info():
    query = """SELECT corr_cnt, exe_time, reg_date, 
               rank() over (order by corr_cnt DESC, exe_time ASC) AS irank 
               FROM wordgame"""
    cursor.execute(query)
    return cursor.fetchall()

# 등수 출력
ranked_info = get_ranked_game_info()
for row in ranked_info:
    print(row)