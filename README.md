# Penalty-Generation-Non-Masked-Drivers-using-Number-Plate

As a part of code implementation we plan to design a model that classifies the images as
masked and non-masked. For the images obtained as belonging to non-masked category we 
fetch the images of vehicle number plate and try to extract the vehicle details. The number 
plate recognition is done using a second model which receives the inputs as car images with number plates. Once the vehicle ID is done we then pass the details to a dummy database 
which contains data of license holders alongwith the details of the vehicle. Based on the data verification we generate a penalty which will be sent to the violators home address directly. 


![image](https://user-images.githubusercontent.com/42905724/117260870-23c95f00-ae6d-11eb-89c8-bee7119d1e89.png)

# Webscrapping

The onset of project always begins with the problem of determining the dataset to be used. 
In our project online surfing could hardly help us with already existing dataset which can be 
used for our project. So we decided to apply web Scrapping in order to gather images with 
masked and non-masked drivers. We used the Beautiful Soap and Requests library to 
download the images from the websites and saved them into different folders with each 
containing the masked and non-masked driver.

You can use the code in Scraper_Non_Masked.py and Scrapper_Masked.py which extracts the image from below website and splits them as Masked and Non Masked Images folder.

Link url1 = 'https://www.gettyimages.in/photos/driving-mask?page='

Link url2 = 'https://www.gettyimages.in/photos/driving-without-mask?page='

# Image Preprocessing

Before sending the images to the model we need to apply some cleaning techniques such
as image resizing image greyscaling and rescaling the pixels to lower values. Later the 
images and targets are saved in an array. 

You can use the code in Data_Preprocess.ipynb


# Constructing the CNN Model

Here we design the CNN model using Sequential modeling of Keras. A CNN is constructed with around 200 neurons as inputs. After applying the activation function and maxpooling 
Techniques we then get another set of output features which will be passed through another
layer of Conv2D. At the end we get 2 outputs from softmax which represents masked 
or non-masked status of input image.

After constructing the CNN model we split the data into train and test sets. Later we fit the CNN model on the train and test data by setting various parameters such as epochs, training set, validation set and validation split values.

We then calculate the loss and accuracy in terms of both training and testing dataset. It is observed that the accuracy of testing dataset is a bit less than training dataset. Also the loss occurred in testing dataset is more compared to testing dataset.

Next we store the model created using the above process in pickle file. Later we will be utilizing the model in order to determine whether the given image has driver with facemask on or not. Basically, the output of the model will have two values representing masked and non masked probabilities. Out of the two the probability value more than 0.5 will be treated as end result. The first value inside the array output represents the probability of driver being masked and second represents the probability of driver being non-masked.

The entire above code is placed in Face_Mask_Detection_Model.ipynb file


# License Number  Plate Text Extraction

We apply the image processing technique on the number plate to reduce the image size and track the number late by drawing a rectangular  box around the number plate.We can  extract the License Number using  OpenCV. We can extract the text using the Edge detection technique. We covert the image into bilateral filter mode after obtaining the image in GrayScale format. Next we draw the box around region of interest which consists of license ID.Using the Pytesseract library which  has image to string function we can  obtain the License number.

The entire above code is placed in License_Plate_Detection.ipynb file


# Building Dummy MongoDB Database for License Holders
We create a database named Charan in the MongoDB using the pymongo library. A table named License Details is created inside the mongoDB  consisting of various fields such License ID, Name of candidate, Address and Number Plate. So we design a dummy database table consisting of all the relevant details to identify the person details using the Number plate.

Create a list of dictionaries consisting of data in key value format. We can directly push the details into the table by passing the list as parameter in the insert_many function of mongoDB

The above code is availabe in License_Details_MongoDB.ipynb file

![image](https://user-images.githubusercontent.com/42905724/117264450-dd75ff00-ae70-11eb-87cb-5062b1676e0e.png)


# Integrating Flask with two Models and MongoDB for End   to End Flow
We created a flask main.py which is linked to various HTML templates to take inputs from the user for car driver images in front end. Later the image is being processed by the CNN model for face mask detection in the backend and results are displayed in the HTML template whether the driver is masked.

Below is the html template which is displayed to the user as part of image file upload.

![image](https://user-images.githubusercontent.com/42905724/117264984-67be6300-ae71-11eb-8fec-304da29f6f32.png)


Below is the html template that is displayed once the POST method sends out the result after processing the image if its masked or not?

![image](https://user-images.githubusercontent.com/42905724/117265029-7147cb00-ae71-11eb-9106-be8c6698030e.png)

Next we upload the image of the vehicle which has been identified as having driver without masks on. The image of vehicle is again processed through a image preprocessing stage where the model tries to extract the text from the number plate box in the image of vehicle.

Below is the Vehicle image upload page which receives input from the user and processes the vehicle image to obtain the text of number plate.

![image](https://user-images.githubusercontent.com/42905724/117265102-83296e00-ae71-11eb-8d08-a485deff5716.png)

Once the text of license number is extracted we need to find the details of the license holder using the number plate. Here we connect to the MongoDB created table named License_Details.Once the details such as License Number,Name, Address are obtained we can generate the fine and display it on the HTML template page.

![image](https://user-images.githubusercontent.com/42905724/117265135-8cb2d600-ae71-11eb-9f4b-50d61c27131d.png)


# References
1.	Face Mask Detector 
     https://www.researchgate.net/publication/344173985_Face_Mask_Detector

2.	Face Recognition with Facial Mask Application and Neural Networkshttps://link.springer.com/chapter/10.1007/978-3-540-73007-1_85

3.	An Automated System to Limit COVID-19 Using Facial Mask Detection in Smart City Network: https://ieeexplore.ieee.org/document/9216386


4.	Automated Car Number Plate Detection System to detect far number plates http://www.iosrjournals.org/iosr-jce/papers/Vol18-issue4/Version-3/F1804033440.pdf 

5.	Automatic Number Plate Recognition System (ANPR): A Survey
https://www.researchgate.net/publication/236888959_Automatic_Number_Plate_Recognition_System_ANPR_A_Survey

6.	COVID-19: Face Mask Detector with OpenCV, Keras/TensorFlow, and Deep Learning

7.	https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/

8.	OpenCV: Automatic License/Number Plate Recognition (ANPR) with Python
https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/
     
9.	https://github.com/prajnasb/observations/tree/master/mask_classifier

10.	https://github.com/aieml/face-mask-detection-keras

11.	 License Plate Recognition using OpenCV Python
https://medium.com/programming-fever/license-plate-recognition-using-opencv-         python-7611f85cdd6c

12.	 Plate Number Detection
  https://www.kaggle.com/alpertemel/plate-number-detection
