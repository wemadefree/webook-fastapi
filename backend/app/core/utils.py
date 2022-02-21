from humps import camelize, decamelize
from pathlib import Path


def to_camel(string):
    return camelize(string)


def to_snake(string):
    return decamelize(string)


def pwd():
    return Path(__file__)
