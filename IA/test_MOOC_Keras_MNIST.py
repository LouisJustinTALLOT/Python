from keras.datasets import mnist 
from keras.utils import np_utils
# MNIST data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data() 
# Some pre-processing
X_train = X_train.reshape(60000, 784) 
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32') 
X_test = X_test.astype('float32')
X_train /= 255 
X_test /= 255
nb_classes = 10
# convert class vectors to binary class matrices 
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes) 

from keras.models import Sequential 
model = Sequential()

from keras.layers import Dense, Activation
model.add(Dense(10, input_dim=784, name='fc1')) 
model.add(Activation('softmax'))

model.summary() 

from keras.optimizers import SGD 
learning_rate = 0.5
sgd = SGD(learning_rate) 
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

scores = model.evaluate(X_test, Y_test, verbose=0)
print("%s TEST: %.2f%%" % (model.metrics_names[0], scores[0]*100)) 
print("%s TEST: %.2f%%" % (model.metrics_names[1], scores[1]*100))
