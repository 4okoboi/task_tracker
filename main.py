import json
import argparse
import os

task_filename = "tasks.json"

class TasksFileNotFound(Exception):
    pass

def add_task(
    text: str
) -> int:
    pass
    

def check_file():
    global task_filename
    if os.access(task_filename):
        return True
    else:
        return False

def create_file():
    global task_filename
    file = os.open(task_filename)
    os.close(file)

def run_task(
    task: str
):
    
    match task:
        case "add":
            pass
        case "update":
            pass
        case "mark-in-progress":
            pass
        case "mark-done":
            pass
        case "list":
            pass
            

def main():
    parser = argparse.ArgumentParser(description="Task CLI")

    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task to be added")
    
    update_parser = subparsers.add_parser("update", help="Update already created task")
    update_parser.add_argument("task_id", type=int, help="The ID of task you want to update")
    update_parser.add_argument("task", type=str, help="The task to be added")
    
    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark your task as 'in progress'")
    mark_in_progress_parser.add_argument("task_id", type=int, help="The ID of task you want to update")
    
    mark_done_parser = subparsers.add_parser("mark-done", help="Mark your task as 'done'")
    mark_done_parser.add_argument("task_id", type=int, help="The ID of task you want to update")
    
    list_parser = subparsers.add_parser("list", help="List all your tasks, or filter it by status")
    list_parser.add_argument("done", action="store_true", help="Filter by 'done'")
    list_parser.add_argument("todo", action="store_true", help="Filter by 'todo'")
    list_parser.add_argument("in-progress", action="store_true", help="Filter by 'in-progress'")
    
    args = parser.parse_args()
    
    run_task(args.command)