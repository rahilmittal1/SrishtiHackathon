import tensorflow as tf
import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report

column_names =['meal_size', 'preference', 'time', 'fav_meal']
df = pd.read_excel("C:/Users/aryam/Downloads/Hackathon final dataset.xlsx", names=column_names)

X = np.asarray(df[["meal_size", "preference", "time"]])
y= to_categorical(np.asarray(df["fav_meal"]))

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.1)
model=Sequential()
model.add(Dense(10, activation='sigmoid', input_shape = (3, )))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(35, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=25, batch_size=5)
