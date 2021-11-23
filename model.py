# Import libraries
import warnings
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from fit import fittiing
from read import pretrained
from dataframe import col
from write import writer
import time
import pickle
from forecasting import forecast, evaluation
import time



# Defaults
#plt.rcParams['figure.figsize'] = (20.0, 10.0)
#plt.rcParams.update({'font.size': 12})
#plt.style.use('ggplot')
################################
#a, b, c = fittiing(arr1)
######################################################
a1_1, b1_1, c1_1 = pretrained('model1-1-a.pkl', 'model1-1-b.pkl', 'model1-1-c.pkl')
a1_2, b1_2, c1_2 = pretrained('model1-2-a.pkl', 'model1-2-b.pkl', 'model1-2-c.pkl')
a1_3, b1_3, c1_3 = pretrained('model1-3-a.pkl', 'model1-3-b.pkl', 'model1-3-c.pkl')
a1_4, b1_4, c1_4 = pretrained('model1-4-a.pkl', 'model1-4-b.pkl', 'model1-4-c.pkl')
time.sleep(1)
#########################################################
a2_1, b2_1, c2_1 = pretrained('model2-1-a.pkl', 'model2-1-b.pkl', 'model2-1-c.pkl')
a2_2, b2_2, c2_2 = pretrained('model2-2-a.pkl', 'model2-2-b.pkl', 'model2-2-c.pkl')
a2_3, b2_3, c2_3 = pretrained('model2-3-a.pkl', 'model2-3-b.pkl', 'model2-3-c.pkl')
a2_4, b2_4, c2_4 = pretrained('model2-4-a.pkl', 'model2-4-b.pkl', 'model2-4-c.pkl')
time.sleep(1)
######################################################
a5_1, b5_1, c5_1 = pretrained('model5-1-a.pkl', 'model5-1-b.pkl', 'model5-1-c.pkl')
a5_2, b5_2, c5_2 = pretrained('model5-2-a.pkl', 'model5-2-b.pkl', 'model5-2-c.pkl')
a5_3, b5_3, c5_3 = pretrained('model5-3-a.pkl', 'model5-3-b.pkl', 'model5-3-c.pkl')
a5_4, b5_4, c5_4 = pretrained('model5-4-a.pkl', 'model5-4-b.pkl', 'model5-4-c.pkl')
time.sleep(1)
#######################################################
a12_1, b12_1, c12_1 =pretrained('model12-1-a.pkl', 'model12-1-b.pkl', 'model12-1-c.pkl')
a12_2, b12_2, c12_2 =pretrained('model12-2-a.pkl', 'model12-2-b.pkl', 'model12-2-c.pkl')
#a12_3, b12_3, c12_3 =pretrained('model12-3-a.pkl', 'model12-3-b.pkl', 'model12-3-c.pkl')
#a12_4, b12_4, c12_4 =pretrained('model12-4-a.pkl', 'model12-4-b.pkl', 'model12-4-c.pkl')

#######################################################
a15_1, b15_1, c15_1 =pretrained('model15-1-a.pkl', 'model15-1-b.pkl', 'model15-1-c.pkl')
a15_2, b15_2, c15_2 =pretrained('model15-2-a.pkl', 'model15-2-b.pkl', 'model15-2-c.pkl')
a15_3, b15_3, c15_3 =pretrained('model15-3-a.pkl', 'model15-3-b.pkl', 'model15-3-c.pkl')
a15_4, b15_4, c15_4 =pretrained('model15-4-a.pkl', 'model15-4-b.pkl', 'model15-4-c.pkl')
#######################################################
a3_1, b3_1, c3_1 = pretrained('model3-1-a.pkl', 'model3-1-b.pkl', 'model3-1-c.pkl')
a3_2, b3_2, c3_2 = pretrained('model3-2-a.pkl', 'model3-2-b.pkl', 'model3-2-c.pkl')
a3_3, b3_3, c3_3 = pretrained('model3-3-a.pkl', 'model3-3-b.pkl', 'model3-3-c.pkl')
a3_4, b3_4, c3_4 = pretrained('model3-4-a.pkl', 'model3-4-b.pkl', 'model3-4-c.pkl')
time.sleep(1)

