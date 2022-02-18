from humps import camelize
from pathlib import Path


def to_camel(string):
    return camelize(string)


def pwd():
    return Path(__file__)
