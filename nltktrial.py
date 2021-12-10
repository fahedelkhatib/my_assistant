import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import functions as fn

print("fetching website data")
fn.speak("give me a website link!")
userInput = input("give me a website link!\n")

print("fetching")
fn.speak("fetching")
response =  urllib.request.urlopen(userInput)
html = response.read()

print("tokenizing")
fn.speak("tokenizing")
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
tokens = [t for t in text.split()]

print("processing")
fn.speak("processing")
englishLanguage = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in englishLanguage:
        clean_tokens.remove(token)

print("displaying word frequency graph")
fn.speak("displaying word frequency graph")
freq = nltk.FreqDist(clean_tokens)

freq.plot(30,cumulative = False)

fn.speak("deez nuts")