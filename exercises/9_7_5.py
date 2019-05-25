fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('There is no file named as', fname)
    exit()

counts = dict()
for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1

print(counts)