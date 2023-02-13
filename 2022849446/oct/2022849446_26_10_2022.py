import PyPDF2


def emails():
    email_addresss_yonsei = ["ysoia@yonsei.ac.kr", "study@yonsei.ac.kr",
                             "sap@yonsei.ac.kr", "abroad@yonsei.ac.kr", "skghouse@yonsei.ac.kr"]
    email_addresss_avans = ["gsc@avans.nl", "studyabroad@avans.nl",
                            "admission@adm.avans.nl", "webmaster@avans.nl", "onestop2@avans.nl"]
    email_addresss_barcelona = ["snuadmit@barcelona.es", "snuoia@barcelona.es",
                                "snupr2@barcelona.es", "sotongteam@barcelona.es", "klp@barcelona.es"]
    email_addresss_stanford = ["songhy@stanford.edu", "hyunso@stanford.edu",
                               "jieun@stanford.edu", "jaysoo@stanford.edu", "chewoo@stanford.edu"]
    email_addresss_beijing = ["circula2@bisu.edu.cs", "libstacks@bisu.edu.cs",
                              "journals@bisu.edu.cs", "infoserv@bisu.edu.cs", "libacq2@bisu.edu.cs"]

    return email_addresss_yonsei + email_addresss_avans + email_addresss_barcelona + email_addresss_stanford + email_addresss_beijing


def email_contacts(contact):
    switch = {
        emails()[0]: "ysoia",
        emails()[1]: "study",
        emails()[2]: "sap",
        emails()[3]: "abroad",
        emails()[4]: "skghouse",
        emails()[5]: "gsc",
        emails()[6]: "studyabroad",
        emails()[7]: "admission",
        emails()[8]: "webmaster",
        emails()[9]: "onestop2",
        emails()[10]: "snuadmit",
        emails()[11]: "snuoia",
        emails()[12]: "snupr2",
        emails()[13]: "sotongteam",
        emails()[14]: "klp",
        emails()[15]: "songhy",
        emails()[16]: "hyunso",
        emails()[17]: "jieun",
        emails()[18]: "jaysoo",
        emails()[19]: "chewoo",
        emails()[20]: "circula2",
        emails()[21]: "libstacks",
        emails()[22]: "journals",
        emails()[23]: "infoserv",
        emails()[24]: "libacq2",
    }
    return switch.get(contact, "Error: Contact does not exist")


def email_funcitons():
    email_addresses = emails()
    email_addresses_new = email_addresses.copy()

    # Replace with new email
    for i in range(len(email_addresses)):
        if (i % 2 == 0):
            email_addresses_new[i] = "New email address"
    email_addresses += email_addresses_new

    print("Replace with new email", email_addresses, "\n")

    # slice command example
    print("Slice command exmample 10-50", email_addresses[10:], "\n")
    print("Slice command example 0-25", email_addresses[:25], "\n")

    # replace with slice
    email_addresses[44:] = ["REPLACE WITH SLICE"] * len(email_addresses[44:])
    print("Replace with slice command", email_addresses, "\n")

    # append
    email_addresses.append("APPEND")
    print("Append example", email_addresses, "\n")

    # extend
    other_email_addresses = ["EXTEND1", "EXTEND2", "EXTEND3"]
    email_addresses.extend(other_email_addresses)
    print("Extend example", email_addresses, "\n")

    # sort
    email_addresses.sort()
    print("Sort example", email_addresses, "\n")

    # pop
    email_addresses.pop(10)
    print("Pop example", email_addresses, "\n")

    # remove
    email_addresses.remove("EXTEND1")
    print("Remove example", email_addresses, "\n")

    # del
    del (email_addresses[0])
    print("Del example", email_addresses, "\n")


def email_print():
    print("Email example \n")
    email_addresses = emails()
    for mail in email_addresses:

        print("BCC", mail)
        print("Subject: [Study Abroad] Application for exchange program")
        # print("Dear", mail.partition("@")[0], ",")
        print("Dear", email_contacts(mail), ",\n")


def pdf():
    # open pdf
    file = open('./python/2022849446/oct/midterm.pdf', 'rb')

    # read pdf
    reader = PyPDF2.PdfFileReader(file)

    # split pdf
    reader.getPage(10).extract_text()

    # split each word
    words = []
    for word in reader.getPage(10).extract_text().split():
        words += [word]
    print("Split words example", words, "\n")

    # count each word
    count = len(reader.getPage(10).extract_text().split())
    print("Count total amount of words", count, "\n")

    # split each word
    words_split = []
    for word in reader.getPage(10).extract_text().split():
        words_split += [list(word)]

    print("Letter split example", words_split, "\n")


def main():
    print("Student id:", 2022849446)
    email_funcitons()
    email_print()
    pdf()


if __name__ == "__main__":
    main()
