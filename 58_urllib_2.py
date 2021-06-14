import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

hit = dict()
for i in fhand:
    kata = i.decode().split()
    for ii in kata:
        hit[ii] = hit.get(ii,0)+1
print(hit)