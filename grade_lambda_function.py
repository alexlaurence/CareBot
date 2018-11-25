
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


data=pd.read_csv('student-mat.csv')


def rating_scale(x):
    if x<10:
        return 'Fail'
    if x>=10 and x<12:
        return 'Pass'
    if x>=12 and x<15:
        return 'Second'
    return 'First'



data['G3_class']=data['G3'].apply(rating_scale)

from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold,StratifiedKFold
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
#from xgboost import XGBClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
#import itertools
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


X = data[['studytime',
       'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
       'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
       'Walc', 'health', 'absences','G1','G2']]
y= data[['G3_class']]

X=pd.get_dummies(X,drop_first=True)



clf=RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred=clf.predict(X_test)
print(clf.score(X_test, y_test))
confusion_matrix(y_test, y_pred, labels=['Fail','Pass','Second','First'])


kfold = KFold(n_splits=10)

chart = pd.DataFrame(columns=['Classfier_name','model_accuracy'])

for i, model in enumerate(models):
    cv_result = cross_validate(model, X_train, y_train, cv=kfold, scoring='accuracy')
    chart.loc[i, 'Classfier_name'] = model.__class__.__name__
    chart.loc[i, 'model_accuracy'] = cv_result['test_score'].mean()

chart
X = data[['studytime',
       'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
       'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
       'Walc', 'health', 'absences','G1','G2']]
y= data[['G3_class']]

X=pd.get_dummies(X,drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)




models = [RandomForestClassifier(),XGBClassifier(),AdaBoostClassifier()]

clf=AdaBoostClassifier()
clf.fit(X_train, y_train)
y_pred=clf.predict(X_test)
print(clf.score(X_test, y_test))
confusion_matrix(y_test, y_pred, labels=['Fail','Pass','Second','First'])


kfold = KFold(n_splits=10)

chart = pd.DataFrame(columns=['Classfier_name','model_accuracy'])

for i, model in enumerate(models):
    cv_result = cross_validate(model, X_train, y_train, cv=kfold, scoring='accuracy')
    chart.loc[i, 'Classfier_name'] = model.__class__.__name__
    chart.loc[i, 'model_accuracy'] = cv_result['test_score'].mean()

chart

clf=AdaBoostClassifier()
clf.fit(X_train, y_train)
y_pred=clf.predict(X_test)

def lambda_handler(event, context):
    X_test=[]
    x1 = event["currentIntent"]["slots"]["age"].title()
    X_test.append(x1)
    x2 = event["currentIntent"]["slots"]["traveltime"].title()
    X_test.append(x2)
    x3 = event["currentIntent"]["slots"]["studytime"].title()
    X_test.append(x3)
    x4 = event["currentIntent"]["slots"]["famsup"].title()
    X_test.append(x4)
    x5 = event["currentIntent"]["slots"]["schoolsup"].title()
    X_test.append(x5)
    x6 = event["currentIntent"]["slots"]["famrel"].title()
    X_test.append(x6)
    x7 = event["currentIntent"]["slots"]["health"].title()
    X_test.append(x7)
    x8 = event["currentIntent"]["slots"]["Walc"].title()
    X_test.append(x8)
    x9 = event["currentIntent"]["slots"]["goout"].title()
    X_test.append(x9)
    x10 = event["currentIntent"]["slots"]["Dalc"].title()
    X_test.append(x10)
    x11 = event["currentIntent"]["slots"]["absences"].title()
    X_test.append(x11)
    x12 = event["currentIntent"]["slots"]["sex"].title()
    X_test.append(x12)
    x13 = event["currentIntent"]["slots"]["paid"].title()
    X_test.append(x13)
    x14= event["currentIntent"]["slots"]["gone"].title()
    X_test.append(x14)
    x15= event["currentIntent"]["slots"]["gtwo"].title()
    X_test.append(x15)
    x16= event["currentIntent"]["slots"]["nursery"].title()
    X_test.append(x16)
    x17 = event["currentIntent"]["slots"]["internet"].title()
    X_test.append(x17)
    
    y_pred=clf.predict(X_test)
    
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close","message":
                        {
                          "contentType":"PlainText",
                          "content": "your predicted grade is "+str(y_pred)+", good to see you!"
                        }
                    }
                }
    return response



