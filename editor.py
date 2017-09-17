#Profanity Editor
#This Program detects Curse word from your text file.
#To detect curse word
#use wdly.com to detect this
#e.g:- http://www.wdly.com/profanity?q=shit return true

import urlib
def read_text():
    #use your own file path
    quotes = open("home/ved/hello.txt")
    contents_of_file = quotes.read()

    print(contents_of_file)
    quotes.close()
    check(contents_of_file)

def check(text_to_check):
    connection = urlib.urlopen(http://www.wdly.com/profanity?q=+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
read_text()
