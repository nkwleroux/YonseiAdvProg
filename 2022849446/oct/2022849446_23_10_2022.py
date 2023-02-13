import PyPDF2

def first_assignment(reader):
    count = 1
    
    pages_with_word = []
    
    for page in reader.pages:
        if("for" in page.extractText()):
            pages_with_word = pages_with_word + [reader.getPageNumber(page)]
            for word in page.extractText().split():
                if(word.lower() == "for"):
                    count = count + 1
                
    print("Number of pages:", pages_with_word)
    print("\"for\" appears in :", len(pages_with_word),"pages")              
    print("Number of times the word \"for\" appears in the document:", count)
    
def second_assignment(reader):
    text = reader.getPage(10).extractText()
    
    for word in text.split():
        if (word.find("stock") != -1):
            text = text.replace("stock", "HELLO")
        elif (word.find("a") != -1):
            text = text.replace(" a ", " NEW WORD ")    
        elif (word.find("The") != -1):
            text = text.replace("The", "NO need")
        else:
            pass
    
    print(text)

def homework(reader):
    print("Pdf pages amount:",len(reader.pages))
    
    email_addresss_yonsei = ["ysoia@yonsei.ac.kr","study@yonsei.ac.kr","sap@yonsei.ac.kr","abroad@yonsei.ac.kr","skghouse@yonsei.ac.kr"]
    email_addresss_avans = ["gsc@avans.nl","studyabroad@avans.nl","admission@adm.avans.nl","webmaster@avans.nl","onestop2@avans.nl"]
    email_addresss_barcelona = ["snuadmit@barcelona.es","snuoia@barcelona.es","snupr2@barcelona.es","sotongteam@barcelona.es","klp@barcelona.es"]
    email_addresss_stanford = ["songhy@stanford.edu", "hyunso@stanford.edu","jieun@stanford.edu", "jaysoo@stanford.edu","chewoo@stanford.edu"]
    email_addresss_beijing = ["circula2@bisu.edu.cs","libstacks@bisu.edu.cs","journals@bisu.edu.cs","infoserv@bisu.edu.cs","libacq2@bisu.edu.cs"]
    
    email_addresses = email_addresss_yonsei + email_addresss_avans + email_addresss_barcelona + email_addresss_stanford + email_addresss_beijing
    
    for email in email_addresses:
        if("yonsei.ac.kr" in email):
            print("Korea - Yonsei University: ", email)
        elif("avans.nl" in email):
            print("Netherlands - Avans University: ", email)
        elif("barcelona.es" in email):
            print("Spain - Barcelona University: ", email)
        elif("stanford.edu" in email):
            print("USA - Stanford University: ", email)
        elif("bisu.edu.cs" in email):
            print("China - Beijing University: ", email)
        else:
            pass

def main():
    print("Student id:", 2022849446)
    
    file = open('./python/2022849446/oct/midterm.pdf', 'rb')
    reader = PyPDF2.PdfFileReader(file)
    first_assignment(reader)
    second_assignment(reader)
    homework(reader)

if __name__ == "__main__":
    main()