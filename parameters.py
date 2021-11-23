import itertools
# Define the d and q parameters to take any value between 0 and 1
def para():
    q = d = range(0, 2)
    # Define the p parameters to take any value between 0 and 3
    p = range(0, 4)

    # Generate all different combinations of p, q and q triplets
    pdq = list(itertools.product(p, d, q))
    # print(pdq)
    # Generate all different combinations of seasonal p, q and q triplets
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
    #print('Examples of parameter combinations for Seasonal ARIMA...')
    #print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
    #print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
    #print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
    #print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

    return pdq, seasonal_pdq

def AIC(b,c):
    print('The smallest AIC is {} for model SARIMAX{}x{}'.format(min(b), c[b.index(min(b))][0], c[b.index(min(b))][1]))
