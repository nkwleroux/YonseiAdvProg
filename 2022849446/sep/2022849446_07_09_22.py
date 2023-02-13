from math import sqrt, radians, sin, cos, atan2

print("Student id is:", 2022849446)

SeoulTuple = (37.566, 126.9784)
BusanTuple = (35.10168, 129.03004)
earthRadius = 6378.137 #in km

def pointOfSymmetry(coord1,coord2):
    return ((coord1[0]+coord2[0])/2,(coord1[1]+coord2[1])/2)

def distanceBetweenCoordsTuple(coord1,coord2):
    return sqrt(pow(coord2[0]-coord1[0],2)+pow(coord2[1]-coord1[1],2))

def arcDistanceBetweenCoordsTuple(coord1,coord2):
    
    lat1 = radians(coord1[0])
    lat2 = radians(coord2[0])
    
    dLat = radians(coord2[0]-coord1[0])
    dLong = radians(coord2[1]-coord1[1])

    #Haversine formula found online at https://www.movable-type.co.uk/scripts/latlong.html
    a = sin(dLat/2) * sin(dLat/2) + cos(lat1) * cos(lat2) * sin(dLong/2) * sin(dLong/2)
    
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return earthRadius * c # in km

distance = distanceBetweenCoordsTuple(SeoulTuple,BusanTuple)
arcDistance = arcDistanceBetweenCoordsTuple(SeoulTuple,BusanTuple)

print("The coordinates of Seoul is", SeoulTuple, ". The coordinates of Busan is", BusanTuple, ".")
print("The point of symmetry/middle point is", pointOfSymmetry(SeoulTuple,BusanTuple))
print("The distance between Seoul and Busan is (Euclidean):", distance,"km")
print("The distance to the middle point is (Euclidean):", distance/2,"km")
print("The distance between Seoul and Busan is (Arc/Haversine formula):", arcDistance,"km")
print("The distance to the middle point is (Arc/Haversine formula):", arcDistance/2,"km")