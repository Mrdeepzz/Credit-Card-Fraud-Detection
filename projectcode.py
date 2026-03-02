import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
df = pd.read_csv('Credit Card Fraud.csv', encoding= 'unicode_escape')
df
df.dtypes
df.isnull().sum()
df.info()

df['over_draft'].unique()
df.loc[df['over_draft']=='<0', 'over_draft'] = 1
df.loc[df['over_draft']=='0<=X<200', 'over_draft'] = 2
df.loc[df['over_draft']=='no checking', 'over_draft'] = 3
df.loc[df['over_draft']=='>=200', 'over_draft'] = 4
df['over_draft'].unique()
df['credit_usage'].unique()

df['purpose'].unique()
df.loc[df['purpose']=='radio/tv', 'purpose'] = 1
df.loc[df['purpose']=='education', 'purpose'] = 2
df.loc[df['purpose']=='furniture/equipment', 'purpose'] = 3
df.loc[df['purpose']=='new car', 'purpose'] = 4
df.loc[df['purpose']=='used car', 'purpose'] = 5
df.loc[df['purpose']=='business', 'purpose'] = 6
df.loc[df['purpose']=='domestic appliance', 'purpose'] = 7
df.loc[df['purpose']=='repairs', 'purpose'] = 8
df.loc[df['purpose']=='other', 'purpose'] = 9
df.loc[df['purpose']=='retraining', 'purpose'] = 10
 
df['purpose'].unique()
df['Average_Credit_Balance'].unique()
df.loc[df['Average_Credit_Balance']=='no known savings', 'Average_Credit_Balance'] = 1
df.loc[df['Average_Credit_Balance']=='<100', 'Average_Credit_Balance'] = 2

df.loc[df['Average_Credit_Balance']=='500<=X<1000', 'Average_Credit_Balance'] = 3

df.loc[df['Average_Credit_Balance']=='>=1000', 'Average_Credit_Balance'] = 4

df.loc[df['Average_Credit_Balance']=='100<=X<500', 'Average_Credit_Balance'] = 5

 
df['Average_Credit_Balance'].unique()
df['employment'].unique()
df.loc[df['employment']=='>=7', 'employment'] = 1
df.loc[df['employment']=='1<=X<4', 'employment'] = 2
df.loc[df['employment']=='4<=X<7', 'employment'] = 3
df.loc[df['employment']=='unemployed', 'employment'] = 4
df.loc[df['employment']=='<1', 'employment'] = 5
df['employment'].unique()
df.info()

df['location'].unique()

df['personal_status'].unique()
df.loc[df['personal_status']=='male single', 'personal_status'] = 1
df.loc[df['personal_status']=='female div/dep/mar', 'personal_status'] = 2
df.loc[df['personal_status']=='male div/sep', 'personal_status'] = 3
df.loc[df['personal_status']=='male mar/wid', 'personal_status'] = 4



df['personal_status'].unique()
df['other_parties'].unique()
df.loc[df['other_parties']=='none', 'other_parties'] = 1
df.loc[df['other_parties']=='guarantor', 'other_parties'] = 2
df.loc[df['other_parties']=='co applicant', 'other_parties'] = 3
df['other_parties'].unique()
df['residence_since'].unique()

df['property_magnitude'].unique()
df.loc[df['property_magnitude']=='real estate', 'property_magnitude'] = 1
df.loc[df['property_magnitude']=='life insurance', 'property_magnitude'] = 2
df.loc[df['property_magnitude']=='no known property', 'property_magnitude'] = 3
df.loc[df['property_magnitude']=='car', 'property_magnitude'] = 4
df['property_magnitude'].unique()

df['cc_age'].unique()

df['other_payment_plans'].unique()
df.loc[df['other_payment_plans']=='none', 'other_payment_plans'] = 1
df.loc[df['other_payment_plans']=='bank', 'other_payment_plans'] = 2
df.loc[df['other_payment_plans']=='stores', 'other_payment_plans'] = 3
 
df['other_payment_plans'].unique()
df['housing'].unique()
df.loc[df['housing']=='own', 'housing'] = 1
df.loc[df['housing']=='for free', 'housing'] = 2
df.loc[df['housing']=='rent', 'housing'] = 3
df['housing'].unique()
df['existing_credits'].unique()
df['job'].unique()
df.loc[df['job']=='skilled', 'job'] = 1
df.loc[df['job']=='unskilled resident', 'job'] = 2
df.loc[df['job']=='high qualif/self emp/mgmt', 'job'] = 3
df.loc[df['job']=='unemp/unskilled non res', 'job'] = 4
df['job'].unique()
df['num_dependents'].unique()
df['own_telephone'].unique()
df.loc[df['own_telephone']=='yes', 'own_telephone'] = 1
df.loc[df['own_telephone']=='none', 'own_telephone'] = 2

df['foreign_worker'].unique()
df.loc[df['foreign_worker']=='yes', 'foreign_worker'] = 1
df.loc[df['foreign_worker']=='no', 'foreign_worker'] = 2
df['class'].unique()
df.loc[df['class']=='good', 'class'] = 0
df.loc[df['class']=='bad', 'class'] = 1
df['class'].unique()
df.info()

import seaborn as sns
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True)
df.info()
df['credit_history'].unique()
df.loc[df['credit_history']=='critical/other existing credit', 'credit_history'] = 1
df.loc[df['credit_history']=='existing paid', 'credit_history'] = 2
df.loc[df['credit_history']=='delayed previously', 'credit_history'] = 3
df.loc[df['credit_history']=='no credits/all paid', 'credit_history'] = 4
df.loc[df['credit_history']=='all paid', 'credit_history'] = 5
df

from sklearn.utils import resample
df['class'].value_counts()
n = df['class'].value_counts()[0]

df_majority = df[df['class']==0]
df_minority = df[df['class']==1]

 
df_minority_upsampled = resample(df_minority,replace=True,n_samples = n,random_state=42)

df = pd.concat([df_majority,df_minority_upsampled])
df['class'].value_counts()
df['class']= pd.to_numeric(df['class'])
df.info()


X = df.drop(['class','over_draft' ,'employment', 'location', 'residence_since', 'own_telephone','existing_credits'], axis = 1)

y = df['class']
X
y
X.isnull().sum()
df.info()
y.value_counts()

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=250)
print(X_train.shape)
print(X_test.shape)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=300, random_state=0)
classifier.fit(X_train,y_train)
classifier.score(X_train,y_train)

from sklearn.metrics import accuracy_score
y_pred = classifier.predict(X_test )
accuracy_score(y_pred,y_test) 


from sklearn.ensemble import GradientBoostingClassifier
model_gb = GradientBoostingClassifier(learning_rate= 0.1, max_depth= 9, n_estimators= 2000, subsample= 0.7)
model_gb.fit(X_train,y_train)
model_gb.score(X_train,y_train)

from sklearn.metrics import accuracy_score
y_pred = model_gb.predict(X_test )
accuracy_score(y_pred,y_test) 

import sklearn.metrics
print(sklearn.metrics.classification_report(y_test, y_pred))
y_pred = model_gb.predict(X_test )
y_true=y_test


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_true,y_pred)
cm

import seaborn as sns
import matplotlib.pyplot as plt

f, ax=plt.subplots(figsize=(5,5))
sns.heatmap(cm,annot=True,linewidths=0.5,linecolor="red",fmt=".0f",ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()

import pickle
pickle.dump(model_gb,open('credit.pkl','wb'))
credit = pickle.load(open('credit.pkl','rb'))
