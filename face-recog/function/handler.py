from urllib import request
import uuid
import json
import os, sys

from deepface import DeepFace
from deepface.basemodels import VGGFace

def cvt_base64_to_img(app_data, filepath="/tmp/app.jpg"):
    response = request.urlopen(app_data)
    with open(filepath, 'wb') as f:
        f.write(response.file.read())

def cvt_base64_to_img(app_data, filepath="/tmp/app.jpg"):
    response = request.urlopen(app_data)
    with open(filepath, 'wb') as f:
        f.write(response.file.read())

def recognize(new_img, stored_img):
	result = DeepFace.verify(
            img1_path = new_img, 
            img2_path = stored_img,
            distance_metric = 'cosine',
            detector_backend = 'opencv',
            model_name = 'VGG-Face'
    )
	return result

def gen_uuid():
    return str(uuid.uuid4().hex)
	
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    req = json.loads(req) # loading json as python dictonary

    uuid = gen_uuid;

    # Save the new image in tmp path
    app_data = req['image']
    cvt_base64_to_img(app_data, filepath=f"/tmp/app_{uuid}.jpg")

    # Save the new image in tmp path
    app_data_db = req['image_db']
    cvt_base64_to_img(app_data_db, filepath=f"/tmp/app_{uuid}_db.jpg")

    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")
    result = recognize(f'/tmp/app_{uuid}.jpg',  f'/tmp/app_{uuid}_db.jpg')
    sys.stdout = old_stdout

    return json.dumps(result)

