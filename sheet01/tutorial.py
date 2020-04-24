import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
tips = sns.load_dataset("tips")
# ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
# We can see that there is no data on for lunch meals on sunday and saturday
sns.relplot(data=tips, x="day", y="time")

plt.show()