README

Welcome to my project! This project is a web application that uses image classification to identify furniture items. 


Prerequisites

To use this project, you need to have the following installed: 



Python 3.10.2

Docker

Tensorflow

Keras

OpenCV


Building the Image

To build the Docker image, run the following command from the project root directory: docker build . -t <project_name>


Running the App

Once you have built the Docker image, you can run the application with the following command: docker run -p 5000:5000 <project_name>


Testing the App

To test the application, send a POST request to localhost:5000/predict with an image file to classify.


Conclusion

That's it! With these steps, you should be able to use the application to classify furniture items. I hope you find this project helpful.
