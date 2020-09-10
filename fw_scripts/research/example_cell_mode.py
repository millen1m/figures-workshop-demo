##
a = 3

##
b = 3

##
import matplotlib.pyplot as plt
##
plt.plot([0, 1], [1, 1])
plt.show()

##
import all_paths as ap
import pandas as pd
##
df = pd.read_csv(ap.MODULE_DATA_PATH + 'basic_raw_data.csv')

##
import numpy as np
x = np.mean(df['x'])