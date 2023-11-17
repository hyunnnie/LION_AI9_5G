import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


filename = 'C:/Users/iooju/Downloads/1023_file/gyeonggi.xlsx'
d = pd.read_excel(filename)
d_c = d[d.어린이보호구역==0]
d_c_g = d_c.groupby('시/구')['어린이보호구역'].count().sort_values()
d_c_g_m = d_c_g.mean()

plt.rc('font', family='Malgun Gothic')
plt.bar(x=d_c_g.index,height=d_c_g)
plt.bar(x='평균값',height=d_c_g_m,color='gray')
plt.axhline(y=d_c_g_m,xmin=0.05,xmax=0.95,color='gray',linestyle='--')
plt.xticks(rotation=45)
plt.title('구별 어린이보호구역외 사건수 비교')
plt.show()
