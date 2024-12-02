import os
import random
import string

extensions = ['.py', '.ipynb', '.txt']

def generate_random_string(length=5):
    """Generate a random alphanumeric string."""
    letter = random.choice(string.ascii_uppercase)
    return letter+'_'+''.join(random.choices(string.digits, k=length))

def create_random_py_file(folder_path):
    """Create a random Python file with a random name in the specified folder."""
    random_filename = generate_random_string() + random.choice(extensions)
    random_file_path = os.path.join(folder_path, random_filename)

    with open(random_file_path, 'w') as f:
        f.write("# This is a randomly generated Python file!\n")
        f.write(f"print('Hello from {random_filename}!')\n")

    print(f"Created {random_file_path}")

def create_random_subfolders(base_folder, num_subfolders=5, num_files_per_subfolder=3):
    """Create random subfolders and random Python files within them."""
    for _ in range(num_subfolders):
        subfolder_name = generate_random_string()
        subfolder_path = os.path.join(base_folder, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

        for _ in range(num_files_per_subfolder):
            create_random_py_file(subfolder_path)

if __name__ == "__main__":
    current_working_folder = os.getcwd()
    create_random_subfolders(current_working_folder)
