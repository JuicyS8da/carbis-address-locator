import sqlite3

connection = sqlite3.connect('settings.db')
cursor = connection.cursor()

def set_db():
    #creates a database for settings
    global cursor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Settings (
    id INTEGER PRIMARY KEY,
    language TEXT NOT NULL,
    api TEXT,
    secret_key TEXT,
    count INTEGER
    )
    ''')
    
    user_check = cursor.execute('SELECT * FROM Settings WHERE id = ?', (1, )).fetchone()
    if user_check is None: 
        cursor.execute('INSERT INTO Settings (language, api, secret_key, count) VALUES (?, ?, ?, ?)', ('ru', None, None, 10))
    else:
        return 0

#CHANGE
def change_api(api):
    global cursor       
    cursor.execute('UPDATE Settings SET api = ? WHERE id = ?', (api, 1))

def change_lang(lang):
    global cursor
    cursor.execute('UPDATE Settings SET language = ? WHERE id = ?', (lang, 1))

def change_secret_key(key):
    global cursor
    cursor.execute('UPDATE Settings SET secret_key = ? WHERE id = ?', (key, 1))

def change_count(count):
    global cursor
    cursor.execute('UPDATE Settings SET count = ? WHERE id = ?', (count, 1))

#GET
def get_api():
    global cursor
    db_data = cursor.execute('SELECT * FROM Settings WHERE id = ?', (1, )).fetchone()
    return db_data[2]

def get_lang():
    global cursor
    db_data = cursor.execute('SELECT * FROM Settings WHERE id = ?', (1, )).fetchone()
    return db_data[1]

def get_secret_key():
    global cursor
    db_data = cursor.execute('SELECT * FROM Settings WHERE id = ?', (1, )).fetchone()
    return db_data[3]

def get_count():
    global cursor
    db_data = cursor.execute('SELECT * FROM Settings WHERE id = ?', (1, )).fetchone()
    return db_data[4]

#DELETE
def del_api():
    global cursor
    cursor.execute('UPDATE Settings SET api = ? WHERE id = ?', (None, 1))
    
def del_secret_key():
    global cursor
    cursor.execute('UPDATE Settings SET secret_key = ? WHERE id = ?', (None, 1))

connection.commit()
