import os

from utils.folder_file_manager import make_directory_if_not_exists

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
TRAINING_DIR = os.path.join(CUR_DIR, 'training_data')
OUTPUT_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'output'))
MODEL_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'utils', 'model'))

FRONT_FACE_DETECTION_MODEL = os.path.join(CUR_DIR, 'utils', 'model', 'haarcascade_frontalface_default.xml')

FACE_TRACK_CYCLE = 20
TRACK_QUALITY = 2
MARGIN = 0
OVERLAP_THRESH = 0.2
UNDETECTED_THRESH = 3
EMOTION_CATEGORIES = ["anger", "surprise", "disgust", "fear", "happiness", "sadness"]

TRAIN = False
CNN_MODEL = False
IMAGE_PATH = ""
VIDEO_PATH = "./input/1.mp4"
