
print("Student id is:", 2022849446)

#Coordinates in the Netherlands
# Ridderkerk
coord1_Ridderkerk_Top = (51.889888, 4.600195)
coord1_Ridderkerk_Middle = (51.882606, 4.618227)
coord1_Ridderkerk_Bottom = (51.861026, 4.630916)
coord1_Ridderkerk_Population = 46241 #inhabitants
# 11 schools, 1 police, 2 moskee/church, 4 medical buildings, 1 animal medical, 11 dentist, 2 goverment building, 1 fire station
coord1_Ridderkerk_Public_Buildings = 33

# Barendrecht
coord2_Barendrecht_Top = (51.826676, 4.517158)
coord2_Barendrecht_Middle = (51.849957, 4.518049)
coord2_Barendrecht_Bottom = (51.840600, 4.533266)
coord2_Barendrecht_Population = 48673 #inhabitants
# 14 schools, 1 police, 7 moskee/church, 6 medical buildings, 3 animal medical, 7 dentist, 5 goverment building, 1 fire station
coord2_Barendrecht_Public_Buildings = 44

def pointOfSymmetry(coord1, coord2):
     return ((coord1[0]+coord2[0])/2,(coord1[1]+coord2[1])/2)

coord3_MiddleCoord_Top = pointOfSymmetry(coord1_Ridderkerk_Top,coord2_Barendrecht_Top)
coord3_MiddleCoord_Middle = pointOfSymmetry(coord1_Ridderkerk_Middle,coord2_Barendrecht_Middle)
coord3_MiddleCoord_Bottom =  pointOfSymmetry(coord1_Ridderkerk_Bottom,coord2_Barendrecht_Bottom)

print("Top coord point of symmetry is", coord3_MiddleCoord_Top)
print("Middle coord point of symmetry is", coord3_MiddleCoord_Middle)
print("Bottom coord point of symmetry is", coord3_MiddleCoord_Bottom)

coord1 = [coord1_Ridderkerk_Top, coord1_Ridderkerk_Middle ,coord1_Ridderkerk_Bottom]
coord2 = [coord2_Barendrecht_Top, coord2_Barendrecht_Middle, coord2_Barendrecht_Bottom]
coord3 = [coord3_MiddleCoord_Top, coord3_MiddleCoord_Middle, coord3_MiddleCoord_Bottom] 

print("There is a total of", coord1_Ridderkerk_Public_Buildings, "buildings within the Ridderkerk section")
print("line A: ", *coord1, sep = ", ")
print("line M: ", *coord3, sep = ", ")
print("There is a total of", coord2_Barendrecht_Public_Buildings, "buildings within the Barendrecht section")
print("line M: ", *coord3, sep = ", ")
print("line B: ", *coord2, sep = ", ")