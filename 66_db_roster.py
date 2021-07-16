import json
from os import curdir
import sqlite3

koneksi = sqlite3.connect('rosterdb.sqlite')
kursor = koneksi.cursor()

#setup
kursor.executescript('''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

nama_file = input('Masukkan nama file = ')
if len(nama_file) < 1:
    nama_file = 'roster_data_sample.json'

str_data = open(nama_file).read()
json_data = json.loads(str_data)

for i in json_data:

    nama = i[0]
    title = i[1]

    print((nama,title))

    kursor.execute('''INSERT OR IGNORE INTO User(name)
            VALUES(?)''',(nama,))
    kursor.execute('SELECT id FROM User Where name = ?',(nama,))
    user_id = kursor.fetchone()[0]
    # 
    kursor.execute('''INSERT OR IGNORE INTO Course(title)
            VALUES(?)''',(title,))
    kursor.execute('SELECT id FROM Course Where title = ?',(title,))
    course_id = kursor.fetchone()[0]
    # 
    kursor.execute('''INSERT OR REPLACE INTO Member(user_id, course_id)
            VALUES(?,?)''',(user_id,course_id))
    

    koneksi.commit()