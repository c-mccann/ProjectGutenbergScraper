from bs4 import BeautifulSoup
import requests
import re
import sched

'''

Want to download project gutenberg's entire library of texts, splitting them into plays, movies etc

supposed number of texts: 51020
http://www.gutenberg.org/w/captcha/question/Project Gutenberg offers 51020 free ebooks to download.


plays:
from oscar wilde, the importance of being earnest
line 14:    Title:  The Importance of Being Earnest
line 15:            A Trivial Comedy for Serious People
line 18:    Author: Oscar Wilde
line 47:    THE PERSONS IN THE PLAY

movies:




books:



poems:


'''

access_text_file = open("access_text_data.txt", 'r')
access_text = int(access_text_file.readline());
access_text_file.close()

i = 0
daily_limit = 10000 # need to find out

while i < daily_limit:
    print("Accessing text file:     " + str(access_text))
    gutenberg_file_directory = requests.get("http://www.gutenberg.org/files/" +
                                            str(access_text) + "/" + str(access_text) + ".txt")
    gutenberg_file_data = gutenberg_file_directory.text
    gutenberg_file_soup = BeautifulSoup(gutenberg_file_data, "lxml")

    # print(gutenberg_files_soup.text)

    a_tags = gutenberg_file_soup.find_all('p')
    pre_tags = gutenberg_file_soup.find_all('pre')
    complete_text = gutenberg_file_soup.get_text()
    if complete_text.__contains__("ERROR 403"):
        break

    text_name = 'placeholder'  # naming code from pre tags hopefully can be parsed easily
    media_type = "placeholder" # how to know where to save, e.g. plays movies poems etc

    if not int(complete_text.find("THE PERSONS IN THE PLAY")) == -1:
        media_type = "plays"



    lines_list = complete_text.splitlines()

    try:
        author_last = lines_list[17].split()[2].rstrip('\n')
        author_first = lines_list[17].split()[1][:1].rstrip('\n')
        title = lines_list[13][7:].rstrip('\n')
    except IndexError:
        author_first = "carl"
        author_last = "mccann"
        title = "The hungry caterpillar"

    text_name = title +". " + author_last + ", " + author_first
    if media_type.__eq__("plays"):
        f = open("Project Gutenberg Scrape/" + media_type + "/" + text_name + ".txt", 'w')
        f.write(complete_text)
        f.close()

    i += 1
    access_text += 1;


access_text_file = open("access_text_data.txt", 'w')
access_text_file.write(str(access_text))
access_text_file.close()


