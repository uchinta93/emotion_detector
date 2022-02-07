# EmotionDetector

## Overview
This project is to train the several models for the emotion estimation of facial expressions and to evaluate each model's
capability.
The main architectures of the models include CNN & Scikit-learn using inception model for the feature extraction.
Tensorflow, Keras, Scikit-learn, OpenCV, Pandas, Matplotlib, Pillow libraries are used in this project.

## Structure

- src

    The main source code for training the models and detectetion of the facial expressions

- utils

    * The trained models
    * The source code for the management of folders and files of this project
    
- training_data

    * The images & their legends for model training
    
- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    The several settings including file path
    
## Installation

- Environment

    Ubuntu 18.04, Windows 10, Python 3.6

- Dependency Installation

    Please navigate to the project directory and run the following command in the terminal
    ```
        pip3 install -r requirements.txt
    ``` 

## Execution

- If you want model training, please set TRAIN variable in settings file with True, or if you want only emotion detection, 
please set TRAIN variable in settings file with False.

- In the case of emotion detection, you have to set either IMAGE_PATH or VIDEO_PATH variable in settings file with the 
absolute path of image or video where you want to detect the emotion. At this time, you can select which model you will use
in CNN_MODEL variable of settings file, where if CNN_MODEL is True, you will use CNN model, else, Scikit-learn model. 

- Please run the following command in the terminal

    ```
        python3 app.py
    ```

    
