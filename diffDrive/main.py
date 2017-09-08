import numpy as np
import posq

t = 0
xnow = [0,0,0]
xend = [1,1,np.pi/2]
direction = 1
old_beta = 0
vmax = 1
base = 0.4

output = []

output=posq.step(t,xnow,xend,direction,old_beta,vmax,base)
#vl,vr,eot,vd,old_beta=posq.step(t,xnow,xend,direction,old_beta,vmax,base)



print(output)
