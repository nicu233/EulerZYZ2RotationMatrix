import numpy as np
import math

pi = 3.1415926

# ZYZ 2 rotation matrix
# reference https://en.wikipedia.org/wiki/Euler_angles

# assume Z Y Z
Z1 = 82.86599 * pi / 180.0 # O
Y2 = 60.78886 * pi / 180.0 # A
Z3 = 84.08982 * pi / 180.0 # T

print("Z1 ", Z1, "Y2 ", Y2, "Z3 ", Z3)

R = np.identity(3)

c1 = math.cos(Z1)
c2 = math.cos(Y2)
c3 = math.cos(Z3)

s1 = math.sin(Z1)
s2 = math.sin(Y2)
s3 = math.sin(Z3)

R[0,0] = c1*c2*c3 -s1*s3
R[0,1] = -c3*s1 - c1*c2*s3
R[0,2] = c1*s2

R[1,0] = c1*s3 + c2*c3*s1
R[1,1] = c1*c3 - c2*s1*s3
R[1,2] = s1*s2

R[2,0] = -c3*s2
R[2,1] = s2*s3
R[2,2] = c2

print("Rotation ", R)

# rotation matrix 2 ZYZ Euler 
alpha_Z1 = math.atan2(R[1,2], R[0,2])
beta_Y2 = math.atan2(math.sqrt(1 - R[2,2] * R[2,2]), R[2,2])
gamma_Z3 = math.atan2(R[2,1], -1*R[2,0])

print("alpha ", alpha_Z1, "beta ", beta_Y2, "gamma ", gamma_Z3)

# Rotation martix 2 Axis angle
# Reference https://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/index.htm
m00 = R[0,0]
m01 = R[0,1]
m02 = R[0,2]
m10 = R[1,0]
m11 = R[1,1]
m12 = R[1,2]
m20 = R[2,0]
m21 = R[2,1]
m22 = R[2,2]
ang = math.acos((m00 + m11 + m22 - 1)/2)
den = math.sqrt((m21-m12)*(m21-m12) + (m02-m20)*(m02-m20) + (m10-m01)*(m10-m01) )
AAX = (m21 - m12) / den
AAY = (m02 - m20) / den
AAZ = (m10 - m01) / den
print("Axis Angle: angle is ", ang, "X is ", AAX*ang, "Y is", AAY*ang, "Z is ", AAZ*ang)


# Axis angle 2 Rotation matrix
# Reference https://www.euclideanspace.com/maths/geometry/rotations/conversions/angleToMatrix/index.htm
c = math.cos(ang)
s = math.sin(ang)
t = 1 - c
x = AAX
y = AAY
z = AAZ

R2 = np.identity(3)
R2[0,0] = t*x*x + c
R2[0,1] = t*x*y - z*s
R2[0,2] = t*x*z + y*s

R2[1,0] = t*x*y + z*s
R2[1,1] = t*y*y + c
R2[1,2] = t*y*z - x*s

R2[2,0] = t*x*z - y*s
R2[2,1] = t*y*z + x*s
R2[2,2] = t*z*z + c

print("Rotation matrix from Axis Angle is ", R2)

