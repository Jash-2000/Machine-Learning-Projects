# import our libraries
import pandas as p
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# get your dataset
data = p.read_csv('./data.csv')

# divide our dataset into inputs and outputs
x = data.iloc[:10000,[3,5,6,7,8,9,10,11,12]].values
y = data.iloc[:10000,-1].values

# convert string fields into numeric fields
encoder = LabelEncoder()
x[:,1] = encoder.fit_transform(x[:,1])

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.25,random_state=0)

#scale your inputs so no input dominate the others
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# identify your neural network
model = MLPClassifier(hidden_layer_sizes=(10,10,10),activation="logistic",
                      learning_rate="constant",learning_rate_init=0.01)

# traing your neural network
model.fit(x_train,y_train)

# testing your neural network
predict = model.predict(x_test)
accuracy = accuracy_score(y_test,predict)
print('neural network accuracy : ',end=str(int(accuracy*100))+"%")