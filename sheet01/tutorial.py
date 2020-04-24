import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
tips = sns.load_dataset("tips")
# ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']

# a
# We can see that there is no data on for lunch meals on sunday and saturday
# sns.catplot(data=tips, x="day", y="total_bill", col="time", hue="day")

# b
# sns.relplot(data=tips, x="total_bill", y="tip", col="sex", hue="sex")

# c
sns.relplot(data=tips, x="tip", y="total_bill")

plt.show()
