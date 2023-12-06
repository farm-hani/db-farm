import sqlite3
from datetime import datetime

# SQLite 연결 및 테이블 생성
def create_table():
    conn = sqlite3.connect('user_data.sqlite')
    cursor = conn.cursor()

    # 사용자 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT
        )
    ''')

    conn.commit()
    conn.close()

# 사용자 정보 저장
def save_user(name, location):
    conn = sqlite3.connect('user_data.sqlite')
    cursor = conn.cursor()

    # 사용자 정보 저장
    cursor.execute('INSERT INTO users (name, location) VALUES (?, ?)', (name, location))

    conn.commit()
    conn.close()

# 사용자 정보 불러오기
def get_user_location(name):
    conn = sqlite3.connect('user_data.sqlite')
    cursor = conn.cursor()

    # 사용자 이름으로 위치 정보 조회
    cursor.execute('SELECT location FROM users WHERE name = ?', (name,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return None
