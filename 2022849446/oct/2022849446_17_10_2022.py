import csv

print("Student id:", 2022849446)

def readCSVFile(fileName):
    with open(fileName, 'r',newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rank = reader.__next__()
        university = reader.__next__()
        location = reader.__next__()
        score = reader.__next__()
        
        return rank, university, location, score
    
def getHeaderName(listOfValues):
    return listOfValues.pop(0)

def getListOfValues(listOfValues):
    return listOfValues[0:]

def printList(lsit):
    header = getHeaderName(lsit)
    values = getListOfValues(lsit)
    print(header, values)
    
def printStats(l, r, s):
    print("Stats for the university -", "Location:", l, ",Rank:", r, ",Score:", s)

def main():
    rank, university, location, score = readCSVFile('./python/2022849446/oct/University_rankings.csv')    
    
    rank = [eval(i) for i in rank[1:]]
    score = [eval(i) for i in score[1:]]

    for(r, u, l, s) in zip(rank, university, location, score):
        if(min(rank) == r):
            print("University with the highest rank:", u)
            printStats(l, r, s)
            
        if(max(rank)== r):
            print("University with the lowest rank:", u)
            printStats(l, r, s)
            
        print(u[0:len(u)])
    
if __name__ == "__main__":
    main()

