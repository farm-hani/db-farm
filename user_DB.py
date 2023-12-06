import sqlite3

# SQLite 연결 및 테이블 생성
def create_table():
    conn = sqlite3.connect('user_data.sqlite')
    cursor = conn.cursor()

    # 사용자 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            location TEXT
        )
    ''')

    # 농작물 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crops (
            crops_id INTEGER PRIMARY KEY AUTOINCREMENT,
            crops_name TEXT,
            season TEXT
        )
    ''')

    # 사용자-농작물 관계 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_crops (
            crops_id INTEGER,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(crops_id) REFERENCES crops(crops_id),
            PRIMARY KEY (user_id, crops_id)
        )
    ''')

    conn.commit()
    conn.close()

# 사용자 정보 저장
def save_user(name, location):
    conn = sqlite3.connect('user_data.sqlite')
    cursor = conn.cursor()

    # 사용자 정보 저장
    cursor.execute('INSERT INTO users (user_name, location) VALUES (?, ?)', (name, location))

    conn.commit()
    conn.close()

# 사용자 정보 불러오기
def get_user_location(name):
    conn = sqlite3.connect('user_data.sqlite')  # 데이터베이스 파일 이름 수정
    cursor = conn.cursor()

    # 사용자 이름으로 위치 정보 조회
    cursor.execute('SELECT location FROM users WHERE user_name = ?', (name,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return None
    
# 농작물 정보 저장
def save_crops(crops_name, season):
    conn = sqlite3.connect('user_data.sqlite')  # 데이터베이스 파일 이름 수정
    cursor = conn.cursor()

    # 농작물 정보 저장
    cursor.execute('INSERT INTO crops (crops_name, season) VALUES (?, ?)', (crops_name, season, ))

    conn.commit()
    conn.close()

# 관계 정보 저장
def save_user_crops(crops_id, user_id):
    conn = sqlite3.connect('user_data.sqlite')  # 데이터베이스 파일 이름 수정
    cursor = conn.cursor()

    cursor.execute('INSERT INTO user_crops (crops_id, user_id) VALUES (?, ?)', (crops_id, user_id,))

    conn.commit()
    conn.close()

# 사용자 재배 작물 갖고 오기
def get_user_crops(name):
    conn = sqlite3.connect('user_data.sqlite')  # 데이터베이스 파일 이름 수정
    cursor = conn.cursor()

    # 사용자 이름으로 재배 작물 갖고 오기
    cursor.execute(
        'SELECT crops.crops_name FROM users, crops, user_crops WHERE user_name = ? and users.user_id = user_crops.user_id and crops.crops_id = user_crops.crops_id', (name,))  # 쿼리 수정
    result = cursor.fetchall()

    conn.close()

    if result:
        return [row[0] for row in result]
    else:
        return None
    
def get_user_id(name):
    conn = sqlite3.connect('user_data.sqlite')  # 데이터베이스 파일 이름 수정
    cursor = conn.cursor()

    # 사용자 이름 - user_id 갖고 오기
    cursor.execute(
        'SELECT user_id FROM users WHERE user_name = ?', (name,))  # 쿼리 수정
    result = cursor.fetchall()

    conn.close()

    if result:
        return result[0][0]
    else:
        return None
    
def get_crops_id(name):
    conn = sqlite3.connect('user_data.sqlite')  # 데이터베이스 파일 이름 수정
    cursor = conn.cursor()

    # 사용자 이름 - user_id 갖고 오기
    cursor.execute(
        'SELECT crops_id FROM crops WHERE crops_name = ?', (name,))  # 쿼리 수정
    result = cursor.fetchall()

    conn.close()

    if result:
        return result[0][0]
    else:
        return None
