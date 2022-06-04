from genericpath import exists
from black import main
import object_detection
import os
import tensorflow as tf 
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

CUSTOM_MODEL_NAME = 'my_ssd_mobnet' 
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'

paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow','scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace','annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace','models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace','pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME), 
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'export'), 
    'TFJS_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfjsexport'), 
    'TFLITE_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfliteexport'), 
    'PROTOC_PATH':os.path.join('Tensorflow','protoc')
}

files = {
    'PIPELINE_CONFIG':os.path.join('Tensorflow', 'workspace','models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME), 
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}

def main():

    """
    for path in paths.values():
        if not os.path.exists(path):
            command = "mkdir -p " + path
            os.system(command)

    command = "wget " + PRETRAINED_MODEL_URL
    os.system(command)


    labels = [{'name':'thumbUp', 'id':1}, {'name':'thumbDown', 'id':2}, {'name':'thankYou', 'id':3}, {'name':'peace', 'id':4}]

    with open(files['LABELMAP'], 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')


    if not os.path.exists(files['TF_RECORD_SCRIPT']):
        command = "git clone https://github.com/nicknochnack/GenerateTFRecord " + paths['SCRIPTS_PATH']
        os.system(command)

    """
    command = "python3 "+files['TF_RECORD_SCRIPT']+ " -x "+ os.path.join(paths['IMAGE_PATH'], 'train_bis') + " -l " + files['LABELMAP'] + " -o " + os.path.join(paths['ANNOTATION_PATH'], 'train.record')
    os.system(command)

    #command = "python3 "+files['TF_RECORD_SCRIPT']+ " -x "+ os.path.join(paths['IMAGE_PATH'], 'test') + " -l " + files['LABELMAP'] + " -o " + os.path.join(paths['ANNOTATION_PATH'], 'test.record')
    #os.system(command)


if __name__ == '__main__':
    main()
    