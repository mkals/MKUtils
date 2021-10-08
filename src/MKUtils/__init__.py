import collections
from dataclasses import dataclass
import re
from pathlib import Path
from enum import Enum
from abc import ABC
import os
from pathlib import Path

HOME_DIRECTORY = Path.home()
DATA_DIRECTORY = os.path.join(HOME_DIRECTORY, 'data')
SCRIPT_DIRECTORY = os.path.dirname(__file__)  # absolute dir the script is in
WORKING_DIRECTORY = os.getcwd()

def create_dir(path):
    pass