# Face Detection 

<img src = "./img/faceDetection.png">

## What is Face Detection?
Face detection is a computer technology being used in a variety of applications that identifies human faces in digital images. Face detection also refers to the psychological process by which humans locate and attend to faces in a visual scene.

## What are Haar Cascades?
- Haar Cascade classifiers are an effective way for object detection. 
- Proposed by Paul Viola and Michael Jones in their paper Rapid Object Detection using a Boosted Cascade of Simple Features [↗](https://www.researchgate.net/publication/3940582_Rapid_Object_Detection_using_a_Boosted_Cascade_of_Simple_Features)
- It is a machine learning-based approach where a lot of positive and negative images are used to train the classifier.
  - Positive images – These images contain the images which we want our classifier to identify.
  - Negative Images – Images of everything else, which do not contain the object we want to detect.
  
(Know more [here ↗](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html)).

## Haar-cascade Detection in Python(OpenCV)
- OpenCV comes as a detector which uses Haar Cascade.
- In face detection, we use the *Haarcascade Frontal Face* which is in `xml` format.

---

# Let's jump into the code
- What are the requirements you need to have before running the code (all latest version)
```python
--- python
--- opencv-python
--- haarcascade_frontalface_default.xml
```
Download the haar cascade files [here ↗](https://raw.githubusercontent.com/saswatsamal/faceDetection/master/haarcascade_frontalface_default.xml)
