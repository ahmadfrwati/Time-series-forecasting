from datetime import datetime, timedelta
import numpy as np
import itertools
import pandas as pd
def forecast(a,col):
    ini_time_for_now = datetime.now()


    future_date_after_month = ini_time_for_now + timedelta(days=30)
    pred3 = a.get_forecast(future_date_after_month)
    pred3_ci = pred3.conf_int()
    month_forcasting = pred3.predicted_mean[ini_time_for_now:future_date_after_month]
    df = pd.DataFrame(month_forcasting).reset_index()

    df.columns = ['Date', col]



    #print(month_forcasting)
    #print(df)
    return df
def evaluation(test_first, test_last,test_data,model):
    pred1 = model.get_prediction(start=test_first, dynamic=False)
    pred1_ci = pred1.conf_int()
    prediction = pred1.predicted_mean[test_first:test_last].values
    #print(prediction)
    # flatten nested list

    # del list
    truth = list(itertools.chain.from_iterable(test_data.values))
    # Mean Absolute Percentage Error
    MAPE = np.mean(np.abs((truth - prediction) / truth)) * 100

    print('The Mean Absolute Percentage Error for the forecast of year 2021  for last month is {:.2f}%'.format(MAPE))

