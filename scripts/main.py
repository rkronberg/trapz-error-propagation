import numpy as np
from argparse import ArgumentParser
from trapz_error import Trapz
import matplotlib.pyplot as plt

def parse():

	# Parse command line arguments

	p = ArgumentParser(description='Thermodynamic integration code')
	p.add_argument('-i', '--input', required=True, help='Input file')
	p.add_argument('-I', '--initial', type=float, default=0.0, help='Initial value of integral')
	p.add_argument('-p', '--plot', action='store_true', help='Visualize results')

	return vars(p.parse_args())

def main():

	args = parse()
	inp = args['input']
	init = args['initial']
	isplot = args['plot']

	# Expects input shape (n, m) where n is the number 
	# of samples and m = 3 (xdata, ydata, yerror)
	xdata = np.loadtxt(inp, usecols=[0])
	ydata = np.loadtxt(inp, usecols=[1])
	yerr = np.loadtxt(inp, usecols=[2])

	# Initialize by calculating grid spacing based on xdata
	tz = Trapz(xdata)

	# Integrate using the cumulative trapezoidal rule
	tz.integrate(ydata, init)

	# Propagate errors associated with input ydata
	tz.propagate(yerr)

	np.savetxt('integral.out', np.c_[xdata, tz.integral, tz.error], header='x, F(x), error')

	# Visualize results
	if(isplot):
		plt.plot(xdata, tz.integral)
		plt.fill_between(xdata, tz.integral-tz.error, tz.integral+tz.error, alpha=0.3)
		plt.show()

if __name__ == '__main__':
	main()
	