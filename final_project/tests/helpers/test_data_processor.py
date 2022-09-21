from src.helpers.data_processor import question1, question2
from src.helpers.csv_processor import get_csv_data_as_dict

def test_happy_question1():
    csv_data = get_csv_data_as_dict("/home/andresgb/Documentos/Andres/JalaSoft/Python/week3_day1/teams_attendance_app/attendace_reports")
    meetings_data = question1(csv_data, "Training Branches: Database Basics on TSQL", "4/25/2022", "4/25/2022")
    print(meetings_data)
    assert (meetings_data.get('data')[0]['participants'] == '10')

def test_unhappy_question1():
    csv_data = get_csv_data_as_dict("/home/andresgb/Documentos/Andres/JalaSoft/Python/week3_day1/teams_attendance_app/attendace_reports")
    meetings_data = question1(csv_data, "Training Branches: Database Basics on TSQL", "4/26/2022", "4/26/2022")
    print(meetings_data)
    assert (meetings_data.get('data') == [])