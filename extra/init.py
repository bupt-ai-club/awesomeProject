import os
import re
import shutil
from datetime import datetime, timedelta

"""
Init m markdown file.
"""

# Get the current working directory
current_directory = os.getcwd()
contents_directory = os.path.join(os.path.dirname(current_directory), "docs", "contents")

# Get the names of all directories in the current directory
directories = [d for d in os.listdir(contents_directory) if os.path.isdir(os.path.join(contents_directory, d))]

# Regular expression pattern to match directory names in the format YYYYMMDD-YYYYMMDD
pattern = re.compile(r'(\d{8})-(\d{8})')

# Filter out directories that match the pattern and sort them by date
valid_directories = []
for directory in directories:
    match = pattern.match(directory)
    if match:
        valid_directories.append(directory)

# Sort by start date
valid_directories.sort(key=lambda date: datetime.strptime(date.split('-')[0], '%Y%m%d'))

# Find the latest directory
latest_directory = valid_directories[-1] if valid_directories else None

if latest_directory:
    latest_end_date_str = latest_directory.split('-')[1]
    latest_end_date = datetime.strptime(latest_end_date_str, '%Y%m%d')

    # Create a new week time
    new_start_date = latest_end_date + timedelta(days=1)
    new_end_date = new_start_date + timedelta(days=6)
    new_directory = f"{new_start_date.strftime('%Y%m%d')}-{new_end_date.strftime('%Y%m%d')}"

    # Print results
    print(f"Latest directory: {latest_directory}")
    print(f"New directory: {new_directory}")
else:
    print("No valid directories found.")


final_directory = os.path.join(contents_directory, new_directory)
images_directory = os.path.join(final_directory, "images")

print(f"Create directory: {final_directory}")
os.mkdir(final_directory)

print(f"Create images directory: {images_directory}")
os.mkdir(images_directory)

print(f"Copy template file")
template_file = os.path.join(contents_directory, "template.md")
destination_file = os.path.join(final_directory, "{}.md".format(new_directory))
shutil.copy2(template_file, destination_file)
