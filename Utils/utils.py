from importlib import import_module
import os
import csv
import re

from Utils.logger_helper import create_log_directory
from Utils.logger_helper import setup_logging

imps = []

def process_config_file(request):
    """Process and load valid configs from command line arg --config

    Args:
        request (object): conftest object to introspect test environment

    Raises:
        ImportError: Raise if module specified via command arg --config does
            not exist
    """
    user_config = None
    config_name = request.config.getoption('--config')
    try:

        user_config = import_module(config_name)
        return user_config
    except ImportError:
        error_msg = 'No config named {}. Make sure you\'re correctly ' \
                    'referencing where config is saved'.format(config_name)
        raise ImportError(error_msg)

    except AttributeError:
        err_msg = 'Specify a config to use or remove the config flag'
        raise ImportError(err_msg)

class ImproperlyConfigured(Exception):
    """Exceptions for unset environment variables"""
    def __init__(self, value):
        """Summary

        Args:
            value (TYPE): Description
        """
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)

def get_config_var(var_name, config_module):
    """Get specified variable from config module

    Args:
        var_name (str): The name of the variable to access from the config
        module object.
        config_module (object): the config module
            from which you access variable settings.

    Raises:
        ImproperlyConfigured: If `var_name` isn't in
            the `config_module` object.

    Returns:
        str: The value of `var_name` in the `config_module` object.
    """
    try:
        return config_module.__dict__[var_name]
    except (AttributeError, KeyError):
        import config.base as cb
        try:
            return cb.__dict__[var_name]
        except:
            err_msg = "Couldn't find {} in base config module, " \
                      "are you sure that's the variable name?".format(var_name)
            raise ImproperlyConfigured(err_msg)


def init_logging():
    """initiates logging for tests"""
    try:
        setup_logging()
    except ValueError:
        create_log_directory()

