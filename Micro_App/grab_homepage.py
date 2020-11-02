import bs4 #Importing BeautifulSoup4 package to read data from the webpage(To scrap the webpage)
import requests #Importing requests which allows to send HTTP requests to websites
from urlvalidator import urlpass #Importing urlpass module from urlvalidator package


while(True):
    print("PLEASE MENTION THE EXTENSION WHILE ENTERING THE URL, for eg : '.com' or '.in' ")
    url = input("ENTER THE URL HERE: ")
    v, res = urlpass.isurl(url)
    if(v):
        break
    else:
        print("Please Try Again!")

