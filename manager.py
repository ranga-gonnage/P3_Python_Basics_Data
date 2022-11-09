from subset import data
from transformer import Transformer
from extractor import Extractor
from loader import Loader
from updater import Updater

import csv


class Manager:
    def __init__(self, url_to_extract):
        self.extractor = Extractor(url_to_extract)
        self.dataset = []
        self.is_extract_status_ok = False
        self.tranform_data = []

    def run(self):
        self._extract()
        self._transform()
        self._load()

    def _extract(self):
        self.dataset, self.is_extract_status_ok = self.extractor.extract()

    def _transform(self):
        self._handle_tranform_or_update()

    def _load(self):
        loader = Loader(self.tranform_data)
        loader.load()

    def _handle_tranform(self):
        transformer = Transformer(self.dataset)
        transformer.transform()
        self.tranform_data = transformer.get_clean_data()
        

    def _handle_update(self):
        transformer = Transformer(self.dataset)
        transformer.transform()
        updater = Updater(transformer.get_clean_data())
        updater.update()
        self.tranform_data = updater.get_clean_data()

    def _handle_tranform_or_update(self):
        if self.is_extract_status_ok:
            if self._is_file_contains_data():
                self._handle_update()
            else:
                self._handle_tranform()
        else:
            print("Error during extraction ! End of the program. Good Bye")

    def _is_file_contains_data(self):
        is_file_contains_data = False
        try:
            with open('covid_data.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                is_file_contains_data = len(list(spamreader)) != 0
        except FileNotFoundError:
            return False
        return is_file_contains_data
    
