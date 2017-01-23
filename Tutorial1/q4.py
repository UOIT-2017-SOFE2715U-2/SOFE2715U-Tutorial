#initially created by Matthew Rabski before creating GitHub repoitory

f = open('input.txt', 'r')
ta = 'teaching assistant'
for line in f:
    if ta in line:
        line = line.replace(ta, ta + ' is awesome')
        print line
    else: print line
f.close()
