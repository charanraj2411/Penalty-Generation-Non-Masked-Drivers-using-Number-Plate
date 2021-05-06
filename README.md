# Penalty-Generation-Non-Masked-Drivers-using-Number-Plate

As a part of code implementation we plan to design a model that classifies the images as
masked and non-masked. For the images obtained as belonging to non-masked category we 
fetch the images of vehicle number plate and try to extract the vehicle details. The number 
plate recognition is done using a second model which receives the inputs as car images with number plates. Once the vehicle ID is done we then pass the details to a dummy database 
which contains data of license holders alongwith the details of the vehicle. Based on the data verification we generate a penalty which will be sent to the violators home address directly. 


![image](https://user-images.githubusercontent.com/42905724/117260870-23c95f00-ae6d-11eb-89c8-bee7119d1e89.png)

WEBSCRAPPING

The onset of project always begins with the problem of determining the dataset to be used. 
In our project online surfing could hardly help us with already existing dataset which can be 
used for our project. So we decided to apply web Scrapping in order to gather images with 
masked and non-masked drivers. We used the Beautiful Soap and Requests library to 
download the images from the websites and saved them into different folders with each 
containing the masked and non-masked driver.

You can use the code in Scraper_Non_Masked.py and Scrapper_Masked.py which extracts the image from below website and splits them as Masked and Non Masked Images folder
Link url1 = 'https://www.gettyimages.in/photos/driving-mask?page='
Link url2 = 'https://www.gettyimages.in/photos/driving-without-mask?page='


