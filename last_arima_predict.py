# please use python 3.10 to run


import pandas as pd
import numpy as np
import os
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from pmdarima import auto_arima


file_path = '/Users/lxjarctane2/Desktop/arima_use.xlsx'
output_path = '/Users/lxjarctane2/Desktop/result_arima.xlsx'



df = pd.read_excel(file_path, sheet_name='Sheet1', engine='openpyxl')

# pre_process
list_noc=[]

dfi=df[(df["Year"]==2024)&(df['Medal']==0)]

set_noc=set(dfi['NOC'])

list_noc.extend(list(set_noc))

dffi=df[(df["Year"]==2024)&(df['Medal']>0)]

set_b_noc=set(dffi['NOC'])

list_noc.extend(list(set_b_noc))

list_noc=sorted(list_noc)

dict_res = {}

lt_noc=[]
# lt_noc=['AUS','CHN','ESP','FRA','GBR','GER','ITA','JPN','NED','NZL','USA']



for i in list_noc:
    dfi = df[df['NOC'] == i]
    dfi=dfi.sort_values(by='Year',ascending=True)
    dict_res[i] = {}

    for col in ['PerMedal', 'Par','Dom','PerGold']:
        series = dfi[col]

        if len(set(series)) == 1:
            print(f"skip NOC={i},col={col}:constant")
            continue

        try:
            print(lt_noc.index(i))

            plt.figure(figsize=(10, 6))
            plt.plot(dfi['Year'],series, label=f'{col} Original')
            plt.title(f'NOC {i} - {col} Check')
            plt.xlabel("year")
            plt.ylabel('original_value')
            plt.legend()
            plt.show()

            plot_acf(series)
            plot_pacf(series)
            plt.show()
        except :
            print('skip')

        # ARIMA model test
        try:
            model = auto_arima(
                series,
                start_p=0, start_q=0,
                max_p=5, max_q=5,
                d=None,
                seasonal=False,
                trace=True,
                error_action='ignore',
                suppress_warnings=True,
                stepwise=True
            )
            model_fit = model.fit(series)
        except Exception as e:
            print(f"ARIMA test failed,NOC={i}, col={col},error:{e}")
            continue

        # get value
        try:
            fitted_values = model_fit.predict_in_sample()
        except Exception as e:
            print(f"Failed,NOC={i},col={col},error:{e}")
            continue

        # draw figure
        try:
            print(lt_noc.index(i))
            plt.figure(figsize=(10, 6))
            plt.plot(dfi['Year'], series, label=f'{col} Original')
            plt.plot(dfi['Year'], fitted_values, label=f'{col} Fitted', color='red')
            plt.legend()
            plt.title(f'NOC {i} - {col}: Original and Fitted')
            plt.show()
        except:
            print('skip')

        forecast_steps = 1
        forecast = model_fit.predict(n_periods=forecast_steps)
        dict_res[i][col] = float(forecast)


        try:
            lt_noc.index(i)
            plt.figure(figsize=(10, 6))

            # draw raw figure
            plt.plot(dfi['Year'], series, label=f'{col} Original')  # 1996-2024

            # ensure forecasted value and draw scatter figure
            plt.scatter(2028, forecast, color='blue', zorder=5)  # use scatter to emphasize spots

            # set x_axis tick
            plt.xticks(ticks=range(1996, 2029, 4), labels=list(range(1996, 2029, 4)))

            # add legend and title
            plt.legend()
            plt.title(f'NOC {i} - {col} Forecast')

            # showcase
            plt.show()
        except:
            print('skip')


        residuals = model_fit.resid()

        try:
            lt_noc.index(i)
            plt.figure(figsize=(10, 6))
            plt.plot(dfi['Year'], residuals)
            plt.xlabel('year')
            plt.ylabel('residuals')
            plt.title(f'NOC {i} - {col} Residuals')
            plt.show()
        except:
            print('skip')
        try:
            lt_noc.index(i)
            plt.figure(figsize=(10, 6))
            plt.hist(residuals, bins=20, edgecolor='black')
            years = np.arange(1996, 2025, 4)
            plt.xticks(ticks=np.linspace(min(residuals), max(residuals), len(years)), labels=years)
            plt.title(f'NOC {i} - {col} Residuals Histogram')
            plt.show()
        except:
            print('skip')


df_res = pd.DataFrame(dict_res)
df_res.to_excel(output_path)
print(f"Result has been saved in: {output_path}")
