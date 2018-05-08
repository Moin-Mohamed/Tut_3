#______PROBLEM 1______

#added the __sub__, __mul__ and __div__ class definitions

import numpy

class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def copy(self):
        return Complex(self.r,self.i)
    def __add__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r+val.r
            ans.i=ans.i+val.i
        else:
            ans.r=ans.r+val
        return ans

    def __sub__(self,val):
	ans=self.copy()
	if isinstance(val,Complex):
	    ans.r=ans.r-val.r
	    ans.i=ans.i-val.i
	else:
	    ans.r=ans.r-val
	return ans

    def __mul__(self,val):
	ans=self.copy()
	if isinstance(val,Complex):
	    ans.r=self.r*val.r-self.i*val.i
	    ans.i=self.r*val.i+self.i*val.r
	else:
	    ans.r=ans.r*val
	    ans.i=ans.i*val
	return ans

    def __div__(self,val):
	if isinstance(val,Complex):
	    val=val.copy() #making a copy of the denominator
	    val.i=-1*val.i #this gets the "complex conjugate"
	    numerator=self*val
	    denominator=val.r**2+val.i**2
	    ans=numerator*(1.0/denominator)
	else:
	    ans=self*(1.0/val)
	return ans

    def __repr__(self):
        if (self.i<0):
            return repr(self.r)+' - '+repr(-1*self.i) +'i'
        else:
            return repr(self.r)+' + '+repr(self.i) +'i'

if __name__=='__main__':

    a=Complex(2,5)
    b=Complex(4,-3)
    c=a+b
    print c
    d=a-b
    print d
    e=a*b
    print e
    f=a/b
    print f

