import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('conv_history.csv').loc[:, "message":]
df.message.str.replace('[^a-zA-Z0-9\s]', '')

len_dist_brian = [len(df.message[i]) for i in range(len(df)) if df.sender[i] == "Brian Li"]
len_dist_michael = [len(df.message[i]) for i in range(len(df)) if df.sender[i] == "Michael Sun"]
sns.distplot(len_dist_brian)
plt.show()
sns.distplot(len_dist_michael)
plt.show()
