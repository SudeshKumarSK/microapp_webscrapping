#Importing all the necessary packages and modules for Web Scrapping

import bs4 #Importing BeautifulSoup4 package to read data from the webpage(To scrap the webpage)
import requests #Importing BeautifulSoup4 package to read data from the webpage(To scrap the webpage)
from urlmate import urlpass  #Importing urlpass module from urlvalidator package
import pandas as pd #Importing Pandas to create dataframe from a dictionary and convert it into .csv
from urllib.parse import urlparse #Importing urllib package to get the domain_name
from nltk.corpus import stopwords #To get the stop words
from nltk.tokenize import word_tokenize #To Tokenize a string of words or content from web
import re #Importing regex to remove punctuations
import nltk #Importing nltk for ngram operations
from IPython.display import clear_output #importing this module to clear the output

cachedStopWords = stopwords.words("english")


print(" \n====================================================================")
print(f"\n||SUCCESSFULLY IMPORTED ALL THE NECESSARY MODULES AND PACKAGES||\n")
print("====================================================================\n")


#Initialising all the necessary Variables, Lists and Dictionaries
size_kb_links = []
valid_links = []
total_no = 0
title_names = []
storage_dict = {}
internal_links = []
external_links = []
meta_data_links = []
meta_data_home = []
unigram_lst = []
bigram_lst = []



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


with open("/Users/sk/Desktop/Challenge/Home/Home_Page.txt", mode = "w") as home:
    home.write(f" \n=========================================================\n|| The Home Page is {home_page} ||\n=========================================================\n")
    home.write(f" \n=========================================================\n|| The Domain Name is {domain_name} ||\n=========================================================\n")



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

        
print(" \n=========================================================================")
print(f"\n|| SUCCESSFULLY GENERATED ALL THE POSSIBLE LINKS AND THEIR TITLES!! ||\n")
print("======================================================================\n")


#Getting the Meta Data for Home Page

meta_data_home = []
meta_data_home = urlpass.meta_find(proper_url)


#Converting the List to set() to eliminate repeated links
valid_links_set = set(valid_links)


#Converting the valid_links back to list() to loop through it
valid_links = list(valid_links_set)


#Getting the number of valid links
valid_no = len(valid_links)

#Getting the number of invalid links
invalid_no = total_no - valid_no



#Collecting the details like Titles, Internal or External Links

#Declaring bools to check if a link is Internal or External which will be used in dataFrame
internal_bool = []
external_bool = []


for link in valid_links:
    print(f"\n Getting Title and Internal & External Links of {link}")
    
    #Getting Title of all the valid Links
    title = urlpass.title(link)
    title_names.append(title)
    
    
    #Segregating the valid links into Internal and External links 
    if domain_name in link:
        internal_links.append(link)
        internal_bool.append("True")
        external_bool.append("False")
        
        
    else:
        external_links.append(link)
        internal_bool.append("False")
        external_bool.append("True")
    
    #Clearing the output after each iteration to improve the readability
    clear_output(wait=True)
    
print(" \n=========================================================================")
print(f"\n|| SUCCESSFULLY COLLECTED ALL THE NECESSARY DETAILS!! ||\n")
print("======================================================================\n")



#Writing the valid links into the "Valid_Links.txt" file in the "Home" Directory

with open("/Users/sk/Desktop/Challenge/Home/Valid_Links.txt", mode = "w") as val:
    val.write(f"ALL THE VALID LINKS IN {domain_name}\n")
    for link in valid_links:
        val.write(f"\n\n{link}\n\n#########################################################################################\n\n")
        
        

#Writing the Titles into the "Titles.txt" file in the "Home" Directory

