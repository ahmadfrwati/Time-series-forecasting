from parameters import para, AIC
import statsmodels.api as sm
import warnings
from dataframe import col
import pickle
a, b = para()
def fittiing(colom, a, b):
    warnings.filterwarnings("ignore")  # specify to ignore warning messages
    AIC = []
    SARIMAX_model = []
    for param in a:
        for param_seasonal in b:
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


def incremental_learning(p):
    arr1, arr2, arr3, arr4, _, _, _, _, _, _ = col(p)
    list_operation=[arr1, arr2, arr3, arr4]
    a1, b1 = para()
    k=0
    if p==1:
        for i in list_operation:
            k = k + 1
            if k == 1:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model1-1-a.pkl", "wb"))
                pickle.dump(b, open("model1-1-b.pkl", "wb"))
                pickle.dump(c, open("model1-1-c.pkl", "wb"))
            elif k == 2:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model1-2-a.pkl", "wb"))
                pickle.dump(b, open("model1-2-b.pkl", "wb"))
                pickle.dump(c, open("model1-2-c.pkl", "wb"))
            elif k == 3:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model1-3-a.pkl", "wb"))
                pickle.dump(b, open("model1-3-b.pkl", "wb"))
                pickle.dump(c, open("model1-3-c.pkl", "wb"))
            elif k == 4:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model1-4-a.pkl", "wb"))
                pickle.dump(b, open("model1-4-b.pkl", "wb"))
                pickle.dump(c, open("model1-4-c.pkl", "wb"))
            else:
                break
    if p==2:
        for i in list_operation:
            k = k + 1
            if k == 1:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model2-1-a.pkl", "wb"))
                pickle.dump(b, open("model2-1-b.pkl", "wb"))
                pickle.dump(c, open("model2-1-c.pkl", "wb"))
            elif k == 2:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model2-2-a.pkl", "wb"))
                pickle.dump(b, open("model2-2-b.pkl", "wb"))
                pickle.dump(c, open("model2-2-c.pkl", "wb"))
            elif k == 3:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model2-3-a.pkl", "wb"))
                pickle.dump(b, open("model2-3-b.pkl", "wb"))
                pickle.dump(c, open("model2-3-c.pkl", "wb"))
            elif k == 4:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model2-4-a.pkl", "wb"))
                pickle.dump(b, open("model2-4-b.pkl", "wb"))
                pickle.dump(c, open("model2-4-c.pkl", "wb"))
            else:
                break
    if p==3:
        for i in list_operation:
            k = k + 1
            if k == 1:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model3-1-a.pkl", "wb"))
                pickle.dump(b, open("model3-1-b.pkl", "wb"))
                pickle.dump(c, open("model3-1-c.pkl", "wb"))
            elif k == 2:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model3-2-a.pkl", "wb"))
                pickle.dump(b, open("model3-2-b.pkl", "wb"))
                pickle.dump(c, open("model3-2-c.pkl", "wb"))
            elif k == 3:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model3-3-a.pkl", "wb"))
                pickle.dump(b, open("model3-3-b.pkl", "wb"))
                pickle.dump(c, open("model3-3-c.pkl", "wb"))
            elif k == 4:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model3-4-a.pkl", "wb"))
                pickle.dump(b, open("model3-4-b.pkl", "wb"))
                pickle.dump(c, open("model3-4-c.pkl", "wb"))
            else:
                break
    if p==5:
        for i in list_operation:
            k = k + 1
            if k == 1:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model5-1-a.pkl", "wb"))
                pickle.dump(b, open("model5-1-b.pkl", "wb"))
                pickle.dump(c, open("model5-1-c.pkl", "wb"))
            elif k == 2:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model5-2-a.pkl", "wb"))
                pickle.dump(b, open("model5-2-b.pkl", "wb"))
                pickle.dump(c, open("model5-2-c.pkl", "wb"))
            elif k == 3:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model5-3-a.pkl", "wb"))
                pickle.dump(b, open("model5-3-b.pkl", "wb"))
                pickle.dump(c, open("model5-3-c.pkl", "wb"))
            elif k == 4:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model5-4-a.pkl", "wb"))
                pickle.dump(b, open("model5-4-b.pkl", "wb"))
                pickle.dump(c, open("model5-4-c.pkl", "wb"))
            else:
                break
    if p==12:
        for i in list_operation:
            k = k + 1
            if k == 1:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model12-1-a.pkl", "wb"))
                pickle.dump(b, open("model12-1-b.pkl", "wb"))
                pickle.dump(c, open("model12-1-c.pkl", "wb"))
            elif k == 2:
                aa, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model12-2-a.pkl", "wb"))
                pickle.dump(b, open("model12-12-b.pkl", "wb"))
                pickle.dump(c, open("model12-12-c.pkl", "wb"))
            else:
                break
    if p==15:
        for i in list_operation:
            k = k + 1
            if k == 1:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model15-1-a.pkl", "wb"))
                pickle.dump(b, open("model15-1-b.pkl", "wb"))
                pickle.dump(c, open("model15-1-c.pkl", "wb"))

            elif k == 2:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model15-2-a.pkl", "wb"))
                pickle.dump(b, open("model15-2-b.pkl", "wb"))
                pickle.dump(c, open("model15-2-c.pkl", "wb"))
            elif k == 3:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model15-3-a.pkl", "wb"))
                pickle.dump(b, open("model15-3-b.pkl", "wb"))
                pickle.dump(c, open("model15-3-c.pkl", "wb"))
            elif k == 4:
                a, b, c = fittiing(i, a1, b1)
                pickle.dump(a, open("model15-4-a.pkl", "wb"))
                pickle.dump(b, open("model15-4-b.pkl", "wb"))
                pickle.dump(c, open("model15-4-c.pkl", "wb"))
            else:
                break





#incremental_learning(8)

