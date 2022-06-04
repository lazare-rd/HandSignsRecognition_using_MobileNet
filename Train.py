import os
import Setup

TRAINING_SCRIPT = os.path.join(Setup.paths['APIMODEL_PATH'], 'research', 'object_detection', 'model_main_tf2.py')

def train():
    command = "python3 {} --model_dir={} --pipeline_config_path={} --num_train_steps=1500".format(TRAINING_SCRIPT, Setup.paths['CHECKPOINT_PATH'], Setup.files['PIPELINE_CONFIG'])
    os.system(command)

def test():
    command = "python3 {} --model_dir={} --pipeline_config_path={} --checkpoint_dir={}".format(TRAINING_SCRIPT, Setup.paths['CHECKPOINT_PATH'], Setup.files['PIPELINE_CONFIG'], Setup.paths['CHECKPOINT_PATH'])
    os.system(command)

if __name__ == "__main__" :
    train()
    #test()

