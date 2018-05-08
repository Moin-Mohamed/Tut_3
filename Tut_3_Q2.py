import numpy as np

class Solver:
	def __init__(self,x=0,y=0,n=1000,G=1.0):
		self.x=np.random.randn(n) #produces random x points
		self.y=np.random.randn(n) #produces random y points
		self.m=np.ones(n) #produces a mass for every position
		self.option={'particles':n,'GC':G} #dictionary
	def potential(self):
		pot=np.zeros(self.option['particles']) #this sets the intitial potential to zero for every particle
		for i in range(0,self.option['particles']):
			dx=self.x[i]-self.x
			dy=self.y[i]-self.y
			r=1.0/np.sqrt(dx**2+dy**2) 
			pot[i]=np.sum(self.option['GC']*self.m[i]*self.m*r)
		return pot


