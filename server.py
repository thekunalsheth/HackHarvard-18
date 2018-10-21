import cv2
import trycam
import os
from subprocess import call
from subprocess import Popen
import subprocess
import ast
from predict import get_prediction

import trycam
from threading import Thread

from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

app = Flask(__name__)




#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

@app.route("/")
def status():
#    return "Hello from growth!"
    js = jsonify({'response': "Thank you for submitting your request."})
    return js


@app.route("/snapshot", methods=['GET'])
def openCamera():

    call(["python3","trycam.py"])
    
    process = Popen(["python3","predict.py", "./try.jpg"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode("utf-8")
    pos = out.find('"')
    temp = out[pos+1:pos+6]
    file = jsonify({"Name": temp})
    print(temp)
    return file
