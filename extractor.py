import requests


class Extractor:
    OK_STATUS_CODE = 200

    def __init__(self, url_to_extract):
        self.url_to_extract = url_to_extract

    def extract(self):
        print("Starting the extract ...")
        is_extract_status_ok = False
        response = requests.get(self.url_to_extract)
        if response.status_code == self.OK_STATUS_CODE:
            is_extract_status_ok = True
            print("Extract completed ...")
        return response.json(), is_extract_status_ok
