from subset import data
from transformer import Transformer
from extractor import Extractor

DATASET_API_URL = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"

if __name__ == '__main__':
    print("Starting the processing ...")
    extractor = Extractor(DATASET_API_URL)
    dataset, is_extract_status_ok = extractor.extract()
    if is_extract_status_ok:
        transformer = Transformer(data)
        transformer.transform(data)
        print(transformer.get_clean_data())
    else:
        print("Error during extraction ! End of the program. Good Bye")