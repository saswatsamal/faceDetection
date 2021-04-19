#run.py
import os
print("Welcome to the Face Detection Algorithm/nUsing this program you can see a face in a photo getting recognized by OpenCV and HaarCascade")
print("If you want to execute the program type Y else N")
userInput = str(input())

if (userInput=='Y' or userInput=='y'):
    os.system('python main.py')
else:
    print('Thank you for using')