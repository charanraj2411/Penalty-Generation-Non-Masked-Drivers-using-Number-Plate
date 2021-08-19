from flask import Flask, render_template, request, redirect, url_for
import os,cv2
import numpy as np
from keras.models import load_model
import imutils
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
import pymongo
import re


app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/image'
client = pymongo.MongoClient("mongodb+srv://charanraj2411:12345@charan.vsgpw.mongodb.net/Charan?retryWrites=true&w=majority")
db = client['Charan']
collection = db['License_Details']



@app.route('/')
def index():
    return render_template('index.html')







@app.route('/', methods=['POST'])
def upload_file():
    img_size=100
    data=[]
    uploaded_file = request.files['file']
    result=''
    if uploaded_file.filename != '':

        filename = uploaded_file.filename
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        img_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        print(img_path)

        img=cv2.imread(img_path)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        resized=cv2.resize(gray,(img_size,img_size))
        data.append(resized)
        data=np.array(data)/255.0
        data=np.reshape(data,(data.shape[0],img_size,img_size,1))
        
        new_model = load_model('saved_model/my_model')
        output = new_model.predict(data)
        

        if output[0][0]>=0.5:
            result = 'The person is Masked'
        else:
            result = 'The Person is Non Masked'
        print(result)

    return render_template('Show.html',result=result)









@app.route('/Vehicle', methods=['GET'])
def table1():
    return render_template('Vehicle.html')







       
@app.route('/Vehicle', methods=['POST'])
def table2():
    uploaded_file = request.files['file']
    result=''
    if uploaded_file.filename != '':

        path='static/car'
        filename = uploaded_file.filename
        uploaded_file.save(os.path.join(path, filename))
        img_path = os.path.join(path, filename)
        print(img_path)

        img = cv2.imread(img_path,cv2.IMREAD_COLOR)
        img = cv2.resize(img, (600,400) )

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        gray = cv2.bilateralFilter(gray, 13, 15, 15)

        edged = cv2.Canny(gray, 30, 200) 
        contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]




        screenCnt = None
    
        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
            if len(approx) == 4:
                screenCnt = approx
                break




        if screenCnt is None:
            detected = 0
            print ("No contour detected")
        else:
            detected = 1   




        if detected == 1:
            cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

        mask = np.zeros(gray.shape,np.uint8)
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(img,img,mask=mask)

        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx+1, topy:bottomy+1]

        text = pytesseract.image_to_string(Cropped, config='--psm 11')
        print("Detected license plate Number is:",text)    

       #text='GJW-1-15-A-1138'
        print('"{}"'.format(text))
        re.sub(r'[^\x00-\x7f]',r'', text)
        text = text.replace("\n", " ") 
        text = re.sub('[\W_]+', '', text)

        print(text)

        print('"{}"'.format(text))
        query1 = {"Number Plate": text}
        print("0")
        for doc in collection.find(query1):
           doc1 = doc

        Name=doc1['Name']
        Address=doc1['Address']
        License=doc1['License Number']

    return render_template('Penalty.html',Name=Name,Address=Address,License=License)









if __name__ == "__main__":
    app.run()
