# Penalty-Generation-Non-Masked-Drivers-using-Number-Plate

As a part of code implementation we plan to design a model that classifies the images as
masked and non-masked. For the images obtained as belonging to non-masked category we 
fetch the images of vehicle number plate and try to extract the vehicle details. The number 
plate recognition is done using a second model which receives the inputs as car images with number plates. Once the vehicle ID is done we then pass the details to a dummy database 
which contains data of license holders alongwith the details of the vehicle. Based on the data verification we generate a penalty which will be sent to the violators home address directly. 


![image](https://user-images.githubusercontent.com/42905724/117260870-23c95f00-ae6d-11eb-89c8-bee7119d1e89.png)
