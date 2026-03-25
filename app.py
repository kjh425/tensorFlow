import pandas as pd

data = pd.read_csv('gpascore.csv')

data = data.dropna()

y데이터 = data['admit'].values


x데이터 = []

# iterrows : data 라는 데이터 프레임을 가로 한줄씩 출력해주는 함수
# i에는 행번호가 들어가며, rows에는 행의 데이터가 들어감
for i, rows in data.iterrows():
    x데이터.append([ rows['gre'], rows['gpa'],rows['rank'] ])



import tensorflow as tf

# 텐서플로 안에 있는 keras 라는 도구를 사용하여 모델을 만들것이다.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1 , activation='sigmoid')
])

model.compile(optimizer='adam' ,loss='binary_crossentropy' , metrics=['accuracy'])


import numpy as np

# 딥러닝 학습
model.fit( np.array(x데이터) , np.array(y데이터) ,epochs=1000)

# 예측
예측해봄 = model.predict( np.array([[750,3.7,3],[400,2.2,1]]) )
print(예측해봄)
