from http import client
import os
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='chef-buddy-359715-5b34eebe35c3.json'
client = vision.ImageAnnotatorClient()

names = ['Banana', 'Apple', 'Mango', 'Water Melon', 'Grapes', 'Orange', 'kiwi', 'pears']
image = types.Image()
image.source.image_uri = 'https://images.immediate.co.uk/production/volatile/sites/30/2017/01/Bananas-218094b-scaled.jpg?resize=960,872?quality=90&webp=true&resize=375,341'

response_label = client.label_detection(image=image)

for label in response_label.label_annotations:
    if label.description in names: 
        print(label.description)
    #print({'label':label.description, 'score':label.score})