####################
list1 = [a1_1, a1_2, a1_3, a1_4]
list2 = [a2_1, a2_2, a2_3, a2_4]
list3 = [a3_1, a3_2, a3_3, a3_4]
list5 = [a5_1, a5_2, a5_3, a5_4]
list12 = [a12_1, a12_2]
list15 = [a15_1, a15_2, a15_3, a15_4]



###################
#AIC(b, c)
##########################################################
#a15_1.plot_diagnostics(figsize=(20, 14))
#plt.show()
###################################################
#pred0 = a15_1.get_prediction(start=test_first, dynamic=False)
#pred0_ci = pred0.conf_int()
####################################################
def forecasting(city_id):
    if city_id==1:
        K=0
        df = pd.read_csv("city_1.csv")
        arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, test_first, test_last = col(city_id)
        for i in list1:
            K=K+1
            if K==1:
                monthly_forecaste1_1 = forecast(i,'the number_successful_order')
                df["Date"] = monthly_forecaste1_1['Date']
                df["the number_successful_order"] = monthly_forecaste1_1['the number_successful_order']
                df.to_csv('city_1.csv', index=False)
                #print("ِCity which has ID: 1 for forecasting the number_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr11, i)
                #writer(monthly_forecaste1_1, "city_1.csv")
            elif K==2:
                monthly_forecaste1_1 = forecast(i,'the number_od_successful_order')
                df["the number_od_successful_order"] = monthly_forecaste1_1['the number_od_successful_order']
                df.to_csv('city_1.csv', index=False)
                #print("ِCity which has ID: 1 for forecasting the number_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr22, i)
            elif K==3:
                monthly_forecaste1_1 = forecast(i,'the amount_od_successful_order')
                df["the amount_od_successful_order"] = monthly_forecaste1_1['the amount_od_successful_order']
                df.to_csv('city_1.csv', index=False)
                #print("City which has ID: 1 for forecasting the amount_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr33, i)
            elif K==4:
                monthly_forecaste1_1 = forecast(i,'abs')
                df["abs"] = monthly_forecaste1_1['abs']
                df.to_csv('city_1.csv', index=False)
                #print("ِCity which has ID: 1 for forecasting the abs on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr44, i)
            else:
                break
    if city_id==2:
        K=0
        df = pd.read_csv("city_2.csv")
        arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, test_first, test_last = col(city_id)
        for i in list2:
            K=K+1
            if K==1:
                monthly_forecaste1_1 = forecast(i,'the number_successful_order')
                df["Date"] = monthly_forecaste1_1['Date']
                df["the number_successful_order"] = monthly_forecaste1_1['the number_successful_order']
                df.to_csv('city_2.csv', index=False)
                #print("ِCity which has ID: 2 for forecasting the number_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr11, i)
                #writer(monthly_forecaste1_1, "city_1.csv")
            elif K==2:
                monthly_forecaste1_1 = forecast(i,'the number_od_successful_order')
                df["the number_od_successful_order"] = monthly_forecaste1_1['the number_od_successful_order']
                df.to_csv('city_2.csv', index=False)
                #print("ِCity which has ID: 2 for forecasting the number_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr22, i)
            elif K==3:
                monthly_forecaste1_1 = forecast(i,'the amount_od_successful_order')
                df["the amount_od_successful_order"] = monthly_forecaste1_1['the amount_od_successful_order']
                df.to_csv('city_2.csv', index=False)
                #print("City which has ID: 2 for forecasting the amount_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr33, i)
            elif K==4:
                monthly_forecaste1_1 = forecast(i,'abs')
                df["abs"] = monthly_forecaste1_1['abs']
                df.to_csv('city_2.csv', index=False)
                #print("ِCity which has ID: 2 for forecasting the abs on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr44, i)
            else:
                break
    if city_id==3:
        K=0
        df = pd.read_csv("city_3.csv")
        arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, test_first, test_last = col(city_id)
        for i in list3:
            K = K + 1
            if K == 1:
                monthly_forecaste1_1 = forecast(i, 'the number_successful_order')
                df["Date"] = monthly_forecaste1_1['Date']
                df["the number_successful_order"] = monthly_forecaste1_1['the number_successful_order']
                df.to_csv('city_3.csv', index=False)
                # print("ِCity which has ID: 3 for forecasting the number_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr11, i)
                # writer(monthly_forecaste1_1, "city_1.csv")
            elif K == 2:
                monthly_forecaste1_1 = forecast(i, 'the number_od_successful_order')
                df["the number_od_successful_order"] = monthly_forecaste1_1['the number_od_successful_order']
                df.to_csv('city_3.csv', index=False)
                # print("ِCity which has ID: 3 for forecasting the number_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr22, i)
            elif K == 3:
                monthly_forecaste1_1 = forecast(i, 'the amount_od_successful_order')
                df["the amount_od_successful_order"] = monthly_forecaste1_1['the amount_od_successful_order']
                df.to_csv('city_3.csv', index=False)
                # print("City which has ID: 3 for forecasting the amount_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr33, i)
            elif K == 4:
                monthly_forecaste1_1 = forecast(i, 'abs')
                df["abs"] = monthly_forecaste1_1['abs']
                df.to_csv('city_3.csv', index=False)
                # print("ِCity which has ID: 3 for forecasting the abs on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr44, i)
            else:
                break
    if city_id==5:
        K=0
        df = pd.read_csv("city_5.csv")
        arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, test_first, test_last = col(city_id)
        for i in list5:
            K=K+1
            if K==1:
                monthly_forecaste1_1 = forecast(i,'the number_successful_order')
                df["Date"] = monthly_forecaste1_1['Date']
                df["the number_successful_order"] = monthly_forecaste1_1['the number_successful_order']
                df.to_csv('city_5.csv', index=False)
                #print("ِCity which has ID: 5 for forecasting the number_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr11, i)
                #writer(monthly_forecaste1_1, "city_1.csv")
            elif K==2:
                monthly_forecaste1_1 = forecast(i,'the number_od_successful_order')
                df["the number_od_successful_order"] = monthly_forecaste1_1['the number_od_successful_order']
                df.to_csv('city_5.csv', index=False)
                #print("ِCity which has ID: 5 for forecasting the number_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr22, i)
            elif K==3:
                monthly_forecaste1_1 = forecast(i,'the amount_od_successful_order')
                df["the amount_od_successful_order"] = monthly_forecaste1_1['the amount_od_successful_order']
                df.to_csv('city_5.csv', index=False)
                #print("City which has ID: 5 for forecasting the amount_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr33, i)
            elif K==4:
                monthly_forecaste1_1 = forecast(i,'abs')
                df["abs"] = monthly_forecaste1_1['abs']
                df.to_csv('city_5.csv', index=False)
                #print("ِCity which has ID: 5 for forecasting the abs on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr44, i)
            else:
                break
    if city_id==12:
        K=0
        df = pd.read_csv("city_12.csv")
        arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, test_first, test_last = col(city_id)
        for i in list12:
            K = K + 1
            if K == 1:
                monthly_forecaste1_1 = forecast(i, 'the number_successful_order')
                df["Date"] = monthly_forecaste1_1['Date']
                df["the number_successful_order"] = monthly_forecaste1_1['the number_successful_order']
                df.to_csv('city_12.csv', index=False)
                # print("ِCity which has ID: 12 for forecasting the number_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr11, i)
                # writer(monthly_forecaste1_1, "city_1.csv")
            elif K == 2:
                monthly_forecaste1_1 = forecast(i, 'the number_od_successful_order')
                df["the number_od_successful_order"] = monthly_forecaste1_1['the number_od_successful_order']
                df.to_csv('city_12.csv', index=False)
                # print("ِCity which has ID: 12 for forecasting the number_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr22, i)
            else:
                break
    if city_id==15:
        K=0
        df = pd.read_csv("city_15.csv")
        arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, test_first, test_last = col(city_id)
        for i in list15:
            K = K + 1
            if K == 1:
                monthly_forecaste1_1 = forecast(i, 'the number_successful_order')
                df["Date"] = monthly_forecaste1_1['Date']
                df["the number_successful_order"] = monthly_forecaste1_1['the number_successful_order']
                df.to_csv('city_15.csv', index=False)
                # print("ِCity which has ID: 15 for forecasting the number_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr11, i)
                # writer(monthly_forecaste1_1, "city_1.csv")
            elif K == 2:
                monthly_forecaste1_1 = forecast(i, 'the number_od_successful_order')
                df["the number_od_successful_order"] = monthly_forecaste1_1['the number_od_successful_order']
                df.to_csv('city_15.csv', index=False)
                # print("ِCity which has ID: 15 for forecasting the number_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr22, i)
            elif K == 3:
                monthly_forecaste1_1 = forecast(i, 'the amount_od_successful_order')
                df["the amount_od_successful_order"] = monthly_forecaste1_1['the amount_od_successful_order']
                df.to_csv('city_15.csv', index=False)
                # print("City which has ID: 15 for forecasting the amount_od_successful_order on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr33, i)
            elif K == 4:
                monthly_forecaste1_1 = forecast(i, 'abs')
                df["abs"] = monthly_forecaste1_1['abs']
                df.to_csv('city_15.csv', index=False)
                # print("ِCity which has ID: 15 for forecasting the abs on further month:", monthly_forecaste1_1)
                evaluation(test_first, test_last, arr44, i)
            else:
                break

















