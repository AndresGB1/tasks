#Test of function csv_processor
from src.helpers.csv_processor import get_csv_data_as_dict, get_csv_data

def test_happy_get_csv_data_as_dict():
    csv_data = get_csv_data_as_dict("/home/andresgb/Documentos/Andres/JalaSoft/Python/week3_day1/teams_attendance_app/attendace_reports")
    assert (len(csv_data) == 5)

def test_unhappy_get_csv_data_as_dict():
    csv_data = get_csv_data_as_dict("/home/andresgb/Documentos/Andres/JalaSoft/Python/week3_day1/teams_attendance_app/asd")
    assert (len(csv_data) == 0)