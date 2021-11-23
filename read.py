import pickle
from statsmodels.tsa.stattools import adfuller
def pretrained(modela:str, modelb:str, modelc:str):

    a = pickle.load(open(modela, 'rb'))
    b = pickle.load(open(modelb, 'rb'))
    c = pickle.load(open(modelc, 'rb'))
    return a, b, c


def adfuller_test(sales):
    result = adfuller(sales)
    labels = ['ADF Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used']
    for value, label in zip(result, labels):
        print(label + ' : ' + str(value))
    if result[1] <= 0.05:
        print(
            "strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")


a = pickle.load(open('model3-2-a.pkl', 'rb'))
