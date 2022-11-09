import csv

class Updater:
    LAST_INDEX = -1

    def __init__(self, extracted_data):
        self.cleaned_data = []
        self.extracted_data = extracted_data

    def update(self):
        print("Starting the update ...")
        last_line = self._get_last_line()
        if(last_line[0] != self.extracted_data[self.LAST_INDEX]['date']):
            self.cleaned_data.append(self.extracted_data[self.LAST_INDEX])
        else:
            print("Nothing to update ! Goodbye")
            exit()

    def get_clean_data(self):
        return self.cleaned_data

    def _get_last_line(self):
        try:
            with open('covid_data.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                return list(spamreader)[self.LAST_INDEX]
        except FileNotFoundError:
            print("Error during file reading ! End of the program. Good Bye")
            exit()