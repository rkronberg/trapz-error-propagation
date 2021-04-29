import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser

from trapz_error import Trapz


def parse():

    # Parse command line arguments

    p = ArgumentParser(description='(Thermodynamic) integration code')
    p.add_argument('-i', '--input', required=True,
                   help='Input pandas DataFrame (.csv)')
    p.add_argument('-I', '--initial', type=float, default=0.0,
                   help='Initial value of integral')
    p.add_argument('-p', '--plot', action='store_true',
                   help='Visualize results')

    return p.parse_args()


def main():

    args = parse()
    inp = args.input
    init = args.initial
    isplot = args.plot

    try:
        df = pd.read_csv(inp)
        xdata = df['xdata'].to_numpy()
        ydata = df['ydata'].to_numpy()
        yerror = df['yerror'].to_numpy()
    except FileNotFoundError as err:
        print('%s: %s' % (err.args[1], inp))
        quit()
    except KeyError as err:
        print('Column %s not found in input DataFrame' % err)
        quit()

    # Initialize by calculating grid spacing based on xdata
    tz = Trapz(ydata, x=xdata)

    # Integrate using the cumulative trapezoidal rule
    tz.integrate(init)

    # Propagate errors associated with input ydata
    tz.propagate(yerror)

    # Store output as .csv
    out = pd.DataFrame({'x': xdata, 'F(x)': tz.integral, 'error': tz.error})
    out.to_csv('integral.csv', index=False)

    # Visualize results
    if(isplot):
        plt.plot(xdata, tz.integral, '.-')
        plt.fill_between(
            xdata, tz.integral-tz.error, tz.integral+tz.error, alpha=0.25)
        plt.show()


if __name__ == '__main__':
    main()
