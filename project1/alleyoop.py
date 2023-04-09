import numpy
import scipy.constants
from vpython import box, vector, rate, color, sphere, ring

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:05:27 2022

@author: Joseph Helsing
"""

GRAVITY = scipy.constants.g

aoDistFromBasket = 0.375
aoMaxHeight = 2.35
ballHeight = 1.50


#distFromBasket = 6.75
distFromBasket = float(input("How far from the hoop is the player with the ball, in meters: "))

#aoJumpVel = 4.00
aoJumpVel = float(input("What is jumping player's jumping speed: "))

#ballAngle = 50.0
ballAngle = float(input("What angle is the ball thrown at: "))
ballRadians = numpy.pi/180 * ballAngle

ballTravelDist = distFromBasket-aoDistFromBasket
heightDiff = ballHeight - aoMaxHeight

ballVel = ballTravelDist/numpy.cos(ballRadians) * numpy.sqrt((GRAVITY/2)/(heightDiff + ballTravelDist * numpy.tan(ballRadians) - aoJumpVel**2/(2*GRAVITY)))
jumpDelay = ballTravelDist/(ballVel*numpy.cos(ballRadians)) - aoJumpVel/GRAVITY
timeTillCatch = jumpDelay + aoJumpVel/GRAVITY

print("The speed the ball must thrown is %.2f m/s." % (ballVel))
print("The jumping player needs to wait %.2f seconds after you throw the ball to catch it at the perfect moment." % (jumpDelay))


d = distFromBasket
l = aoDistFromBasket
hb = ballHeight
hs = aoMaxHeight
thb = ballRadians
vb = ballVel
vs = aoJumpVel
hh = 3.05
tcatch = timeTillCatch
tj = jumpDelay

you = box(pos=vector(-d/2, hb/2-1.5, 0), length=.2, width=.2, height=hb, color=color.blue)
jumper = box(pos=vector(d/2-l, hs/2-1.5, 0), length=.2, width=.2, height=hs, color=color.red, velocity=vector(0, vs, 0))
ball = sphere(pos=vector(-d/2, hb-1.5, 0), radius=.1, color=color.orange, velocity=vector(vb*numpy.cos(thb), vb*numpy.sin(thb), 0), make_trail=True)
hoop = ring(pos=vector(d/2, hh-1.5, 0), axis=vector(0, 1, 0), radius=.2, thickness=0.05, color=color.green)

dt = 0.001
t = 0

def update_object(obj, dt=dt, accel=vector(0, -GRAVITY, 0)):
    obj.pos = obj.pos + obj.velocity*dt
    obj.velocity = obj.velocity + accel*dt
    

while t<tcatch:
    rate(100)
    update_object(ball)
    if t>=tj:
        update_object(jumper)
    
    t = t + dt
