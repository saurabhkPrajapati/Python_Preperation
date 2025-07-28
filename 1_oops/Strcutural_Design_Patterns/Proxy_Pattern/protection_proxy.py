# You want to control access to a file and restrict operations based on user permissions.
# This example demonstrates how a proxy adds functionality without altering the RealFileAccess implementation

# _________Explanation_______________

# Subject (FileAccess):
#   An abstract interface that defines methods read and write.

# RealSubject (RealFileAccess):
#   The actual class that implements file operations.

# Proxy (ProxyFileAccess):
#   Controls access to the RealFileAccess based on the user's role.
#     Logs every read or write operation.
#     Enforces permissions for write operations.

# Client Code:
#   The client interacts only with the proxy, unaware of the RealFileAccess implementation.

from abc import ABC, abstractmethod


# Step 1: Define the Subject interface
class FileAccess(ABC):
    @abstractmethod
    def read(self) -> str:
        pass

    @abstractmethod
    def write(self, data: str) -> None:
        pass


# Step 2: Create the RealSubject
class RealFileAccess(FileAccess):
    def __init__(self, filename: str):
        self.filename = filename
        self.data = ""  # Simulating file content

    def read(self) -> str:
        return f"Reading data from {self.filename}: {self.data}"

    def write(self, data: str) -> None:
        self.data = data
        print(f"Writing data to {self.filename}: {self.data}")


# Step 3: Create the Proxy
class ProxyFileAccess(FileAccess):
    def __init__(self, filename: str, user_role: str):
        self.real_file_access = RealFileAccess(filename)
        self.user_role = user_role  # e.g., "admin" or "viewer"

    def read(self) -> str:
        print(f"[LOG] {self.user_role} is attempting to read the file.")
        return self.real_file_access.read()

    def write(self, data: str) -> None:
        if self.user_role == "admin":
            print(f"[LOG] {self.user_role} is writing to the file.")
            self.real_file_access.write(data)
        else:
            print(f"[LOG] {self.user_role} does not have write permissions.")
            raise PermissionError("Write access denied.")


# Step 4: Client code
if __name__ == "__main__":
    # Admin user (full access)
    admin_proxy = ProxyFileAccess("admin_file.txt", "admin")
    print(admin_proxy.read())
    admin_proxy.write("Admin data")
    print(admin_proxy.read())

    print("\n")

    # Viewer user (restricted access)
    viewer_proxy = ProxyFileAccess("viewer_file.txt", "viewer")
    print(viewer_proxy.read())
    try:
        viewer_proxy.write("Viewer data")
    except PermissionError as e:
        print(e)
