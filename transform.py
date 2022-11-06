def transform(extracted_data):
    clean_data = {}
    for index, data in enumerate(extracted_data):
        remove_data(data, clean_data)
        convert_date(clean_data)
        convert_to_int(clean_data)
        add_calculations(clean_data)

        print(clean_data)
    return clean_data

def remove_data(data, clean_data):
    clean_data["date"] = data["date_of_interest"]
    clean_data["case_count"] = data["case_count"]
    clean_data["probable_case_count"] = data["probable_case_count"]
    clean_data["hospitalized_count"] = data["hospitalized_count"]
    clean_data["death_count"] = data["death_count"]
    clean_data["probable_death_count"] = data["probable_death_count"]
    clean_data["case_count_7day_avg"] = data["case_count_7day_avg"]
    clean_data["all_case_count_7day_avg"] = data["all_case_count_7day_avg"]
    clean_data["hosp_count_7day_avg"] = data["hosp_count_7day_avg"]
    clean_data["death_count_7day_avg"] = data["death_count_7day_avg"]
    clean_data["all_death_count_7day_avg"] = data["all_death_count_7day_avg"]

def convert_date(clean_data):
    clean_data["date"] = clean_data["date"].split('T')[0]

def convert_to_int(clean_data):
    for key, value in clean_data.items():
        if key is not "date":
            clean_data[key] = int(value)

def add_calculations(clean_data):
    grouped_counted_cases(clean_data)
    grouped_counted_death_cases(clean_data)

def grouped_counted_cases(clean_data):
    clean_data["case_count"] = clean_data["case_count"] + clean_data["probable_case_count"]
    del clean_data["probable_case_count"]

def grouped_counted_death_cases(clean_data):
    clean_data["death_count"] = clean_data["death_count"] + clean_data["probable_death_count"]
    del clean_data["probable_death_count"]


