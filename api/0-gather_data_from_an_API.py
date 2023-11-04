#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    url = fetch('https://jsonplaceholder.typicode.com/todos/1')
    response = requests.get(url)
    data = response.json()

    #Extract employee information
    EMPLOYEE_NAME:Ali
    NUMBER_OF_DONE_TASKS:7
    TOTAL_NUMBER_OF_TASKS:10

    #print employee TODO list progress
    print(f"Employee {Ali} is done with Tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):")


    #print title of completed tasks
    for task in data['todos']:
        if task['completed']:
            print(f"\t{task['title']}")


