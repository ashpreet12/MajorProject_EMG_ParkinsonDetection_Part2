import os

# the folder containing the Kaggle Data ("Tappy Data", "Archived Users") and MIT Data ("Test Data")
# and to which the output files will be saved also:
DATA_FOLDER = "../input/keyboard-taps-data-from-kaggle-and-mit"

# Raw data
RAW_DATA_ZIP_FILENAME = "RawData.zip"
MIT_DATA_FOLDER = os.path.join(DATA_FOLDER, "Test Data")

# Generated data files:
KAGGLE_TAPS_INPUT = "KAGGLE_TAPS.csv"
KAGGLE_USERS_INPUT = "KAGGLE_USERS.csv"
MIT_USERS_INPUT = "MIT_USERS.csv"
MIT_TAPS_INPUT = "MIT_TAPS.csv"

# Generated features files:
KAGGLE_DATA_ARTICLE_METHOD1_FEATURES = "KAGGLE_DATA_ARTICLE_METHOD1_FEATURES.csv"
KAGGLE_NQI_FEATURES = "KAGGLE_NQI_FEATURES.csv"
MIT_NQI_FEATURES = "MIT_NQI_FEATURES.csv"
MIT_NQI_FEATURES_SIDES_PARTITIONS = "MIT_NQI_FEATURES_SIDES_PARTITIONS.csv"

# Others
TAPS_THRESHOLD = 2000