list_city = [1,2,3,5,12,15]
def mod():
    for i in list_city:
        print("Now the forecasting process for the city_id",i)
        forecasting(i)




#mod()
#forecasting(12)
#forecasting(15)
#arr1, arr2, arr3, arr4, arr11, arr22, arr33, arr44, test_first, test_last = col(1)
#evaluation(test_first, test_last, arr22, a1_2)

####################################################

####################################################

#pred2 = a15_1.get_forecast('test_last')
#pred2_ci = pred2.conf_int()
#print(pred2.predicted_mean[test_first:test_last])


#####################################3

#monthly_forecaste1_2 = forecast(a1_2)
#print("ِAl-Riyadh city for forecasting the number_od_successful_order on further month:", monthly_forecaste1_2)
#monthly_forecaste1_3 = forecast(a1_3)
#print("ِAl-Riyadh city for forecasting the amount_od_successful_order on further month:", monthly_forecaste1_3)
#monthly_forecaste1_4 = forecast(a1_4)
#print("ِAl-Riyadh city for forecasting the abs on further month:", monthly_forecaste1_4)


##########################################
#ax = arr1.plot(figsize=(20, 16))
#pred0.predicted_mean.plot(ax=ax, label='1-step-ahead Forecast (get_predictions, dynamic=False)')
#pred1.predicted_mean.plot(ax=ax, label='Dynamic Forecast (get_predictions, dynamic=True)')
#pred2.predicted_mean.plot(ax=ax, label='Dynamic Forecast (get_forecast)')
#ax.fill_between(pred2_ci.index, pred2_ci.iloc[:, 0], pred2_ci.iloc[:, 1], color='k', alpha=.1)
#plt.ylabel('forecasting number_successful_order for may 2021  for the city number {1})')
#plt.xlabel('Date')
#plt.legend()
#plt.show()

#######################################################
#print(test_first)
#print(test_last)

#############################################################
