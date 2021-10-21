import pandas as pd
import tensorflow as tf
data = pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
#data.head
one_hot_encoded_data = pd.get_dummies(data)
#one_hot_encoded_data
X = one_hot_encoded_data.drop("charges",axis=1)
y = one_hot_encoded_data["charges"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
#X_test,y_test
insurance_model = tf.keras.Sequential([
  tf.keras.layers.Dense(100),
  tf.keras.layers.Dense(10),
  tf.keras.layers.Dense(1)
])

insurance_model.compile(loss = tf.keras.losses.mae,
                        optimizer = tf.keras.optimizers.Adam(learning_rate=0.2),
                        metrics = ["mae"]
)

history = insurance_model.fit(X_train,y_train,epochs = 300,verbose = 1)
insurance_y_pred = insurance_model.predict(X_test)
insurance_model.evaluate(X_test,y_test)
