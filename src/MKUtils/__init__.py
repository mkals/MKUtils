from pathlib import Path
import os, logging

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


'''
Convenience method for setting up logger. 
Must be called before logging is tarted.
Must be called again from pools in muiltiprocessing module, works fine to have all write to same file.
'''
def configure_logger(dir: str, filename: str, label: str, file_mode: str, file_level: str = 'DEBUG', stream_level: str = 'INFO'):
    file_handler = logging.FileHandler(os.path.join(dir, filename), mode=file_mode)
    file_handler.setLevel(file_level)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)

    logging.basicConfig(
        format=f'%(asctime)s,%(msecs)d %(name)s %(levelname)s {label} %(message)s', # label to mark which process was logging
        datefmt='%H:%M:%S',
        level=logging.DEBUG,
        handlers=[file_handler, stream_handler],
    )
    
    loggers = ["PIL.TiffImagePlugin", "PIL.PngImagePlugin", "matplotlib.font_manager", "matplotlib.axes"]
    for l in loggers: logging.getLogger(l).level = logging.WARN