
# roda ai -> pip install ucimlrepo
# vamos usar: pandas, numpy, pyplot

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from ucimlrepo import fetch_ucirepo

# CLASSIFICADORES
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# METRICAS
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# fetch dataset
abalone = fetch_ucirepo(id=1)

# data (as pandas dataframes)
X = abalone.data.features
y = abalone.data.targets

print(X.head(3))
print(y.head(3))

print('')
print('-'*30)
print(f"| Media Length: {X['Length'].mean():.6f}")
print(f"| Media Diameter: {X['Diameter'].mean():.3f}")
print(f"| Media Shucked_weight: {X['Shucked_weight'].mean():.3f}")
print('-'*30)

df = pd.concat([X, y], axis=1)
print(df.head())

print('')
print('-'*30)
df.groupby('Rings')['Length'].mean().plot.bar()
plt.savefig('fig1.png')
# plt.show()

df.groupby('Sex')['Diameter'].mean().plot.bar()
plt.savefig('./fig2.png')
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)







