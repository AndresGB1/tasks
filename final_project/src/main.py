from helpers.csv_processor import get_csv_data_as_dict, get_csv_data
from helpers.data_processor import question1, question2
from helpers.json_processor import export_json_file
import pprint 

## app entry point
def process_questions():
    ## display questions menu
    ##- What is the number of Partipants attending **{meeting_name}** Meeting per date, date filter between **{start_date}** and **{end_date}**
    ##- What is the duration of **{meeting_name}** Meeting per date, date filter between **{start_date}** and **{end_date}****
    print("Welcome to the Teams Attendance App")
    print("Please select one of the following options:")

    selected_question = 0
    ##while be a number
    while selected_question not in [1,2,3]:
        print("1. What is the number of Partipants attending **{meeting_name}** Meeting per date, date filter between **{start_date}** and **{end_date}**")
        print("2. What is the duration of **{meeting_name}** Meeting per date, date filter between **{start_date}** and **{end_date}****")
        print("3. Quit")
        selected_question = input("Please select an option: ")
        try:
            selected_question = int(selected_question)
        except:
            print("Please enter a valid option")
            selected_question = 0

    return selected_question

def process_question_options(question):

    if question == 3:
        print("Thank you for using the Teams Attendance App")
        return
    
    ## Read csv from 8 files
    csv_data = get_csv_data_as_dict("/home/andresgb/Documentos/Andres/JalaSoft/Python/week3_day1/teams_attendance_app/attendace_reports")
    
    ## display input to request meeting name, end and start date
    meeting_name = input("Please enter the meeting name: ")
    start_date = input("Please enter the start date: ")
    end_date = input("Please enter the end date: ")

    if question == 1:
        meetings_data = question1(csv_data, meeting_name, start_date, end_date)

    if question == 2:
        meetings_data = question2(csv_data, meeting_name, start_date, end_date)
        
    export_json_file(meetings_data, f'question{question}.json')
    print(f'The result was saved in the path: result/question{question}.json')

def main():
    question  = process_questions()
    process_question_options(question)



main()