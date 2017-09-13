import random
import math
#n = 123
#print ((n - n % 10) / 10) % 10
#print ((n - n % 10) % 100) / 10
#print (n % 10) / 10

#print random.randint(0, 10)
#print random.randrange(0, 10)

def polygon(n, s):
    return ((1/4.0)*n*math.pow(s, 2))/math.tan(math.pi/n)

#print polygon(7, 3)

#/1/4 n s2 / tan(pi/n).

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)