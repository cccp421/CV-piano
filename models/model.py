import cv2
from tensorflow.keras import models
import numpy as np
import sys
sys.path.append("src")
import os

print("Welcome to Paper Piano ！！！")
TRACKING_BOX_RESOLUTION = (40 , 40)
model_path = os.path.join("models", "touch_detection_model.keras")
model_list = os.listdir("models")

if "touch_detection_model.keras" not in model_list:
    print("Model not found. We need to train the model on your finger's data.")
else:
    try:
        model = models.load_model(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

def Predict(img):
    resized_img = cv2.resize(img, TRACKING_BOX_RESOLUTION)
    data = np.expand_dims(resized_img / 255.0, axis=0)
    prediction = model.predict(data)[0][0]  # Assuming single output
    print(prediction)
    threshold = 0.502  # Consider moving this to a configuration or argument
    return 0 if prediction > threshold else 1

#
# import cv2
# from tensorflow.keras import models
# import numpy as np
# import sys
# sys.path.append("src")
# import os
#
# TRACKING_BOX_RESOLUTION = (40 , 40)
#
# model_list = os.listdir("models")
# if "touch_detection_model.h5" not in model_list:
#     print("We need to train model on your finger's data")
# else:
#     model = models.load_model("models/touch_detection_model.h5")
#
# def Predict(img):
#   resized_img = cv2.resize(img, TRACKING_BOX_RESOLUTION)
#   # Add the batch dimension and normalize pixel values
#   data = np.expand_dims(resized_img/255, axis=0)
#   # Make the prediction
#   prediction = model.predict(data)
#   print(prediction)
#   if prediction > 0.502:
#       return 0
#   else:
#       return 1