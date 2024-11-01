import csv
import json
import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger("logs")


def file_no_duplicates(file_name_1: str, file_name_2: str):
    unique_rows: set = set()
    with open(file_name_1, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader):
            unique_rows.add(tuple(row))

        with open(file_name_2, newline='') as csvfile_2:
            reader = csv.reader(csvfile_2)
            for row in reader:
                unique_rows.add(tuple(row))

        with open('result_v_sindiakov.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(unique_rows)


file_no_duplicates("random.csv", "random-michaels.csv")


def check_valid_json(file_name: str):
    with open(file_name, 'r') as json_file:
        try:
            data = json.load(json_file)
            return data  # Return data if reading is successful
        except Exception as e:
            logger.error(f" Json is invalid: {e}")


check_valid_json('broken_file.json')


def find_child_xml(file_name: str):
    tree = ET.parse(file_name)
    root = tree.getroot()
    for group in root.findall('group'):
        for name in group.findall('number'):
            logger.info(f'{name.tag} {name.text}')
        for timingExbytes in group.findall('timingExbytes'):
            for incoming in timingExbytes.findall('incoming'):
                logger.info(f'{incoming.tag} {incoming.text}')


find_child_xml('groups.xml')
