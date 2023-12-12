"""Module to work with application cache"""


import json
import os
import paths
from base import Computer


class Cache:
    """Class to work with application cache"""
    def upload_cache(self, computer_obj: Computer):
        """Upload cache to cache file"""
        if not os.path.exists(paths.cache_folder_path()):
            os.mkdir(paths.cache_folder_path())

        with open(
                paths.cache_file_path(),
                'x' if not os.path.exists(paths.cache_file_path()) else 'w') as ct:
            data = {
                'ip': computer_obj.ip,
                'architecture': computer_obj.architecture,
                'processor': computer_obj.processor,
                'kernel': computer_obj.kernel,
                'python_version': computer_obj.python_version,
                'python_build': computer_obj.python_build
            }
            json.dump(data, ct, indent=4)

    def load_cache(self):
        """Load application cache"""
        with open(paths.cache_file_path()) as ct:
            return json.load(ct)
