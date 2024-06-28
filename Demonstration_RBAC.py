import random

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content

class AccessControl:
    def __init__(self):
        self.roles = {
            'admin': ['read', 'write', 'delete'],
            'editor': ['read', 'write'],
            'viewer': ['read']
        }

    def check_permission(self, user, action):
        return action in self.roles.get(user.role, [])

class FileSystem:
    def __init__(self):
        self.files = {}
        self.access_control = AccessControl()

    def create_file(self, user, file_name, content):
        if self.access_control.check_permission(user, 'write'):
            self.files[file_name] = File(file_name, content)
            print(f"{user.username} created file: {file_name}")
        else:
            print(f"{user.username} doesn't have permission to create files.")

    def read_file(self, user, file_name):
        if self.access_control.check_permission(user, 'read'):
            if file_name in self.files:
                print(f"{user.username} read {file_name}: {self.files[file_name].content}")
            else:
                print(f"File {file_name} not found.")
        else:
            print(f"{user.username} doesn't have permission to read files.")

    def update_file(self, user, file_name, new_content):
        if self.access_control.check_permission(user, 'write'):
            if file_name in self.files:
                self.files[file_name].content = new_content
                print(f"{user.username} updated file: {file_name}")
            else:
                print(f"File {file_name} not found.")
        else:
            print(f"{user.username} doesn't have permission to update files.")

    def delete_file(self, user, file_name):
        if self.access_control.check_permission(user, 'delete'):
            if file_name in self.files:
                del self.files[file_name]
                print(f"{user.username} deleted file: {file_name}")
            else:
                print(f"File {file_name} not found.")
        else:
            print(f"{user.username} doesn't have permission to delete files.")

def simulate_file_operations(file_system, users):
    actions = ['create', 'read', 'update', 'delete']
    file_names = ['document.txt', 'image.jpg', 'script.py', 'data.csv']

    for _ in range(20):  # Simulate 20 random actions
        user = random.choice(users)
        action = random.choice(actions)
        file_name = random.choice(file_names)

        if action == 'create':
            content = f"This is the content of {file_name}"
            file_system.create_file(user, file_name, content)
        elif action == 'read':
            file_system.read_file(user, file_name)
        elif action == 'update':
            new_content = f"Updated content of {file_name}"
            file_system.update_file(user, file_name, new_content)
        elif action == 'delete':
            file_system.delete_file(user, file_name)

        print()  # Add a blank line for readability

if __name__ == "__main__":
    # Create users with different roles
    admin_user = User("Alice", "admin")
    editor_user = User("Bob", "editor")
    viewer_user = User("Charlie", "viewer")

    users = [admin_user, editor_user, viewer_user]

    # Create file system
    file_system = FileSystem()

    # Simulate file operations
    simulate_file_operations(file_system, users)