import collections
from dataclasses import dataclass
import re
from pathlib import Path
from enum import Enum
from abc import ABC
import os
from pathlib import Path
import time
import platform

HOME_DIRECTORY = Path.home()
DATA_DIRECTORY = os.path.join(HOME_DIRECTORY, 'data')
SCRIPT_DIRECTORY = os.path.dirname(__file__)  # absolute dir the script is in
WORKING_DIRECTORY = os.getcwd()

def append_to_file(file, l):
	with open(file, "a") as f: # append mode
		f.write(f'{l}\n')

def generate_directory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
