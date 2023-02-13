# import time

# # Fibonacci Recursive function
# def recursive_fibonacci(n):
#   if n <= 1:
#       return n
#   else:
#       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

# def printFibonacciNumbers(n):
#     n = int(n)
#     start = time.time()
#     # check if the number of terms is valid
#     if n <= 0:
#         print("Invalid input : Please input a positive value")
#     else:
#         print("Fibonacci series:")
#     for i in range(n):
#         print(recursive_fibonacci(i))

#     end = time.time()

#     print("The time of execution of above program is :",
#         (end-start) * 10**3, "ms")

# print("Enter the number of terms:")
# number = input()
# printFibonacciNumbers(number)

# Library for opening url and creating
# requests
import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd

from xlsxwriter import Workbook

# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    # making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    # reading contents of the website
    return f.read()


htmls = [   "https://tcktcktck.org/seoul/january-2016",
            "https://tcktcktck.org/seoul/february-2016",
            "https://tcktcktck.org/seoul/march-2016",
            "https://tcktcktck.org/seoul/april-2016",
            "https://tcktcktck.org/seoul/may-2016",
            "https://tcktcktck.org/seoul/june-2016",
            "https://tcktcktck.org/seoul/july-2016",
            "https://tcktcktck.org/seoul/august-2016",
            "https://tcktcktck.org/seoul/september-2016",
            "https://tcktcktck.org/seoul/october-2016",
            "https://tcktcktck.org/seoul/november-2016",
            "https://tcktcktck.org/seoul/december-2016"
            ]

frames = []

for html in htmls:
 
    # defining the html contents of a url
    xhtml = url_get_contents(html).decode('utf-8')
    
    # instantiating the html table parser object
    p = HTMLTableParser()

    # feeding the html contents in the
    # parser object
    p.feed(xhtml)

    # Now finally obtaining the data of
    # the table required
    table = p.tables[1]

    # converting the data in a pandas
    # dataframe for further processing
    df = pd.DataFrame(table)

    # print(df[1:])
    frames += [df]
    # printing the html contents of the url
    # print(df)

months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

with pd.ExcelWriter('2020.xlsx') as writer:
    for i in range(len(frames)):
        frames[i].to_excel(writer, sheet_name=f"{months[i]}")
