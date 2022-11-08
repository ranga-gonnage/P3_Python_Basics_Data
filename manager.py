from subset import data
from transformer import Transformer
from extractor import Extractor

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

    def _handle_tranform(self):
        if self.is_extract_status_ok:
            transformer = Transformer(data) #to do with real data
            transformer.transform()
            self.tranform_data = transformer.get_clean_data()
        else:
            print("Error during extraction ! End of the program. Good Bye")

    def _handle_update(self):
        pass

    def _handle_tranform_or_update(self):
        self._handle_tranform()

    def _extract(self):
        self.dataset, self.is_extract_status_ok = self.extractor.extract()

    def _transform(self):
        self._handle_tranform_or_update()

    def _load(self):
        print(self.tranform_data)


