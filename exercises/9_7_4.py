"""
# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

"""

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

largest = None
for key, value in counts.items():
    if largest is None or value > largest:
        largest = value
        sender = key

print(sender, largest)
