"""
Class for performing numerical integration using the 
cumulative (composite) trapezoidal rule. Error bars 
are computed based on standard uncertainty propagation.

author: Rasmus Kronberg
email: rasmus.kronberg@aalto.fi

"""

import numpy as np

class Trapz:
	def __init__(self, x):

		self.dx = np.diff(x)

	def integrate(self, y, init=0.0):
	
		i = np.arange(len(y)-1)
		integral = 0.5*np.cumsum((y[i]+y[i+1])*self.dx)
		self.integral = np.concatenate(([init], integral))
	
	def propagate(self, yerr):
	
		i = np.arange(len(yerr)-2)
		ddx = self.dx[i]+self.dx[i+1]
		ddx = np.concatenate(([self.dx[0]], ddx, [self.dx[-1]]))
	
		self.error = np.sqrt(0.25*np.cumsum((yerr*ddx)**2))