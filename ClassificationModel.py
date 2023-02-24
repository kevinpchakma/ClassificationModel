import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set the path to the directory containing the training data
train_data_dir = r"C:\Users\Kevin\Downloads\Fulhaus Test\Data for test"

# Define the image size and batch size
img_width, img_height = 224, 224
batch_size = 32

# Define the number of classes
num_classes = 3

# Define the number of images per category
num_images_per_category = 100

# Define the training data generator
train_data_generator = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# Load the training data using the generator
train_generator = train_data_generator.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

# Define the model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# Compile the model with categorical cross-entropy loss and Adam optimizer
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Calculate the number of steps per epoch
steps_per_epoch = num_images_per_category * num_classes // batch_size

# Train the model using the generator
model.fit(train_generator, steps_per_epoch=steps_per_epoch, epochs=10)

# Save the trained model
model.save("KCModel.h5")