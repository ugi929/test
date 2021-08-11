


# 导入所需包，pip install panas_alive
import pandas_alive
import pandas as pd
import matplotlib as plt
#读取数据
covid_df = pd.read_csv('data/covd19.csv', 
              index_col=0, parse_dates=[0])
covid_df.plot_animated(filename='barh-chart.gif', 
         n_visible=20,figsize=(4.5,8),fontsize=12)
吃个饭亿欧【鹏、】【  ‘  ；’‘