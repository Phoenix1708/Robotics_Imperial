import time
import sys
import math
import random
from numpy import zeros

OX = 400
OY = 250
OTheta =  0
D = 100
alpha = math.pi/2

def noise_e():
    return random.gauss(0,0.1)

def noise_f():
    return random.gauss(0,0.1)

def noise_g():
    return random.gauss(0,0.1)

def forward_renew_particle(particle):
    e = noise_e()
    particle[0] = particle[0]+(D+e)*math.cos(particle[2])
    particle[1] = particle[1]+(D+e)*math.sin(particle[2])
    particle[2] = particle[2]+noise_f()
    return particle

def turn_renw_particle(particle):
    particle[2] = particle[2]+alpha+noise_g()
    if particle[2] > 360:
        particle[2] -= 360
    return particle

def renew_particles(particles,operation):
    if operation == "forward":
        for i in range(len(particles)):
            particles[i] = forward_renew_particle(particles[i])
    elif operation == "turn":
        for i in range(len(particles)):
            particles[i] = turn_renw_particle(particles[i])
    return particles

startX = OX
startY = OY
startTheta = OTheta
numberOfParticles = 100

line1 = (OX, OY, OX+300, OY) # (x0, y0, x1, y1)
line2 = (OX+300, OY, OX+300, OY+300)  # (x0, y0, x1, y1)
line3 = (OX+300, OY+300, OX-200, OY+300)

print "drawLine:" + str(line1)
print "drawLine:" + str(line2)
print "drawLine:" + str(line3)

particles = zeros((numberOfParticles,3),float)
for i in range(len(particles)):
    particles[i,0] = OX
    particles[i,1] = OY

string = [(particles[i,0], particles[i,1], particles[i,2]) for i in range(numberOfParticles)]
print "drawParticles:" + str(string)
time.sleep(0.5)

times_forward = [3,3,5]
for i in range(len(times_forward)):
    for j in range(times_forward[i]):
        particles = renew_particles(particles,"forward")
        string = [(particles[k,0], particles[k,1], particles[k,2]) for k in range(numberOfParticles)]
        print "drawParticles:" + str(string)
        time.sleep(0.5)
    particles = renew_particles(particles,"turn")
    string = [(particles[k,0], particles[k,1], particles[k,2]) for k in range(numberOfParticles)]
    print "drawParticles:" + str(string)
    time.sleep(0.5)


