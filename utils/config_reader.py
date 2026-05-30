"""Centralised reader for config/config.ini.

Keeps environment settings (URL, browser, timeouts) out of the test code so
the same suite can run against different browsers/environments without edits.
"""
import configparser
import os


class ConfigReader:
    _config = None

    @classmethod
    def _load(cls):
        if cls._config is None:
            cls._config = configparser.ConfigParser()
            config_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "config", "config.ini"
            )
            cls._config.read(config_path)
        return cls._config

    @classmethod
    def get(cls, section, key, fallback=None):
        return cls._load().get(section, key, fallback=fallback)

    @classmethod
    def get_bool(cls, section, key, fallback=False):
        return cls._load().getboolean(section, key, fallback=fallback)

    @classmethod
    def get_int(cls, section, key, fallback=0):
        return cls._load().getint(section, key, fallback=fallback)
