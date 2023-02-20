#Задание №6
#(Points of Reflection)
#https://www.codewars.com//kata/57bfea4cb19505912900012c

def symmetric_point(p, q):
    x = (q[0] - p[0] + q[0])
    y = (q[1] - p[1] + q[1])
    newpoint = [x, y]
    return newpoint