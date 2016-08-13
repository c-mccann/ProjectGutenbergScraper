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
    # gutenberg_file_directory = requests.get("http://www.gutenberg.org/files/" +
    #                                       str(access_text) + "/" + str(access_text) + ".txt")
    # gutenberg_file_data = gutenberg_file_directory.text
    # gutenberg_file_soup = BeautifulSoup(gutenberg_file_data, "lxml")

    # print(gutenberg_files_soup.text)

    # a_tags = gutenberg_file_soup.find_all('p')
    # pre_tags = gutenberg_file_soup.find_all('pre')
    complete_text = open('/Volumes/Data/Users/carlmccann2/IdeaProjects/The Shape of Tales to Come/src/res/Plays/The Importance of Being Earnest. Wilde, O.txt','r')
    text_name = 'placeholder'  # naming code from pre tags hopefully can be parsed easily
    media_type = "placeholder" # how to know where to save, e.g. plays movies poems etc

    #print(complete_text)
    # for line in complete_text:
    #     print(line)


    lines_list = []
    for line in complete_text:
        lines_list.append(line)
        if line.find("THE PERSONS IN THE PLAY") == -1:
            media_type = "plays"

    author_last = lines_list[17].split()[2].rstrip('\n')
    print(author_last)
    author_first = lines_list[17].split()[1][:1].rstrip('\n')
    print(author_first)
    title = lines_list[13][7:].rstrip('\n')
    print(title)
    text_name = title +". " + author_last + ", " + author_first

    print("Project Gutenberg Scrape/" + media_type + "/" + text_name + ".txt")
    f = open("Project Gutenberg Scrape/" + media_type + "/" + text_name + ".txt", 'w')
    for line in lines_list:
        f.write(line)
    f.close()

   # print(a_tags)
    x = input("Continue [Y/n]:  ")

    i += 1
    access_text += i;


access_text_file = open("access_text_data.txt", 'w')
access_text_file.write(str(access_text))
access_text_file.close()


