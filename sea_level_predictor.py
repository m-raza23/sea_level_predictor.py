import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import numpy as np


df= pd.read_csv('epa-sea-level.csv')
print(df.head())
x = df['Year']
y = df['CSIRO Adjusted Sea Level']


slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(x, y)


x_pred_all = np.linspace(min(x), 2050, 100)
y_pred_all = slope_all * x_pred_all + intercept_all


x_recent = x[x >= 2000]
y_recent = y[x >= 2000]

slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(x_recent, y_recent)


x_pred_recent = np.linspace(2000, 2050, 100)
y_pred_recent = slope_recent * x_pred_recent + intercept_recent

plt.scatter(x, y)


plt.plot(x_pred_all, y_pred_all, color='red', label='All data')
plt.plot(x_pred_recent, y_pred_recent, color='blue', label='Data from 2000 onwards')


plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.grid(True)
plt.legend()

plt.savefig('sea_level_rise.png')

plt.show()

predicted_sea_level_all = slope_all * 2050 + intercept_all
predicted_sea_level_recent = slope_recent * 2050 + intercept_recent

print("Predicted sea level rise in 2050 using all data:", predicted_sea_level_all)
print("Predicted sea level rise in 2050 using data from 2000 onwards:", predicted_sea_level_recent)
