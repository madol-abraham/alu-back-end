#!/usr/bin/python3
import requests
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: Ali johnson
NUMBER_OF_DONE_TASKS: 6/1o
TOTAL_NUMBER_OF_TASKS:10

completed_tasks = ["Task 1", "Task 2", "Task 3","Task 4", "Task 5", "Task 6" ]  # tasks

for task in completed_tasks:
    formatted_task = "\t " + task  # Add 1 tabulation and 1 space before the task title
    print(formatted_task)

print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")


