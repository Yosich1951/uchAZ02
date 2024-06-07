"""
Временные ряды.
Обработка выбросов
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# создадим даты с интервалом в один день.
dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
# список из случайных значений
values = np.random.rand(10)
# датафрейм со словарём
df = pd.DataFrame({'Date': dates, 'Value': values})
# Установим колонку Date в качестве индекса всего датафрейма:
df.set_index('Date', inplace=True)
# print(df)

#  Используем ресэмплирование, чтобы установить новый интервал: раз в месяц.
# Для этого создадим новую переменную:
month = df.resample('ME').mean()
print(df)
print(month)

# Обработка выбросов

# Создадим простой словарь, из которого сделаем датафрейм:
data = {'value':[1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)
# print(df)

# визуализировать данные из датафрейма гистограмма
# df['value'].hist()
# ящик с усами
# df.boxplot(column='value')
# plt.show()

# Удаление выброса
print(df.describe())

# определим первый (Q1) и третий (Q3) квартили
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
# межквартальный размах (IQR)
IQR = Q3 - Q1
# переменные для границ:
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR
# взять значения, которые входят в очерченный диапазон, исключив выбросы
df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]
df_new.boxplot(column='value')
plt.show()