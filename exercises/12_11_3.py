'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.
'''

import urllib.request, urllib.parse, urllib.error

try:
    url = input('Enter a URL-->')
    fhand = urllib.request.urlopen(url)
except:
    print('Enter a valid URL')
    exit()

count = 0 
result = fhand.read(3000)
output = result.decode().strip('')
for char in output:
    count += 1

print(output)
print('\nThere is {} characters.\n'.format(count))    

