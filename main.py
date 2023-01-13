from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.pipeline.training_pipeline import TrainPipeline



if __name__ == '__main__':
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    
    
