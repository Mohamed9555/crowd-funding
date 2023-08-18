import sys 
from components import *

def create_project(index):
    title = input("Enter title: ")
    details = input("Enter Details: ")
    total_target = input("Enter total target in EGP: ")
    while True:
        pattern = r'^\d+(\.\d+)?$'
        if re.match(pattern, total_target):
            break
        elif total_target == "exit":
            sys.exit(0) 
        else:
            print("Can't contain letters (exit)")
            total_target = input("Enter total target in EGP: ")
    start_date = check_date("start")
    end_date = check_date("end")

    project_data = {
        "title" : title,
        "details" : details,
        "total_target" : total_target,
        "start_date" : start_date,
        "end_date" : end_date 
    }

    save_project(index, project_data)
    

def view_projects(index):
    try:
        with open(users_data, 'r') as fileobj:
            data = json.load(fileobj) 
            table = data[index]["projects"]  
            print(tabulate(table, headers = "keys", showindex="always", tablefmt="grid"))
    except Exception as e:
        print("An error occurred while loading data:", e)
        return []    

def edit_projects(index):
    try:
        print("You can choose from the following: ")
        view_projects(index)
        old_data = load_data()  # list of dicts
        projects_count = len(old_data[index]["projects"])
        try:
            project_num = input("Enter Choice: ")
            project_num = int(project_num)
            while project_num < 0 or project_num >= projects_count:
                print("not valid input")
                project_num = input("Enter Choice: ")
                project_num = int(project_num)

        except:
            print("Invalid input. Please enter a valid integer.")
        while True:
            print("1. title")
            print("2. details")
            print("3. total target")
            print("4. start date")
            print("5. end data")
            print("6. exit editing")
            field = input("Choose Field: ")
            if field == "1":
                edit = input("title: ")
                old_data[index]["projects"][project_num]["title"] = edit
            elif field == "2":
                edit = input("details: ")
                old_data[index]["projects"][project_num]["details"] = edit
            elif field == "3":
                edit = input("Enter total target in EGP: ")
                while True:
                    pattern = r'^\d+(\.\d+)?$'
                    if re.match(pattern, edit):
                        break
                    elif edit == "exit":
                        sys.exit(0) 
                    else:
                        print("Can't contain letters (exit)")
                        edit = input("Enter total target in EGP: ")
                old_data[index]["projects"][project_num]["total_target"] = edit
            elif field == "4":
                edit = check_date("start")
                old_data[index]["projects"][project_num]["start_date"] = edit
            elif field == "5":
                edit = check_date("end")
                old_data[index]["projects"][project_num]["end_date"] = edit
            elif field == "6":
                with open(users_data, 'w') as fileobj:
                    json.dump(old_data, fileobj, indent=4) 
                break
            else:
                print("print invalid choice")   
        view_projects(0)
    except Exception as e:
        print("An error occurred while saving data:", e)


def delete_project(index):
    print("You can choose from the following: ")
    view_projects(index)
    old_data = load_data()  # list of dicts
    projects_count = len(old_data[index]["projects"])
    try:
        project_num = input("Enter Choice: ")
        project_num = int(project_num)
        while project_num < 0 or project_num >= projects_count:
            print("not valid input")
            project_num = input("Enter Choice: ")
            project_num = int(project_num)
        del old_data[index]["projects"][project_num]
        with open(users_data, 'w') as fileobj:
                json.dump(old_data, fileobj, indent=4)
    except:
        print("Invalid input. Please enter a valid integer.")


def search_project(index):
    date = check_date("start or end")
    data = load_data()
    projects_count = len(data[index]["projects"])
    for i, item in enumerate(data[index]["projects"]):
        if date == item["start_date"] or date == item["end_date"]:
            print("project found")
            project_row = data[index]["projects"][i]
            for key, value in project_row.items():
                print(f"{key}: {value}")
        else: 
            print("project not found")
# search_project(1)
# create_project(1)

# edit_projects(0)