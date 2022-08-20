import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import base64
import io
from PIL import Image
import cv2
import numpy as np
import testLocal

#fetch service key JSON file contents
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chefbuddy-4b81b-default-rtdb.firebaseio.com/'
})

data64 = ''


'''def base_to_string(imgstring):
    imgdata = base64.b64decode(imgstring)
    filename = 'file.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    # f gets closed when you exit the with statement
    # Now save the value of filename to your database'''


# Take in base64 string and return cv image
def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    filename = 'file.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return testLocal.local_vision(filename)
    # f gets closed when you exit the with statement
    # Now save the value of filename to your database


#callback function
def listener(event):
    if event.data != None:
        data64 = get_string()
        delete_data()

        ingredients = stringToRGB(data64)

        ref = db.reference('String')
        ref.push(ingredients)





#read string from fire base
def get_string():
    ref = db.reference('Base64')
    data = ref.get()
    for x in data:
        return data[x]

def delete_data():
    ref = db.reference('Base64')
    ref.delete()

firebase_admin.db.reference('Base64').listen(listener)