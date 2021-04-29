# trapz-error-propagation

Python code for numerical integration of uncertain data using the cumulative (composite) trapezoidal method. The error is propagate using the standard rules for [uncertainty propagation of a weighted sum](https://en.wikipedia.org/wiki/Propagation_of_uncertainty#Example_formulae) (assuming zero covariance).

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

Results are stored as the attributes ```tz.integral``` and ```tz.error```, respectively. Code can also be run from the command line using the example ```main.py``` script.

```console
$ python main.py --help
usage: main.py [-h] -i INPUT [-I INITIAL] [-p]

(Thermodynamic) integration code

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input pandas DataFrame (.csv)
  -I INITIAL, --initial INITIAL
                        Initial value of integral
  -p, --plot            Visualize results
```

Input ```DataFrame``` with columns ```xdata```, ```ydata``` and ```yerror```, as well as optional initial value are passed as arguments. Optional flag ```-p``` enables a visualization of the result. An example dataset ```data/sample.csv``` containing 30 randomly sampled points of a 1st order Gaussian derivative with random errors is provided.
