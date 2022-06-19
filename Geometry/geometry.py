import math

def triangleArea(base, height):
    return (base*height)/2
def triangleHeight(base, Area):
    return 2*(area/base)
def triangleBase(height, Area):
    return 2*(area/height)
def trapeziumArea(a, b, height):
    return ((a+b)/2)*h
def trapeziumHeight(a, b, Area):
    return 2*(Area/(a+b))
def paraArea(base, height):
    return base*height
def paraHeight(a, b):
    return a/b
def circleCircumference(radius):
    return 2*math.pi*radius
def circleArea(radius):
    return math.pi*(radius**2)
def sphereVolume(radius):
    return 4/3*math.pi*(radius**3)
def sphereArea(radius):
    return 4*math.pi*(radius**2)
def surfaceArea(a, b, c):
    d = a*b
    e = a*c
    f = b*c
    return 2*(d+e+f)
def volume(a, b, c):
    return a*b*c
def cylinderVolume(radius, height):
    return (math.pi*(radius**2))*height
def cylinderArea(radius, height):
    return (2*math.pi*radius*height)+(2*math.pi*(radius**2))
def cylinderDiameter(volume, height):
    return 2*(mathsqrt(volume/math.pi*height))
def cylinderHeight(volume, radius):
    return volume/(math.pi*(radius**2))
def cylinderRadius(height, Area):
    return round(0.5*math.sqrt(height**2 + 2*(Area/math.pi))-height/2, 5)
def coneArea(radius, height):
    return round(math.pi*radius*(radius + math.sqrt(height**2 + radius**2)), 5)
def coneVolume(radius, height):
    return round(math.pi*radius**2*(height/3), 5)
def coneRadius(height, volume):
    return round(math.sqrt(3*(volume/(math.pi*height))), 5)
def coneHeight(radius, volume):
    return round(3*(volume/(math.pi*radius**2)), 5)
def coneSlantHeight(radius, height):
    return math.sqrt(radius*radius + height*height)
def arcLength(radius, angle):
    return radius * angle
def sectorArea(radius, angle):
    return round(angle/360 * (math.pi*(radius*radius)), 5)
def pyTheoremAB(a, b):
    return math.sqrt(a*a + b*b)
def pyTheoremAC(a, c):
    return math.sqrt(c*c - a*a)
def pyTheoremBC(b, c):
    return math.sqrt(c*c - b*b)




