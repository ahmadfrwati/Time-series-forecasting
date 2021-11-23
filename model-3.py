# Import libraries
import warnings
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Defaults
plt.rcParams['figure.figsize'] = (20.0, 10.0)
plt.rcParams.update({'font.size': 12})
plt.style.use('ggplot')

# Define the d and q parameters to take any value between 0 and 1
q = d = range(0, 2)
# Define the p parameters to take any value between 0 and 3
p = range(0, 4)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))
# print(pdq)
# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

temp_storage = 'Result_9.csv'
raw = ['city_id', 'date', 'number_successful_order', 'number_od_successful_order', 'amount_od_successful_order', 'abs']
info = pd.read_csv(temp_storage, usecols=raw, engine='python', skipfooter=3)


df1 = pd.DataFrame(columns=['date', 'number_successful_order'])
df2 = pd.DataFrame(columns=['date', 'number_od_successful_order'])
df3 = pd.DataFrame(columns=['date', 'amount_od_successful_order'])
df4 = pd.DataFrame(columns=['date', 'abs'])
s = len(info)
for i in range(s):
    if (info['city_id'][i]) == 12: ###8
        # print(info['number_successful_order'][i:i+1])
        df1.loc[i] = info['date'][i], info['number_successful_order'][i]
        df2.loc[i] = info['date'][i], info['number_od_successful_order'][i]
        df3.loc[i] = info['date'][i], info['amount_od_successful_order'][i]
        df4.loc[i] = info['date'][i], info['abs'][i]

df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
df1.set_index(['date'], inplace=True)
df2['date'] = pd.to_datetime(df2['date'], format='%Y-%m-%d')
df2.set_index(['date'], inplace=True)
df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
df3.set_index(['date'], inplace=True)
df4['date'] = pd.to_datetime(df4['date'], format='%Y-%m-%d')
df4.set_index(['date'], inplace=True)

train_data1 = df1['2018-01-01':'2021-4-30']
test_data1 = df1['2021-05-01':'2021-5-31']
train_data2 = df2['2018-01-01':'2021-4-30']
test_data2 = df2['2021-05-01':'2021-5-31']
train_data3 = df3['2018-01-01':'2021-4-30']
test_data3 = df3['2021-05-01':'2021-5-31']
train_data4 = df4['2018-01-01':'2021-4-30']
test_data4 = df4['2021-05-01':'2021-5-31']

arr1 = train_data1.astype(np.float)
arr2 = train_data2.astype(np.float)
arr3 = train_data3.astype(np.float)
arr4 = train_data4.astype(np.float)

arr11 = test_data1.astype(np.float)
arr22 = test_data2.astype(np.float)
arr33 = test_data3.astype(np.float)
arr44 = test_data4.astype(np.float)

df1.plot()

from statsmodels.tsa.stattools import adfuller


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


adfuller_test(df1['number_successful_order'])

from pandas.plotting import scatter_matrix
from pandas.plotting import autocorrelation_plot

autocorrelation_plot(df1['number_successful_order'])
plt.show()

from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
from statsmodels.tsa.api import SARIMAX
from numpy import array


def fittiing(colom):
    warnings.filterwarnings("ignore")  # specify to ignore warning messages
    AIC = []
    SARIMAX_model = []
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(colom,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)
                # print("d")

                results = mod.fit()

                print('SARIMAX{}x{} - AIC:{}'.format(param, param_seasonal, results.aic), end='\r')
                AIC.append(results.aic)
                SARIMAX_model.append([param, param_seasonal])
            except:

                continue
    return results, AIC, SARIMAX_model


a, b, c = fittiing(arr4)  ### arr1 to arr4

import pickle

pickle.dump(a, open("model12-4-a.pkl", "wb"))
pickle.dump(b, open("model12-4-b.pkl", "wb"))
pickle.dump(c, open("model12-4-c.pkl", "wb"))
#pickle.dump(a, open('E:/TSF', 'wb'))

