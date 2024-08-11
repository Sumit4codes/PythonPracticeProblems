# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
import math
print("Enter the Direction and Steps: ")
directions=[]
while(1):
    d=input()
    if d=="":
        break
    else:
        a=d.split()
        directions.append(a)


print(directions)

x1=0
y1=0

x2=0
y2=0

for i in directions:
    if i[0]=="UP":
        y2=y2+int(i[1])
    if i[0]=="DOWN":
        y2=y2-int(i[1])
    if i[0]=="RIGHT":
        x2=x2+int(i[1])
    if i[0]=="LEFT":
        y2=y2-int(i[1])

distance= math.sqrt((x2-x1)**(2)+(y2-y1)**(2))
print("Distance: ",int(distance))