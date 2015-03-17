import os.path
import chart

DATA_DIR_NAME = "data"
CHART_DIR_NAME = os.path.dirname(chart.__file__)
DATA_DIR = os.path.join(CHART_DIR_NAME, DATA_DIR_NAME)
DATA_FILE_NAME = "eFw3Cefj.json"
DATA_FILE = os.path.join(DATA_DIR, DATA_FILE_NAME)