with open("/Users/sk/Desktop/Challenge/Home/Titles.txt", mode = "w") as val:
    val.write(f"ALL THE TITLE OF THE VALID LINKS IN {domain_name}\n")
    for link in title_names:
        val.write(f"\n\n{link}\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
        
        

#Writing the Internal Links into the "Internal_links.txt" file in the "Home" Directory

with open("/Users/sk/Desktop/Challenge/Home/Internal_links.txt", mode = "w") as val:
    val.write(f"THE INTERNAL LINKS IN THE VALID LINKS IN {domain_name}")
    for link in internal_links:
        val.write(f"\n\n{link}\n\n------------------------------------------------------------------------------------------\n\n")
        

#Writing the External Links into the "External_links.txt" file in the "Home" Directory


with open("/Users/sk/Desktop/Challenge/Home/External_links.txt", mode = "w") as val:
    val.write(f"THE EXTERNAL LINKS IN THE VALID LINKS IN {domain_name}")
    for link in external_links:
        val.write(f"\n\n{link}\n\n==========================================================================================\n\n")
        
        
#Writing the Meta Data in the Home Page into the "Meta_Data.txt"  in the "Home" Directory

with open("/Users/sk/Desktop/Challenge/Home/Meta_Data.txt", mode = "w") as val:
    val.write(f"THE META DATA IN THE VALID LINKS IN {domain_name}")
    for link in meta_data_home:
        val.write(f"\n\n{link}\n\n==========================================================================================\n\n")

#Getting the number of Internal Links and External Links


internal_num = len(internal_links)
external_num = len(external_links)

print(" \n=========================================")
print(f"\n|| Total Number of Links: {total_no} ||\n")
print("=========================================")


print(" \n=========================================")
print(f"\n|| Total Number of Valid Links: {valid_no} ||\n")
print("=========================================")


print(" \n=========================================")
print(f"\n|| Total Number of Invalid Links: {invalid_no} ||\n")
print("=========================================")


print(" \n=========================================")
print(f"\n|| Total Number of Internal Links is {internal_num} ||\n")
print("=========================================")


print(" \n==========================================")
print(f"\n|| Total Number of External Links is {external_num} ||\n")
print("==========================================")


with open(f"/Users/sk/Desktop/Challenge/Numbers/Number_links.txt", mode = "w") as val:
        val.write(f"\nTOTAL NUMBER OF LINKS IN {proper_url}\n\n")
        val.write(f"\n\n{total_no}\n\n----------------------------\n\n")
        
        
with open(f"/Users/sk/Desktop/Challenge/Numbers/Number_links.txt", mode = "a") as val:
        val.write(f"\nTOTAL NUMBER OF VALID LINKS IN {proper_url}\n\n")
        val.write(f"\n\n{valid_no}\n\n----------------------------\n\n")


with open(f"/Users/sk/Desktop/Challenge/Numbers/Number_links.txt", mode = "a") as val:
        val.write(f"\nTOTAL NUMBER OF INVALID LINKS IN {proper_url}\n\n")
        val.write(f"\n\n{invalid_no}\n\n----------------------------\n\n")


        
with open(f"/Users/sk/Desktop/Challenge/Numbers/Number_links.txt", mode = "a") as val:
        val.write(f"\nTOTAL NUMBER OF INTERNAL LINKS IN {proper_url}\n\n")
        val.write(f"\n\n{internal_num}\n\n----------------------------\n\n")


        
with open(f"/Users/sk/Desktop/Challenge/Numbers/Number_links.txt", mode = "a") as val:
        val.write(f"\nTOTAL NUMBER OF EXTERNAL LINKS IN {proper_url}\n\n")
        val.write(f"\n\n{external_num}\n\n----------------------------\n\n")



z = 1
top20_uni = []
top20_bi = []
#Iterating through the valid links

for link in valid_links:
    
    print(f"\n Getting Raw Data, Unigrams and Bigrams from {link}")
    
    
    #Getting the raw_text, unigrams and bigrams from the valid links
    raw_text, text_len, unigrams_text_links, bigrams_text_links = urlpass.get_text_from_web(link)
    
    unigram_lst.append(unigrams_text_links)
    bigram_lst.append(bigrams_text_links)
    
    #Getting the Meta Data for every valid link
    meta_data_links = urlpass.meta_find(link)
    
    #Writing the Raw Data of the links 

    with open(f"/Users/sk/Desktop/Challenge/Raw_Data/{z}_Data.txt", mode = "w") as val:
        val.write(f"THE RAW DATA IN THE LINK, {link}")
        for x in raw_text:
            val.write(f"\n\n{x}\n\n----------------------------\n\n")
    
    #Writing the Meta data of the links 
    
    with open(f"/Users/sk/Desktop/Challenge/Meta_Data/{z}_Meta_Data.txt", mode = "w") as val:
        val.write(f"THE META DATA IN THE LINK, {link}")
        for x in meta_data_links:
            val.write(f"\n\n{x}\n\n----------------------------\n\n")
            
    #Writing the Unigrams of the links 
    
    with open(f"/Users/sk/Desktop/Challenge/Unigrams/{z}_Unigrams.txt", mode = "w") as val:
        val.write(f"THE UNIGRAMS IN THE LINK, {link}")
        for x in unigrams_text_links:
            val.write(f"\n\n{x}\n\n-----------------------------\n\n")
            
    #Writing the Bigrams of the links 
    
    with open(f"/Users/sk/Desktop/Challenge/Bigrams/{z}_Bigrams.txt", mode = "w") as val:
        val.write(f"THE BIGRAMS IN THE LINK, {link}")
        for x in bigrams_text_links:
            val.write(f"\n\n{x}\n\n-----------------------------\n\n")
    
    
    #Getting the top 20 frequent unigrams and bigrams
    
    l_uni_links, l_bi_links = urlpass.frequency(unigrams_text_links, bigrams_text_links)
    
    top20_uni.append(l_uni_links)
    top20_bi.append(l_bi_links)
    
    
    #Writing the Top 20 Unigrams of the links 
    
    with open(f"/Users/sk/Desktop/Challenge/Top20Unigrams/{z}_Top20Unigrams=.txt", mode = "w") as val:
        val.write(f"THE TOP 20 UNIGRAMS IN DESCENDING ORDER, {link}")
        for x in l_uni_links:
            val.write(f"\n\n{x}\n\n=====================================\n\n")
            
    #Writing the Top 20 Bigrams of the links
    
    with open(f"/Users/sk/Desktop/Challenge/Top20Bigrams/{z}_Top20Bigrams.txt", mode = "w") as val:
        val.write(f"THE TOP 20 BIGRAMS IN DESCENDING ORDER, {link}")
        for x in l_bi_links:
            val.write(f"\n\n{x}\n\n=====================================\n\n")
    z+=1


#Repeating the same process for the Home Page

raw_text, text_len, unigrams_text_home, bigrams_text_home = urlpass.get_text_from_web(proper_url)
    
with open(f"/Users/sk/Desktop/Challenge/Home/Home_Data.txt", mode = "w") as val:
    val.write(f"THE RAW DATA IN THE LINK, {proper_url}")
    for x in raw_text:
        val.write(f"\n\n{x}\n\n----------------------------\n\n")
            
    
with open(f"/Users/sk/Desktop/Challenge/Home/Home_Unigrams.txt", mode = "w") as val:
    val.write(f"THE UNIGRAMS IN THE LINK, {proper_url}")
    for x in unigrams_text_home:
        val.write(f"\n\n{x}\n\n-----------------------------\n\n")
            
    
with open(f"/Users/sk/Desktop/Challenge/Home/Home_Bigrams.txt", mode = "w") as val:
    val.write(f"THE BIGRAMS IN THE LINK, {proper_url}")
    for x in bigrams_text_home:
        val.write(f"\n\n{x}\n\n-----------------------------\n\n")
    
    
l_uni_home, l_bi_home = urlpass.frequency(unigrams_text_home, bigrams_text_home)
    
    
with open(f"/Users/sk/Desktop/Challenge/Home/Home_Top20Unigrams=.txt", mode = "w") as val:
    val.write(f"THE TOP 20 UNIGRAMS IN DESCENDING ORDER, {proper_url}")
    for x in l_uni_home:
        val.write(f"\n\n{x}\n\n=====================================\n\n")
            
            
with open(f"/Users/sk/Desktop/Challenge/Home/Home_Top20Bigrams.txt", mode = "w") as val:
    val.write(f"THE TOP 20 BIGRAMS IN DESCENDING ORDER, {proper_url}")
    for x in l_bi_home:
        val.write(f"\n\n{x}\n\n=====================================\n\n")
        
        

#Getting the size of the home page using urlpass.pagesize() in urlmate
check_size, size_bytes, size_kb = urlpass.pagesize(proper_url)

with open("/Users/sk/Desktop/Challenge/Size/File_Size.txt", mode = "w") as val:
    val.write(f" \n==========================================================================================\n||The size of {proper_url} in Bytes is {size_bytes} Bytes ||\n==========================================================================================\n")
    val.write(f" \n==========================================================================================\n||The size of {proper_url}in KB is {size_kb:1.2f} KB's ||\n==========================================================================================\n")
    



#Getting the size of all the valid links using urlpass.pagesize() in urlmate

size_kb_links = []

for link in valid_links:
    
    check_size, size_bytes, size_kb = urlpass.pagesize(link)
    size_kb_links.append(round(size_kb, 2))
    
    with open("/Users/sk/Desktop/Challenge/Size/File_Size.txt", mode = "a") as val:
        val.write(f" \n==========================================================================================\n||The size of {link} in Bytes is {size_bytes} Bytes ||\n=========================================================================================\n")
        val.write(f" \n==========================================================================================\n||The size of {link}in KB is {size_kb:1.2f} KB's ||\n===========================================================================================\n")
              

#Iterating through valid_no and creating a dictionary to convert into dataFrame
for i in range(valid_no):
    
    storage_dict[i] = [valid_links[i], title_names[i], internal_bool[i], external_bool[i], top20_uni[i], top20_bi[i], size_kb_links[i]] 

#Creating the dataFrame using pandas
storage_df = pd.DataFrame.from_dict(storage_dict, orient='index', columns=['VALID LINKS','TITLE NAMES','INTERNAL LINK','EXTERNAL LINK', 'TOP20 UNI', 'TOP20 BI', 'WEB PAGE SIZE (KB)'])

#Convert the dataframe into csv file#
storage_df.to_csv("/Users/sk/Desktop/Challenge/CSV/Exeter_Data.csv")