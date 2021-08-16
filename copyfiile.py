# -*- coding: utf-8 -*-
"""Копирование файлов по xml-файлу."""

from sys import argv
import xml.etree.ElementTree as ET
from shutil import copy

def attribs(child):
    """Вернуть атрибуты для копирования."""
    sourcepath = None
    destpath = None
    filename = None
    if child.tag == 'file':
        sourcepath = child.get('source_path')
        destpath = child.get('destination_path')
        filename = child.get('file_name')
    return sourcepath, destpath, filename

def main(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for child in root:
        sourcepath, destpath, filename = attribs(child)
        if sourcepath and destpath and filename is not None:
            copy(sourcepath + '/' + filename, destpath)

if __name__ == '__main__':
    script, xmlfile = argv
    main(xmlfile)
