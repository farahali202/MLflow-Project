# #liwst src
# from src.mlproject import logger

# #Lets log one information
# logger.info("welcome to our custom login")
# main.py
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Now import the mlproject module
import mlproject

# Print the version to verify the import
print(mlproject.__version__)  # Should print 0.0.0

