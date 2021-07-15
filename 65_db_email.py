import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Masukkan file : ')
if(len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for i in fh:
        # jika tidak dimulai dengan from: maka lewati
        if not i.startswith('From: '): continue
        # jika ada maka di split dan akan menjadi array
        pieces = i.split()
        # menangambil nilai index 1 yaitu nama emailnya
        email= pieces[1]
        # sintaks database mengecek apakah ada datanya di db sebelumnya
        cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
        # grab the first one
        row = cur.fetchone()
        # jika tidak ada data pada record maka akan menghasilkan none
        if row is None:
            # dan jika memang none jalankan berikut ini
            cur.execute('''INSERT INTO Counts (email, count)
                    VALUES (?, 1)''', (email,))
        else:
            # jika ada maka update data tersebut
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
        conn.commit()


sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for baris in cur.execute(sqlstr):
    print(str(baris[0]), baris[1])
cur.close()