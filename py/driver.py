import numpy as np
import argparse
import cv2

from keras.models import load_model

import utils
import auto_server


parser = argparse.ArgumentParser()
parser.add_argument('model', help='load the model from this directory')
args = parser.parse_args()

model = load_model(args.model)

def telemetry(telemetry):
    img = utils.stringToImg(telemetry['image'])
    cv2.imshow('car_view', img)
    cv2.waitKey(10)
    
    prediction = model.predict(img.reshape(-1, 120, 80, 1))[0]
    auto_server.send_control(prediction[0].item(), prediction[1].item())


auto_server.telemetry_func = telemetry
auto_server.init()
