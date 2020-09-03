"""
Class for performing numerical integration using the
cumulative (composite) trapezoidal rule. Error bars
are computed based on standard uncertainty propagation.

author: Rasmus Kronberg
email: rasmus.kronberg@aalto.fi

"""

import numpy as np


class Trapz:
    def __init__(self, y, x=None, dx=1.0):

        self.y = y

        # Calculate grid spacing
        if x is not None:
            self.dx = np.diff(x)
        else:
            self.dx = dx*np.ones(len(y))

    def integrate(self, init=0.0):

        y = self.y
        dx = self.dx
        i = np.arange(len(y)-1)

        # Cumulative trapezoidal rule
        integral = 0.5*np.cumsum((y[i]+y[i+1])*dx)
        self.integral = np.concatenate(([init], integral))

    def propagate(self, yerr):

        dx = self.dx
        i = np.arange(len(yerr)-2)

        # Single grid spacing at boundaries, two-step elsewhere
        ddx = dx[i]+dx[i+1]
        ddx = np.concatenate(([dx[0]], ddx, [dx[-1]]))

        # Error propagation of a weighted sum
        self.error = np.sqrt(0.25*np.cumsum((yerr*ddx)**2))
