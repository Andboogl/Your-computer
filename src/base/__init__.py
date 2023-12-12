"""Module to get user computer data"""


import http.client
import platform


class Computer:
    """Class to get user computer info"""
    # Getting IP
    try:
        __IP = http.client.HTTPConnection("ifconfig.me")
        __IP.request("GET", "/ip")
        __IP = str(__IP.getresponse().read()).replace('b', '')
        __IP = __IP.replace('\'', '')

    except Exception:
        __IP = 'Undefind'

    # Computer
    __ARCHITECTURE = platform.architecture()
    __PROCESSOR = platform.processor()

    # Kernel
    __KERNEL = platform.version()
    __KERNEL = __KERNEL.split(':')
    __KERNEL = __KERNEL[0]

    __PYTHON_VERSION = platform.python_version()
    __PYTHON_BUILD = platform.python_build()[0]

    @property
    def ip(self):
        return self.__IP

    @property
    def architecture(self):
        return self.__ARCHITECTURE[0]

    @property
    def processor(self):
        return self.__PROCESSOR

    @property
    def kernel(self):
        return self.__KERNEL

    @property
    def python_version(self):
        return self.__PYTHON_VERSION

    @property
    def python_build(self):
        return self.__PYTHON_BUILD
