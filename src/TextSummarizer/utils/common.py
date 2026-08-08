#functionalities to read yaml file
import os
from box.exceptions import BoxValueError
import yamlfrom src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Pathfrom typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns it as a ConfigBox object.

    Args:
        path_to_yaml (str): Path like input.


    Raises:
        ValueError: If yaml file is empty.
        e: empty file 

    Returns:
        ConfigBox: ConfigBox type object.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories.

    Args:
        path_to_directories (list): List of path of directories.
        ignore_log (bool, optional):ignore if multiple dirs is to be created. Defaults to True. Whether to log info or not.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
 