import csv
import os


class Loader:
    def __init__(self, data_to_load, is_update=False):
        self.data_to_load = data_to_load
        self.is_update = is_update

    def load(self):
        print("Starting the tranformation ...")
        if self.is_update:
            self._load_update_data()
        else:
            self._load_new_data()

    def _load_new_data(self):
        keys = self.data_to_load[0].keys()
        with open("covid_data.csv", "a", newline="", encoding="utf-8-sig") as file:
            csv_writer = csv.DictWriter(file, fieldnames=keys, delimiter=",")
            if os.path.getsize('covid_data.csv') == 0:
                csv_writer.writeheader()
            for data in self.data_to_load:
                csv_writer.writerow(data)

    def _load_update_data(self):
        pass
