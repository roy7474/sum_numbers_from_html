# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# http://py4e-data.dr-chuck.net/comments_42.html

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
import re

numbers = []
count=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.htmlinput'#('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() #urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
#tags = soup('')
#for tag in tags:
#    numbers += 1
    # Look at the parts of a tag
#    print('TAG:', tag)
#    print('URL:', tag.get('href', None))
#    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)
#print(numbers)
text = str(soup)
numbers_str = re.findall(r'\d+',text)
numbers = [int(num_str) for num_str in numbers_str]
total =  sum(numbers)
print(total)
print(numbers_str)




'''
for line in tags:
    text = line.get_text()
    count.extend(re.findall(r'\d+', text))
    #Extract the number from each of the lines using a regular expression and the findall() method
    x = re.findall('([0-9]+)', text)
    if len(x) > 0:                          #tracting only strings
        for val in x:
            val = int(val)                  #converting strings into intergers
            count.append(val)   
'''