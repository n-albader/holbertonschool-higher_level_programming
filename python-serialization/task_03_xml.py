#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for element in root:
        dictionary[element.tag] = element.text

    return dictionary
