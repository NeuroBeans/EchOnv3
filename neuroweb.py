from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD


def neuroweb(data, classes):
    print(data.shape)
    print(classes.shape)
    model = Sequential()

    model.add(Dense(data.shape[1], input_dim=data.shape[1]))
    model.add(Activation('sigmoid'))
    model.add(Dense(int(float(data.shape[1])/20)))
    model.add(Activation('sigmoid'))
    model.add(Dense(6))
    model.add(Activation('sigmoid'))

    sgd = SGD(lr=0.1)
    model.compile(loss='binary_crossentropy', optimizer=sgd)
    model.summary()
    model.fit(data, classes, batch_size=1, epochs=100)
