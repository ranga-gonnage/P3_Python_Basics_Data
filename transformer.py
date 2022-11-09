from tqdm import tqdm
import time

class Transformer:
    def __init__(self, extracted_data):
        self.cleaned_data = []
        self.extracted_data = extracted_data

    def transform(self):
        print("Starting the tranformation ...")
        for index, data in tqdm(enumerate(self.extracted_data), desc="Data transforming"):
            clean_data = {}
            self._remove_data(data, clean_data)
            self._convert_date(clean_data)
            self._convert_to_int(clean_data)
            self._add_calculations(clean_data)
            self._compare_previous_day(index, clean_data)
            self.cleaned_data.append(clean_data)

    def get_clean_data(self):
        return self.cleaned_data

    def _remove_data(self, data, clean_data):
        clean_data["date"] = data["date_of_interest"]
        clean_data["case_count"] = data["case_count"]
        clean_data["probable_case_count"] = data["probable_case_count"]
        clean_data["hospitalized_count"] = data["hospitalized_count"]
        clean_data["death_count"] = data["death_count"]
        clean_data["probable_death_count"] = data["probable_death_count"]
        clean_data["case_count_7day_avg"] = data["all_case_count_7day_avg"]
        clean_data["hosp_count_7day_avg"] = data["hosp_count_7day_avg"]
        clean_data["death_count_7day_avg"] = data["all_death_count_7day_avg"]

    def _convert_date(self, clean_data):
        clean_data["date"] = clean_data["date"].split("T")[0]

    def _convert_to_int(self, clean_data):
        for key, value in clean_data.items():
            if key != "date":
                clean_data[key] = int(value)

    def _grouped_counted_cases(self, clean_data):
        clean_data["case_count"] = (
            clean_data["case_count"] + clean_data["probable_case_count"]
        )
        del clean_data["probable_case_count"]

    def _grouped_counted_death_cases(self, clean_data):
        clean_data["death_count"] = (
            clean_data["death_count"] + clean_data["probable_death_count"]
        )
        del clean_data["probable_death_count"]

    def _calculate_death_pourcent(self, clean_data):
        try:
            pourcent = clean_data["death_count"] / clean_data["case_count"] * 100
        except ZeroDivisionError:
            pourcent = 0

        try:
            pourcent_7days_avg = (
                clean_data["death_count_7day_avg"]
                / clean_data["case_count_7day_avg"]
                * 100
            )
        except ZeroDivisionError:
            pourcent_7days_avg = 0

        clean_data["death_pourcent"] = round(pourcent, 2)
        clean_data["death_7days_avg_pourcent"] = round(pourcent_7days_avg, 2)

    def _calculate_hospitalized_pourcent(self, clean_data):
        try:
            pourcent = clean_data["hospitalized_count"] / clean_data["case_count"] * 100
        except ZeroDivisionError:
            pourcent = 0

        try:
            pourcent_7days_avg = (
                clean_data["hosp_count_7day_avg"]
                / clean_data["case_count_7day_avg"]
                * 100
            )
        except ZeroDivisionError:
            pourcent_7days_avg = 0

        clean_data["hospitalized_pourcent"] = round(pourcent, 2)
        clean_data["hospitalized_7days_avg_pourcent"] = round(pourcent_7days_avg, 2)

    def _add_calculations(self, clean_data):
        self._grouped_counted_cases(clean_data)
        self._grouped_counted_death_cases(clean_data)
        self._calculate_death_pourcent(clean_data)
        self._calculate_hospitalized_pourcent(clean_data)

    def _compare_previous_day(self, index, clean_data):
        if index == 0:
            data = self.extracted_data[index]
            self._fill_comparaison_date(int(data['case_count']), int(data['hospitalized_count']), 
                int(data['death_count']), clean_data)
        else:
            yesterday_data = self.extracted_data[index-1]
            current_data = self.extracted_data[index]
            case_24_last_hours = int(current_data['case_count']) - int(yesterday_data['case_count'])
            hospitalized_24_last_hours = int(current_data['hospitalized_count']) - int(yesterday_data['hospitalized_count'])
            death_24_last_hours = int(current_data['death_count']) - int(yesterday_data['death_count'])
            self._fill_comparaison_date(case_24_last_hours, hospitalized_24_last_hours, 
                death_24_last_hours, clean_data)

    def _fill_comparaison_date(self, case, hospitalized, death, clean_data):
        clean_data["case_24_last_hours"] = case
        clean_data["hospitalized_24_last_hours"] = hospitalized
        clean_data["death_24_last_hours"] = death
        

