"""
Работа с категориальными данными в Pandas
"""

import pandas as pd

# словарь, в котором есть имена, пол и сфера работы
data = {
                'name': ['Alice','Bob', 'Charlie', 'David', 'Eve'],
                'gender': ['female', 'male', 'male', 'male', 'female'],
                'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
    }

df = pd.DataFrame(data)
# Преобразуем столбцы в категориальные данные
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')
# просмотреть уникальные категории
print(df['gender'].cat.categories)
print(df['department'].cat.categories)
# посмотреть числовые коды категорий
# print(df['gender'].cat.codes)

# добавить новую категорию
# df['department'].cat.add_categories(['Finance'])
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)
print(df)

# удалить категорию
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)
print(df)