import bs4
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk

cachedStopWords = stopwords.words("english")

def get_text_from_web(url):
    text = "Hello"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, "lxml")

    for script in soup(["script", "style"]):
        script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())


        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))


        # drop blank lines
        raw_text = '\n'.join(chunk for chunk in chunks if chunk)

        #Removing all the punctuations using regex
        punct_removed_text = re.sub(r'[^\w\s]', '', raw_text)

        #Tokenizing the punctuation removed text from regex uisng "word_tokenize"
        text_tokens = word_tokenize(punct_removed_text)

        #Removing all the Stop Words from the punctuation removed text
        tokens_without_sw = [word for word in text_tokens if (word not in cachedStopWords)]

        unigrams_text = tokens_without_sw

        #Getting all the bigrams from the unigrams genrated above using nltk.bigrams()
        bigrams_text = list(nltk.bigrams(" ".join(unigrams_text).split()))

    return raw_text, len(raw_text), unigrams_text, bigrams_text


#################################################___________________#####################################################



def title(link):
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text,"lxml")
    if(len(soup.select("title")) == 0):
        return "N/A"
    else:
        title = soup.select("title")[0].text
        return title



#################################################___________________#####################################################




# check_url() method just checks if a URL is valid without appending '/' or concatenating 'http://' or 'www.'
def check_url(url):
    try:
        res = requests.get(url)
        return True, url
    except:
        return False, url


 #################################################___________________#####################################################


#Supporting method for isurl() method to execute a set of repeating block of code
def test(url):
    res = 0
    try:
        res = requests.get(url)
        print("URL is VALID! Proceeding Further....")
        print("\n \n")
        return True, res, url
                
    except:
        print("INVALID URL!")
        print("\n \n")
        return False, res, url



#################################################___________________#####################################################



# The isurl() method is used to find if the URL entered by the user is valid or nor ?
def isurl(url):
    res = 0
    if(("https://" in url) or ("https://" in url)):
        url = url + '/'
        v, res, url1 = test(url)
        return v, res, url1
            
    else:
        if("www." in url):
            url = "http://" + url + '/'
            v, res, url1 = test(url)
            return v,res, url1

        else:
            url = "http://www." + url +'/'
            v, res, url1 = test(url)
            return v, res, url1

            

#################################################___________________#####################################################


# The findhome() method is used to find the Home Page of the Link given by the user
def findhome(url):
    c  = 0
    for i in range(len(url)):
        if url[i] == "/":
            c+=1
        if c == 3:
            home = url[0:i:1] + '/'
            return home
            break