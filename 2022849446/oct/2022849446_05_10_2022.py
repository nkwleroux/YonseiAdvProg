import os.path 
import random
import csv

print("Student id:", 2022849446)

file_exists = os.path.exists("./python/2022849446/oct/results.csv")    
if(file_exists == False):
    uniformDistribution = [random.uniform(0,2) for i in range(10)]
    print("Uniform distribution: ", uniformDistribution)

    triangularDistributuion = [random.triangular(0,1,0.5) for i in range(10)]
    print("\nTriangular distributuion: ",triangularDistributuion)

    doubleTriangularDistributuion = [random.triangular(0,1,0.5) + random.triangular(0,1,0.5) for i in range(10)]
    print("\nDouble triangular distributuion: ",doubleTriangularDistributuion)

    betaDistribution = [random.betavariate(0.5,0.5) for i in range(10)]
    print("\nBeta distribution: ",betaDistribution)

    gammaDistribution = [random.gammavariate(0.5,0.5) for i in range(10)]
    print("\nGamma distribution: ", gammaDistribution)
    
    with open('./python/2022849446/oct/results.csv','w') as f:
        write = csv.writer(f)
        write.writerow(["Uniform distribution: ", uniformDistribution])
        write.writerow(["Triangular distributuion: ", triangularDistributuion])
        write.writerow(["Double triangular distributuion: ", doubleTriangularDistributuion])
        write.writerow(["Beta distribution: ", betaDistribution])
        write.writerow(["Gamma distribution: ", gammaDistribution])
else:
    
    with open('./python/2022849446/oct/results.csv','r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(len(row) > 0 ):      
                randomResult = random.choice(row[1].split(","))
                print(row[0], randomResult)
