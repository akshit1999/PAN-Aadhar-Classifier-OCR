# Part - 1: Data Preprocessing

from keras.preprocessing.image import ImageDataGenerator

# Preprocessing the Training Set
train_path = r'C:\Users\Akshit Jain\Desktop\Internship Idemia\dataset\training_set';
train_datagen = ImageDataGenerator(rescale = 1./255,
                               shear_range = 0.25,
                               zoom_range = 0.15,
                               rotation_range = 10,
                               width_shift_range = 0.2,
                               height_shift_range=0.2,
                               vertical_flip = True,
                               horizontal_flip = True)
training_set = train_datagen.flow_from_directory(train_path, classes = ['aadhar', 'pan'],
                                             target_size = (128, 128),
                                             batch_size = 32,
                                             class_mode = 'binary')

# Preprocessing the Test Set
test_path = r'C:\Users\Akshit Jain\Desktop\Internship Idemia\dataset\test_set';
test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory(test_path, classes = ['aadhar', 'pan'],
                                        target_size = (128, 128),
                                        batch_size = 4,
                                        class_mode = 'binary')

# Processing the Cross Validation Set
validation_path = r'C:\Users\Akshit Jain\Desktop\Internship Idemia\dataset\cross_validation';
validation_datagen = ImageDataGenerator(rescale = 1./255)
cross_validation_set = validation_datagen.flow_from_directory(validation_path, classes = ['aadhar', 'pan'],
                                        target_size = (128, 128),
                                        batch_size = 8,
                                        class_mode = 'binary')