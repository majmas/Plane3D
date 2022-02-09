#3D Geometry

import numpy as np
import math

class plane():
    def __init__(self,normal,point):
        self.normal=normal
        self.point=point
        print('The normal and point are {0} and {1}, respectively'.format(self.normal,self.point))
        #Finding plane equation
    def planeparam(self):
        a=self.normal[0];b=self.normal[1];c=self.normal[2]
        d = -self.point.dot(self.normal)
        print('The plane equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))
        # Part 3 - finding distance
    def distance(self):
        x=self.point[0]; y=self.point[1]; z=self.point[2]
        a=self.normal[0];b=self.normal[1];c=self.normal[2]
        d = np.dot([a,b,c], self.normal)

        g = abs((a * x + b * y + c * z + d))
        e = (math.sqrt(a * a + b * b + c * c))
        print("The distance of the point to the plane is", g/e)

# test code
if __name__ == '__main__':
    #choose your point and normal
    Normal=np.array([1, 3, -3])
    Point= np.array([2,5,4])

    p1= plane(Normal,Point)
    p1.planeparam()
    p1.distance()


'''
p1 = np.array([1, 2, 3])
p2 = np.array([4, 6, 9])
p3 = np.array([12, 11, 9])

# These two vectors are in the plane
v1 = p3 - p1
v2 = p2 - p1

# the cross product is a vector normal to the plane
cp = np.cross(v1, v2)
a, b, c = cp

# This evaluates a * x3 + b * y3 + c * z3 which equals d
d = np.dot(cp, p3)

print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))


    def planeparam(self):

        return ,a,b,c,d
'''