from manager import Manager

DATASET_API_URL = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"

if __name__ == '__main__':
    print("Starting the processing ...")
    manager = Manager(DATASET_API_URL)
    manager.run()