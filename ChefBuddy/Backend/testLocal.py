import os
import io
from google.cloud import vision
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'chef-buddy-359715-5b34eebe35c3.json'
client=vision.ImageAnnotatorClient()
names = ['Banana', 'Apple', 'Mango', 'Water Melon', 'Grapes', 'Orange', 'kiwi', 'pears']

def local_vision(fileName):
    file_name=r'file.jpg'
    image_path=f'{file_name}'
    with io.open(image_path,'rb')as image_file:
        content=image_file.read()
    image=vision.Image(content=content)
    response=client.label_detection(image=image)
    labels = response.label_annotations
    df=pd.DataFrame(columns=['description'])
    for label in labels:
        if label.description in names:
            return label.description
    '''df=df.append(
        dict(
            description=label.description,
        ),ignore_index=True
   )
print(df)'''