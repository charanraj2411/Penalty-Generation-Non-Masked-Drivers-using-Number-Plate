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


