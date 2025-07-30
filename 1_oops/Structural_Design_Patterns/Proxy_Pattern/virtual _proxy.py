# Problem:
#     You have an object that is expensive to create, such as loading a large image file or initializing a heavy computational resource.
#     You want to defer its creation until it's actually needed.

# Scenario:
#     You are working with an image viewer application.
#     Loading high-resolution images can be slow, so you use a proxy to delay the actual loading until the image is displayed.


from abc import ABC, abstractmethod


# Step 1: Define the Subject interface
class Image(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


# Step 2: Create the RealSubject
class HighResolutionImage(Image):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._load_image()

    def _load_image(self) -> None:
        print(f"Loading high-resolution image from {self.file_path}... (This is expensive!)")
        # Simulate a time-consuming operation
        import time
        time.sleep(2)  # Simulates a delay in loading
        self.loaded = True

    def display(self) -> None:
        print(f"Displaying high-resolution image: {self.file_path}")


# Step 3: Create the Proxy
class ProxyImage(Image):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.real_image = None

    def display(self) -> None:
        if not self.real_image:
            print("Image not loaded yet. Loading now...")
            self.real_image = HighResolutionImage(self.file_path)
        self.real_image.display()


# Step 4: Client code
if __name__ == "__main__":
    # Client interacts with the proxy instead of directly with the high-resolution image
    image = ProxyImage("large_photo.jpg")

    # The image is not loaded yet
    print("Proxy created, but image not loaded yet.")

    # When display is called, the image is loaded
    print("\n--- Displaying Image for the First Time ---")
    image.display()

    # Subsequent calls to display won't reload the image
    print("\n--- Displaying Image Again ---")
    image.display()
