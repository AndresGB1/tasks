"""
    Filters in-memory meetings data and uses meeting_name, star_date, end_date, etc...
"""
from datetime import datetime

def question1(meetings_data, meeting_name, start_date, end_date):

    meetings_data_result = {
        "meeting_title": meeting_name,
        "data": []
    }
    for key,meeting  in meetings_data.items():
        if meeting[2][1] == meeting_name: 
            if datetime.strptime(meeting[3][1].split(',')[0], '%m/%d/%Y').date() >= datetime.strptime(start_date, '%m/%d/%Y').date() and datetime.strptime(meeting[4][1].split(',')[0], '%m/%d/%Y').date() <= datetime.strptime(end_date, '%m/%d/%Y').date():
                meetings_data_result.get('data').append({
                    "date": meeting[3][1].split(',')[0],
                    "participants": meeting[1][1]
                })            
    return meetings_data_result

def question2(meetings_data, meeting_name, start_date, end_date):
    meetings_data_result = {
        "meeting_title": meeting_name,
        "data": []
    }
    for key,meeting  in meetings_data.items():
        if meeting[2][1] == meeting_name: 
            if datetime.strptime(meeting[3][1].split(',')[0], '%m/%d/%Y').date() >= datetime.strptime(start_date, '%m/%d/%Y').date() and datetime.strptime(meeting[4][1].split(',')[0], '%m/%d/%Y').date() <= datetime.strptime(end_date, '%m/%d/%Y').date():
                meetings_data_result.get('data').append({
                    "date": meeting[3][1].split(',')[0],
                    "duration": get_duration(meeting[3][1].split(', ')[1], meeting[4][1].split(',')[1])
                })
    return meetings_data_result

def get_duration(start_time, end_time):
    start_time = start_time.replace(' ', '')
    end_time = end_time.replace(' ', '')
    duration = datetime.strptime(end_time, '%H:%M:%S%p') - datetime.strptime(start_time, '%H:%M:%S%p')
    #return at 00h 00m 00s format
    duration = str(duration).split(':')
    return f'{duration[0]}h {duration[1]}m {duration[2]}s'