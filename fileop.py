import json
from tabulate import tabulate

users_data = "users.json"

def load_data():
    try:
        with open(users_data, 'r') as fileobj:
            data = json.load(fileobj) 
            return data  
    except Exception as e:
        print("An error occurred while loading data:", e)
        return []


# myinfo ={"id":3,"name":"noha"}
def save_data(info):
    try:
        old_data = load_data()  # list of dicts
        old_data.append(info)
        with open(users_data, 'w') as fileobj:
            json.dump(old_data, fileobj, indent=4)  
    except Exception as e:
        print("An error occurred while saving data:", e)


def save_project(index, project_info):
    try:
        old_data = load_data()  # list of dicts
        old_data[index]["projects"].append(project_info)
        with open(users_data, 'w') as fileobj:
            json.dump(old_data, fileobj, indent=4)  
    except Exception as e:
        print("An error occurred while saving data:", e)

def load_projects(index):
    try:
        with open(users_data, 'r') as fileobj:
            data = json.load(fileobj) 
            return data[index]["projects"]  
    except Exception as e:
        print("An error occurred while loading data:", e)
        return []


# table = load_projects(1)
# print(tabulate(table, headers = "keys"))