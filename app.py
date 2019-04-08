from flask import Flask, request
import os
import json
import uuid
from tf_pose import common
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
import cv2

app = Flask(__name__)

e = TfPoseEstimator(get_graph_path("mobilenet_thin"))

@app.route('/')
def hello_world():
    return 'To use openpose as a service you need to access /upload via POST. Full readme: '

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = "lastphoto.jpg"
        file.save(os.path.join('uploads', f_name))

        image = common.read_imgfile("uploads/lastphoto.jpg", None, None)
        image = cv2.resize(image, (432, 368), interpolation=cv2.INTER_AREA)
        humans = e.inference(image)


        return json.dumps({'filename':f_name, 'humans': humans,'image':image.shape})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
