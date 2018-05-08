import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt

class Solver:
    def __init__(self,m=1.0,n=1000,soft=0.01,G=1.0, dt=0.01):
	self.options={'soft':soft,'n':n,'G':G,'dt':dt}
	self.x=np.random.rand(self.options['n'])
	self.y=np.random.rand(self.options['n'])
	self.m=np.ones(self.options['n'])*m
	self.vx=np.zeros(self.options['n'])
	self.vy=np.zeros(self.options['n'])

    def force(self):
	self.fx=np.zeros(self.options['n'])
	self.fy=np.zeros(self.options['n'])
	potential=0
	for i in range(0,self.options['n']):
	    dx=self.x[i]-self.x
	    dy=self.y[i]-self.y
	    soft=self.options['soft']**2
	    rsq=dx**2+dy**2
	    rsq[rsq<soft]=soft
 	    rsq+=self.options['soft']**2
	    r=1.0/np.sqrt(rsq)
	    r2=r/rsq
	    self.fx[i]=-np.sum(self.m*dx*r3)*self.options['G']
            self.fy[i]=-np.sum(self.m*dy*r3)*self.options['G']
            potential+=self.options['G']*np.sum(self.m/r)*self.m[i]
        return -0.5*potential
	
    def updater(self,tint=0.01):
	self.x+=self.vx*tint
	self.y+=self.vy*tint
	potential=self.forces()
	self.vx+=self.fx*tint
	self.vy+=self.fy*tint
	KE=0.5*np.sum(self.m*(self.vx**2+slef.vy**2))
	return potential + kinetc
	
if __name__=='__main__':
    parts=2000
    oversamp=5
    part=Solver(m=1.0/parts,n=parts,dt=0.01/oversamp)
    plt.plot(part.x,part.y,'.')
    plt.show()
    
    fig=plt.figure()
    ax=fig.add_subplot(111, autoscale_on=False,xlim=(-5,5),ylim=(-5,5))
    line, =ax.plot([],[],'*',lw=2)














	
