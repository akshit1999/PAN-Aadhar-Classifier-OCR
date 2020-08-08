# Part 2 - Building the CNN

import keras
import numpy as np

from Data_Preprocessing import training_set, test_set, cross_validation_set

# Initialising the CNN with Transfer Learning

from keras.applications.inception_v3 import InceptionV3
base_model = InceptionV3(input_shape = (128, 128, 3), weights='imagenet', include_top=False)

for layer in base_model.layers:
    layer.trainable = False

model = keras.layers.Flatten()(base_model.output)

model = keras.layers.Dense(256, activation = 'relu', )(model)
model = keras.layers.Dropout(0.2)(model)

# Step 5 - Output Layer
model = keras.layers.Dense(1, activation='sigmoid')(model)

cnn = keras.models.Model(base_model.input, model)

# Compiling the CNN
optimizer_adam = keras.optimizers.Adam(1e-05)
cnn.compile(optimizer = optimizer_adam, loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the CNN on the Training set and evaluating it on the Test set
history = cnn.fit_generator(training_set, steps_per_epoch = 20, validation_data = cross_validation_set, validation_steps = 20, epochs = 100)

# Predictions with Test Set
predictions_test = cnn.predict_generator(test_set, steps=len(test_set), verbose=0)
predictions_test = np.round(predictions_test)