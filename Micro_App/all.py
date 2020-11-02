import bs4 #Importing BeautifulSoup4 package to read data from the webpage(To scrap the webpage)
import requests #Importing BeautifulSoup4 package to read data from the webpage(To scrap the webpage)
from urlmate import urlpass  #Importing urlpass module from urlvalidator package
import pandas as pd
from urllib.parse import urlparse #Importing urllib package to get the domain_name
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk




#Initialising all the necessary Variables, Lists and Dictionaries
valid_links = []
total_no = 0
title_names = []
storage_dict = {}
internal_links = []
external_links = []
meta_data = []



# An infinite loop to get the input link from user again n again untill the user enters the valid URL
while(True):
    print("\nPLEASE MENTION THE EXTENSION WHILE ENTERING THE URL, for eg : '.com' or '.in' \n")
    url_user = input("\nENTER THE URL HERE: ")

    check_url, response, proper_url = urlpass.isurl(url_user)

    if(check_url):
        break
    else:
        print("Please Try Again!\n")


#Using the urlpass.findhome() user-defined function to get the Home Page
home_page = urlpass.findhome(proper_url)
#Using the urlparse().netloc to get the domain name of the URL given by the user
domain_name = urlparse(proper_url).netloc


print(" \n=========================================================")
print(f"\n|| The Home Page is {home_page} ||\n")
print("=========================================================\n")

print("\n")

print(" \n=========================================================")
print(f"\n|| The Domain Name is {domain_name} ||\n")
print("=========================================================\n")



#Getting the content gathered by requests and storing it in Data
data = response.text
#Using BeautifulSoup to extract the data given my requests
soup = bs4.BeautifulSoup(data, "lxml")


#Looping through the <a> tag links found by BeautifulSoup and getting the Hyperlinks to other sites
for link in soup.find_all("a", href = True):
    check_link, proper_link = urlpass.check_url(link['href'])
    total_no += 1
    
    print(f"\nLINK NO: {total_no}")
    if check_link == True:
        valid_links.append(proper_link)
        print(f"\nLINK : {proper_link}")
        
        title = urlpass.title(proper_link)
        print(f"\nTITLE : {title}")
        
        print("\n")
        
    
    elif check_link == False:
        
        if proper_link[0] == '/':
            valid_links.append(home_page + proper_link)
            print(f"\nLINK : {home_page + proper_link}")

            title = urlpass.title(home_page + proper_link)
            print(f"\nTITLE : {title}")
            
            print("\n")
        
        else:
            pass

#Converting the List to set() to eliminate repeated links
valid_links_set = set(valid_links)
#Converting the valid_links back to list() to loop through it
valid_links = list(valid_links_set)

valid_no = len(valid_links)
invalid_no = total_no - valid_no



for link in valid_links:
    #Getting Title of all the valid Links
    title = urlpass.title(link)
    title_names.append(title)
    
    #Getting the 'CONTENT' for 'Name' as Description
    meta_value = soup.find('meta', attrs={'name':'og:description'}) or soup.find('meta', attrs={'property':'description'}) or soup.find('meta', attrs={'name':'description'})
    if meta_value:
        description = meta_value.get('content')
    else:
        description = 'N/A'
            
        meta_data.append(description)
        
    #Segregating the valid links into Internal and External links 
    if domain_name in link:
        internal_links.append(link)
    else:
        external_links.append(link)
         

print(f"\n ALL THE VALID LINKS IN {valid_links}\n")
print("\n\n############################################################################################\n\n".join(valid_links))


print(f"\n TILTLES OF ALL THE VALID LINKS IN {domain_name}\n")
print("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n".join(title_names))


print(f"\n ALL THE INTERNAL LINKS IN {internal_links}\n")
print("\n\n---------------------------------------------------------------------------------------------\n\n".join(internal_links))
print("\n \n")

print(f"\n ALL THE EXTERNAL LINKS IN {external_links}\n")
print("\n\n=============================================================================================\n\n".join(external_links))
print("\n \n")

print(f"\n ALL CONTENTS IN META DATA ARE {meta_data}\n")
print("\n\n=============================================================================================\n\n".join(external_links))
print("\n \n")


#Converting the valid_links and title_names into a disctionary in order to convert it into a DataFrame
for i in range(valid_no):
    storage_dict[i] = [valid_links[i], title_names[i]]


internal_num = len(internal_links)
external_num = len(external_links)



print(" \n===========================================")
print(f"\n|| Total Number of Links: {total_no} ||\n")
print("=========================================")


print(" \n============================================")
print(f"\n|| Total Number of Links: {valid_no} ||\n")
print("==========================================")


print(" \n=============================================")
print(f"\n|| Total Number of Links: {invalid_no} ||\n")
print("=============================================")


print(" \n======================================================")
print(f"\n|| Total Number of Internal Links is {internal_num} ||\n")
print("=======================================================")


print(" \n======================================================")
print(f"\n|| Total Number of External Links is {external_num} ||\n")
print("======================================================")

raw_text, text_len, unigrams_text, bigrams_text = urlpass.get_text_from_web(proper_url)

print(raw_text)
print(unigrams_text)
print(bigrams_text)

l_uni, l_bi = urlpass.frequency(unigrams_text, bigrams_text)

print(l_uni)
print(l_bi)

check_size, size_bytes, size_kb = urlpass.pagesize(proper_url)

print(f"The size of the page in KB is {size_bytes}Bytes")
print(f"The size of the page in KB is {size_kb:1.2f}KB")




