from settings import TRAIN

if __name__ == '__main__':
    if TRAIN:
        from src.trainer.cnn import CNNTrainer
        from src.trainer.scikit_classifier import ClassifierTrainer
        from src.trainer.training_data_processor import TrainDataProcessor
        train_data_processor = TrainDataProcessor()
        train_data_processor.create_training_data_for_h5()
        train_data_processor.create_training_data_for_pkl()
        CNNTrainer().run()
        ClassifierTrainer().train()
    else:
        from src.detector.emotion import EmotionDetector
        EmotionDetector().run()
