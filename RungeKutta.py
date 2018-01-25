import matplotlib.pyplot as plt
import numpy as np
import math

# Y_1 = stretch
# Y_2 = stretch'

# Y_1' = stretch' = Y_2
# Y_2' = stretch'' = equation given

# Z_1 = swing
# Z_2 = swing'

# Z_1' = swing' = Y_2
# Z_2' = swing'' = equation given

# Stepsize
h = 0.1

# Step array
xVals = np.arange( 0, 5, h )

# Solution arrays
Y_1 = []
Y_2 = []
Z_1 = []
Z_2 = []

# Initial parameter
pendMass = 0.1 # mass of the pendulum
springConst = 0.2 # spring constant
length = 0.3 # unstretched length of the pendulum
stretch = 0.4 # stretch
stretchPrime = 0.2
gravAccel = 0.1 # acceleration due to gravity
swing = 0.7 # swing degrees-of-freedom
swingPrime = 0.2

# Start arrays with initial values
Y_1.append(stretch) 
Y_2.append(stretchPrime) 
Z_1.append(swing) 
Z_2.append(swingPrime)

#-------------------------FUNCTIONS-------------------------------------------
# First order equations
def f( stretch, y1, y2, z1, z2, pendMass, springConst, length, gravAccel ):
    return y2
def fPrime( stretch, y1, y2, z1, z2, pendMass, springConst, length, gravAccel):
    return -( springConst / pendMass ) * y1 + ( length + y1 ) * ( z2 ** 2 ) + gravAccel * math.cos( z1 )
def g( stretch, y1, y2, z1, z2, pendMass, springConst, length, gravAccel ):
    return z2
def gPrime(stretch, y1, y2, z1, z2, pendMass, springConst, length, gravAccel ):
    return -( ( gravAccel * math.sin( z1 ) - 2 * y2 * z2 ) / ( length + y1) )

# k functions
def k1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return h * f( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel )
def k2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return h * f( xn + h/2, y1n + k1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def k3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * f( xn + h/2, y1n + k2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def k4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return h * f( xn + h, y1n + k3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), y2n + l3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z1n + p3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z2n + q3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), pendMass, springConst, length, gravAccel )
def k( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return (1.0/6.0) * ( k1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * k2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * k3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + k4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) )

# l functions
def l1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * fPrime( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel )
def l2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * fPrime( xn + h/2, y1n + k1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def l3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * fPrime( xn + h/2, y1n + k2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def l4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * fPrime( xn + h, y1n + k3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), y2n + l3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z1n + p3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z2n + q3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), pendMass, springConst, length, gravAccel )
def l( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return (1.0/6.0) * ( l1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * l2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * l3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + l4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) )

# p functions
def p1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return h * g( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel )
def p2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return h * g( xn + h/2, y1n + k1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def p3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * g( xn + h/2, y1n + k2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def p4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return h * g( xn + h, y1n + k3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), y2n + l3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z1n + p3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z2n + q3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), pendMass, springConst, length, gravAccel )
def p( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
	return (1.0/6.0) * ( k1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * k2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * k3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + k4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) )

# q functions
def q1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * gPrime( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel )
def q2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * gPrime( xn + h/2, y1n + k1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def q3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * gPrime( xn + h/2, y1n + k2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, y2n + l2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z1n + p2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, z2n + q2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) / 2, pendMass, springConst, length, gravAccel )
def q4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return h * gPrime( xn + h, y1n + k3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), y2n + l3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z1n + p3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), z2n + q3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ), pendMass, springConst, length, gravAccel )
def q( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ):
    return (1.0/6.0) * ( l1( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * l2( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + 2 * l3( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) + l4( xn, y1n, y2n, z1n, z2n, pendMass, springConst, length, gravAccel ) )

#------------------------MAIN PROGRAM------------------------------------------
n=0
while( n < len(xVals) - 1 ):
    Y_1.append( Y_1[n] + k( xVals[n], Y_1[n], Y_2[n], Z_1[n], Z_2[n], pendMass, springConst, length, gravAccel ) ) 
    Y_2.append( Y_2[n] + l( xVals[n], Y_1[n], Y_2[n], Z_1[n], Z_2[n], pendMass, springConst, length, gravAccel ) )
    Z_1.append( Z_1[n] + p( xVals[n], Y_1[n], Y_2[n], Z_1[n], Z_2[n], pendMass, springConst, length, gravAccel ) ) 
    Z_2.append( Z_2[n] + q( xVals[n], Y_1[n], Y_2[n], Z_1[n], Z_2[n], pendMass, springConst, length, gravAccel ) )    
    n+=1

plt.plot( xVals, Y_1 )
plt.show()

plt.plot( xVals, Z_1 )
plt.show()