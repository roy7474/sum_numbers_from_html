# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_1793480.html

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
try: 
   url = input('Please enter the URL of the website: ')
   html = urllib.request.urlopen(url, context=ctx).read() #urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, "html.parser")
   text = str(soup)
   numbers_str = re.findall(r'>(\d+)',text)
   numbers = [int(num_str) for num_str in numbers_str]
   total =  sum(numbers)
   print('The intergers found in this website were:', numbers_str)
   print('The sum of those numbers is:', total)

except:
   print('There was a problem while trying to open the website you enter. Please try again!')
   exit()
