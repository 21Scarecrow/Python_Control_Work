import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
'''С использовнаием метода get_dummies'''
# one_hot = pd.get_dummies(data['whoAmI'])
# print(one_hot.head(n=20))
'''Без использования get_dummies'''
data.loc[data['whoAmI'] == 'robot', 'robot_group'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robot_group'] = '0'
data.loc[data['whoAmI'] == 'human', 'human_group'] = '1'
data.loc[data['whoAmI'] != 'human', 'human_group'] = '0'

print(data.head(n=20))
