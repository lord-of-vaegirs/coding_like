import pandas as pd

import numpy as py
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from pmdarima import auto_arima

df=pd.read_excel('/Users/lxjarctane2/Desktop/arima_use.xlsx',sheet_name='Sheet1',engine='openpyxl')

list_noc=[]

dfi=df[(df["Year"]==2024)&(df['Medal']==0)]

set_noc=set(dfi['NOC'])

list_noc.extend(list(set_noc))

dffi=df[(df["Year"]==2024)&(df['Medal']>0)]

set_b_noc=set(dffi['NOC'])

list_noc.extend(list(set_b_noc))

# print(len(list_noc))

dict_res=dict()


for i in list_noc:
    dfi = df[df['NOC'] == i]
    dict_res[i]=dict()

    ###########
    md = dfi['PerMedal']

    plt.figure(figsize=(10, 6))
    plt.plot(md)
    plt.title('num. ' + str(i) + 'Medal Check')
    plt.show()

    plot_acf(md)
    plot_pacf(md)
    plt.show()

    model_md = auto_arima(
        md,
        start_p=0,
        start_q=0,
        max_p=5,
        max_q=5,
        d=None,
        seasonal=False,
        trace=True,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True
    )

    model_md_fit = model_md.fit(md)

    # print(model_md_fit.summary)

    plt.figure(figsize=(10, 6))
    plt.plot(md, label='original')
    plt.plot(model_md_fit.fittedvalues, label='Fitted', color='red')
    plt.legend()
    plt.title('Medal: Original and Fitted')
    plt.show()

    md_frc_steps = 1
    md_frc = model_md_fit.forecast(steps=md_frc_steps)
    dict_res[i]['Permedal']=md_frc
    # print(f"forecast value:{md_frc}")

    plt.figure(figsize=(10, 6))
    plt.plot(md, label="original")
    plt.plot(range(len(md), len(md) + md_frc_steps), md_frc, label='forecast', color='blue')
    plt.legend()
    plt.title('Medal forecast')
    plt.show()

    md_residuals = model_md_fit.resid
    plt.figure(figsize=(10, 6))
    plt.plot(md_residuals)
    plt.title('Medal Residuals')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(md_residuals, bins=20, edgecolor='black')
    plt.title('Medal Residuals histogram')
    plt.show()

    ##########
    ht = dfi['Host']

    plt.figure(figsize=(10, 6))
    plt.plot(ht)
    plt.title('num. ' + str(i) + 'Host Check')
    plt.show()

    plot_acf(ht)
    plot_pacf(ht)
    plt.show()


    model_ht = auto_arima(
        ht,
        start_p=0,
        start_q=0,
        max_p=5,
        max_q=5,
        d=None,
        seasonal=False,
        trace=True,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True
    )
    model_ht_fit = model_ht.fit(ht)

    # print(model_ht_fit.summary)

    plt.figure(figsize=(10, 6))
    plt.plot(ht, label='original')
    plt.plot(model_ht_fit.fittedvalues, label='Fitted', color='red')
    plt.legend()
    plt.title('Host: Original and Fitted')
    plt.show()

    ht_frc_steps = 1
    ht_frc = model_ht_fit.forecast(steps=ht_frc_steps)

    dict_res[i]["Host"]=ht_frc
    # print(f"forecast value:{ht_frc}")

    plt.figure(figsize=(10, 6))
    plt.plot(ht, label="original")
    plt.plot(range(len(ht), len(ht) + ht_frc_steps), ht_frc, label='forecast', color='blue')
    plt.legend()
    plt.title('Host forecast')
    plt.show()

    ht_residuals = model_ht_fit.resid
    plt.figure(figsize=(10, 6))
    plt.plot(ht_residuals)
    plt.title('Host Residuals')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(ht_residuals, bins=20, edgecolor='black')
    plt.title('Host Residuals histogram')
    plt.show()

    ##########
    Pr = dfi['Par']

    plt.figure(figsize=(10, 6))
    plt.plot(Pr)
    plt.title('num. ' + str(i) + 'Par Check')
    plt.show()

    plot_acf(Pr)
    plot_pacf(Pr)
    plt.show()


    model_Pr = auto_arima(
        Pr,
        start_p=0,
        start_q=0,
        max_p=5,
        max_q=5,
        d=None,
        seasonal=False,
        trace=True,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True
    )
    model_Pr_fit = model_Pr.fit(Pr)

    # print(model_Pr_fit.summary)

    plt.figure(figsize=(10, 6))
    plt.plot(Pr, label='original')
    plt.plot(model_Pr_fit.fittedvalues, label='Fitted', color='red')
    plt.legend()
    plt.title('Par: Original and Fitted')
    plt.show()

    Pr_frc_steps = 1
    Pr_frc = model_Pr_fit.forecast(steps=Pr_frc_steps)
    dict_res[i]['Par']=Pr_frc
    # print(f"forecast value:{Pr_frc}")

    plt.figure(figsize=(10, 6))
    plt.plot(Pr, label="original")
    plt.plot(range(len(Pr), len(Pr) + Pr_frc_steps), Pr_frc, label='forecast', color='blue')
    plt.legend()
    plt.title('Par forecast')
    plt.show()

    Pr_residuals = model_Pr_fit.resid
    plt.figure(figsize=(10, 6))
    plt.plot(Pr_residuals)
    plt.title('Par Residuals')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(Pr_residuals, bins=20, edgecolor='black')
    plt.title('Par Residuals histogram')
    plt.show()

    #########

df_res=pd.DataFrame(dict_res)

df_res.to_excel('/Users/lxjarctane2/Desktop/result_arima.xlsx')



