# python modules
import os
import csv
import json
import collections

DEFAULT = "default"

INPUT_FORMATS = {"json": [DEFAULT],
                 "csv": [DEFAULT]}

OUTPUT_FORMATS = {"json": [DEFAULT],
                  "csv": [DEFAULT]}


class ContactDataCrawler():
    """Contact Data Crawler"""

    def __init__(self, input_file, output_file="", reader="", writer=""):
        """Initializes the object"""

        self.input_file = input_file
        self.reader = reader if reader else DEFAULT
        self.writer = writer if writer else DEFAULT
        self.output_file = output_file
        self.data_dict = {}

    def store_data(self):
        """
        Gets data from source and stores it in requested file format.
        """
        self.get_contact_data()
        if self.data_dict:
            self.set_contact_data()

    def get_contact_data(self):
        """
        Main parser method to collect data from source.
        """
        _, ext = os.path.splitext(self.input_file)

        if ext == ".csv":
            if self.reader == DEFAULT:
                self.data_dict = self.parse_csv_data()
        elif ext == ".json":
            if self.reader == DEFAULT:
                self.data_dict = self.parse_json_data()
        self.data_dict = collections.OrderedDict(sorted(self.data_dict.items()))

    def set_contact_data(self):
        """
        Main writer method to store data in requested file format.
        """
        _, ext = os.path.splitext(self.output_file)

        if ext == ".csv":
            if self.writer == DEFAULT:
                self.write_csv_data()
        elif ext == ".json":
            if self.writer == DEFAULT:
                self.write_json_data()

    def write_csv_data(self):
        """
        Write parsed data to CSV file.
        """
        with open(self.output_file, mode='w') as csv_output:
            csv_writer = csv.writer(csv_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

            for i, entry in enumerate(self.data_dict.values()):
                if i == 0:
                    csv_writer.writerow(entry.keys())
                    csv_writer.writerow(entry.values())
                else:
                    csv_writer.writerow(entry.values())

    def write_json_data(self):
        """
        Write parsed data to JSON file.
        """
        with open(self.output_file, "w") as json_output:
            json.dump(self.data_dict, json_output, indent=4)

    def parse_csv_data(self):
        """
        Parse data from CSV file.
        """
        csv_data = {}
        with open(self.input_file, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for i, row in enumerate(csv_reader):
                csv_data["Entry{}".format(i)] = row
        return csv_data

    def parse_json_data(self):
        """
        Parse data from JSON file.
        """
        with open(self.input_file, "r") as json_file:
            json_data = json.load(json_file)
        return json_data
