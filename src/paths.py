"""Module for getting user directory"""


import os


def __get_user_folder():
    """Get user folder path"""
    return os.path.expanduser('~')


def cache_folder_path():
    """Get cache folder path"""
    return os.path.join(__get_user_folder(), 'Your computer')


def cache_file_path():
    """Get cache file path"""
    return os.path.join(cache_folder_path(), 'cache.json')
