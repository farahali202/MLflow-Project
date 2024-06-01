# #liwst src
# from src.mlproject import logger

# # #Lets log one information
# # logger.info("welcome to our custom login")
# # main.py
# import sys
# import os

# # Add the src directory to the system path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# # Now import the mlproject module
# import mlproject

# # Print the version to verify the import
# print(mlproject.__version__)  # Should print 0.0.0

from src.mlproject import logger

from pathlib import Path
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

