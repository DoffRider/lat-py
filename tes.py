fname = input('Masukkan file : ')
if(len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for i in fh:
    if not i.startswith('From: '): continue
    pieces = i.split()
    email= pieces[1]
    print(email)
