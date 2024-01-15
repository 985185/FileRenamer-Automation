import os

def bulk_rename_files(directory, prefix):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_filename = f"{prefix}_{filename}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} to {new_filename}")

# Provide the directory path and prefix
directory_path = "/path/to/your/directory"
prefix_to_add = "new_prefix"

bulk_rename_files(directory_path, prefix_to_add)
