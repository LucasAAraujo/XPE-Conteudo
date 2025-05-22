from math import sqrt

def rootSquareSolver(a,b,c):
    r1 = (-b+sqrt(b*b-4*a*c))/(2*a)
    r2 = (-b-sqrt(b*b-4*a*c))/(2*a)
    return [r1,r2]