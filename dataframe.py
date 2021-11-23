import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import statsmodels.api as sm

######################################
Today = date.today()


###################################

###########################
#update_day = 'test.csv'
#raw1 = ['city_id', 'date', 'number_successful_order', 'number_od_successful_order', 'amount_od_successful_order', 'abs']
#coming_day = pd.read_csv(update_day, usecols=raw, engine='python', skipfooter=3)
############################
#df1_new = pd.DataFrame(columns=['date', 'number_successful_order'])
#df2_new = pd.DataFrame(columns=['date', 'number_od_successful_order'])
#df3_new = pd.DataFrame(columns=['date', 'amount_od_successful_order'])
#df4_new = pd.DataFrame(columns=['date', 'abs'])
#s_new = len(coming_day)
############################



def col(j) :
    temp_storage = 'Result_9.csv'
    raw = ['city_id', 'date', 'number_successful_order', 'number_od_successful_order', 'amount_od_successful_order',
           'abs']
    info = pd.read_csv(temp_storage, usecols=raw, engine='python', skipfooter=3)
    s = len(info)
    df1 = pd.DataFrame(columns=['date', 'number_successful_order'])
    df2 = pd.DataFrame(columns=['date', 'number_od_successful_order'])
    df3 = pd.DataFrame(columns=['date', 'amount_od_successful_order'])
    df4 = pd.DataFrame(columns=['date', 'abs'])
    for i in range(s):

        if (info['city_id'][i]) == j:
            # print(info['number_successful_order'][i:i+1])
            df1
            df1.loc[i] = info['date'][i], info['number_successful_order'][i]
            df2.loc[i] = info['date'][i], info['number_od_successful_order'][i]
            df3.loc[i] = info['date'][i], info['amount_od_successful_order'][i]
            df4.loc[i] = info['date'][i], info['abs'][i]
    p_first = df1['date'][-30:-29]
    p_last = df1['date'][-1:]
    #print(p_first.iloc[0])

    df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
    df1.set_index(['date'], inplace=True)
    df2['date'] = pd.to_datetime(df2['date'], format='%Y-%m-%d')
    df2.set_index(['date'], inplace=True)
    df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
    df3.set_index(['date'], inplace=True)
    df4['date'] = pd.to_datetime(df4['date'], format='%Y-%m-%d')
    df4.set_index(['date'], inplace=True)



    train_data1 = df1[0:-30]
    test_data1 = df1[-30:]
    train_data2 = df2[0:-30]
    test_data2 = df2[-30:]
    train_data3 = df3[0:-30]
    test_data3 = df3[-30:]
    train_data4 = df4[0:-30]
    test_data4 = df4[-30:]



    arr1 = train_data1.astype(np.float64)
    arr2 = train_data2.astype(np.float64)
    arr3 = train_data3.astype(np.float64)
    arr4 = train_data4.astype(np.float64)

    arr11 = test_data1.astype(np.float64)
    arr22 = test_data2.astype(np.float64)
    arr33 = test_data3.astype(np.float64)
    arr44 = test_data4.astype(np.float64)


    #print(arr1)


    return arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, p_first.iloc[0], p_last.iloc[0]













