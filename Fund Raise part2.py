def database(x, id, title, details, target, start_time, end_time, user_id):
    x.id = id
    x.title = title
    x.details = details
    x.target = target
    x.start_time = start_time
    x.end_time = end_time
    x.user_id = user_id 

    project_id = 1
    while os.path.exists(f"projects/{project_id}.txt"):
        project_id += 1

    with open(f"projects/{project_id}.txt", "w") as f:
        f.write(f"{title}\n")
        f.write(f"{details}\n")
        f.write(f"{target}\n")
        f.write(f"{start_time}\n")
        f.write(f"{end_time}\n")
        f.write(f"{user_id}\n")

    return "Project created successfully"

def get_all_projects():
    project_files = os.listdir("projects")

    projects = []
    for project_file in project_files:
        with open(f"projects/{project_file}", "r") as f:
            id = int(project_file.split(".")[0])
            title = f.readline().strip()
            details = f.readline().strip()
            target = float(f.readline().strip())
            start_time = datetime.datetime.strptime(f.readline().strip(), "%Y-%m-%d %H:%M:%S.%f")
            end_time = datetime.datetime.strptime(f.readline().strip(), "%Y-%m-%d %H:%M:%S.%f")
            user_id = int(f.readline().strip())
            project = Project(id, title, details, target, start_time, end_time, user_id)
            projects.append(project)

    return projects

def get_project_by_id(project_id):
    # Check if the project file exists
    if not os.path.exists(f"projects/{project_id}.txt"):
        return None

    with open(f"projects/{project_id}.txt", "r") as f:
        id = int(project_id)
        title = f.readline().strip()
        details = f.readline().strip()
        target = float(f.readline().strip())
        start_time = datetime.datetime.strptime(f.readline().strip(), "%Y-%m-%d %H:%M:%S.%f")
        end_time = datetime.datetime.strptime(f.readline().strip(), "%Y-%m-%d %H:%M:%S.%f")
        user_id = int(f.readline().strip())
        project = Project(id, title, details, target, start_time, end_time, user_id)

    return project

def update_project(project_id, title, details, target, start_time, end_time, user_id):
    # Check if the project file exists
    if not os.path.exists(f"projects/{project_id}.txt"):
        return "Project not found"

    if end_time <= start_time:
        return "Invalid date formula"
    if start_time <= datetime.datetime.now() or end_time <= datetime.datetime.now():
        return "Invalid date formula"

    try:
        target = float(target)
    except ValueError:
        return "Invalid amount of money"

    with open(f"projects/{project_id}.txt", "w") as f:
        f.write(f"{title}\n")
        f.write(f"{details}\n")
        f.write(f"{target}\n")
        f.write(f"{start_time}\n")
        f.write(f"{end_time}\n")
        f.write(f"{user_id}\n")

    return "Project updated successfully"

def delete_project(project_id, user_id):

    if not os.path.exists(f"projects/{project_id}.txt"):
        return "Project not found"

    with open(f"projects/{project_id}.txt", "r") as f:
        file_user_id = int(f.readline().strip())

    if user_id != file_user_id:
        return "Unauthorized"

    os.remove(f"projects/{project_id}.txt")

    return "Project deleted successfully"

def main_menu():
    print("1. View All Projects")
    print("2. Edit My Project")
    print("3. Delete My Project")
    print("4. Search Projects by Date")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def view_all_projects():
    projects = get_all_projects()
    for project in projects:
        print(f"ID: {project.id}")
        print(f"Title: {project.title}")
        print(f"Details: {project.details}")
        print(f"Target: {project.target}")
        print(f"Start Time: {project.start_time}")
        print(f"End Time: {project.end_time}")
        print(f"User ID: {project.user_id}")
        print("")

def edit_my_project(user_id):
    project_id = input("Enter the ID of the project you want to edit: ")
    project = get_project_by_id(project_id)
    if project is None:
        print("Project not found")
        return

    if user_id != project.user_id:
        print("Unauthorized")
        return

    title = input("Enter the new title: ")
    details = input("Enter the new details: ")
    target = input("Enter the new target amount: ")
    start_time = input("Enter the new start time: ")
    end_time = input("Enter the new end time: ")

    update_project(project_id, title, details, target, start_time, end_time)

    print("Project updated successfully")

def delete_my_project(user_id):
    project_id = input("Enter the ID of the project you want to delete: ")
    project = get_project_by_id(project_id)
    if project is None:
        print("Project not found")
        return

    if user_id != project.user_id:
        print("Unauthorized")
        return

    delete_project(project_id)

    print("Project deleted successfully")

def search_projects_by_date(date):
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        return "Invalid date format"

    project_files = os.listdir("projects")

    projects = []
    for project_file in project_files:
        with open(f"projects/{project_file}", "r") as f:
            id = int(project_file.split(".")[0])
            title = f.readline().strip()
            details = f.readline().strip()
            target = float(f.readline().strip())
            start_time = datetime.datetime.strptime(f.readline().strip(), "%Y-%m-%d %H:%M:%S.%f")
            end_time = datetime.datetime.strptime(f.readline().strip(), "%Y-%m-%d %H:%M:%S.%f")
            user_id = int(f.readline().strip())
            if start_time <= date <= end_time:
                project = Project(id, title, details, target, start_time, end_time, user_id)
                projects.append(project)

    return projects

def current_user_id():
    user_id = "Enter User ID: "
    return user_id


user_id = current_user_id()

while True:
    choice = main_menu()
    if choice == "1":
        view_all_projects()
    elif choice == "2":
        edit_my_project(user_id)
    elif choice == "3":
        delete_my_project(user_id)
    elif choice == "4":
        pass
    elif choice == "5":
        break
    else:
        print("Invalid choice")