# trapz-error-propagation

Python code for numerical integration of uncertain data using the cumulative (composite) trapezoidal method. The error is propagate using the standard rules for [uncertainty propagation of a weighted sum](https://en.wikipedia.org/wiki/Propagation_of_uncertainty#Example_formulae) (with zero covariance).

## Usage

```python
from trapz_error import Trapz

# Initialize by computing grid spacing based on given xdata (defaults 
# to None) or passing the uniform grid spacing dx (defaults to 1.0)
tz = Trapz(ydata, x=xdata, dx=dx)

# Integrate using the cumulative trapezoidal rule and set initial 
# value of the integral (defaults to 0.0)
tz.integrate(init)

# Propagate the errors of input ydata
tz.propagate(yerror)
```

Code can also be run from the command line using the ```main.py``` script.

```bash
$ python main.py [-h] -i INPUT [-I INITIAL] [-p]
```

Input datafile with shape ```(n, 3)``` and optional initial value are passed as arguments. Optional flag ```-p``` enables a visualization of the result. A sample dataset ```data/sample.dat``` containing 30 points of a 1st order Gaussian derivative with random errors is provided.
