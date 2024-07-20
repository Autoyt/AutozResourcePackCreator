import os
import time
import Messages
import Directorymaker  # Import the Directorymaker module
import Utils
from Utils import get_pack_format

# Input for pack name
name = input("What would you like to name this pack? ")

def get_valid_version():
    """
    Repeatedly prompts the user for a valid version until one is provided.
    """
    while True:
        version = input("(Valid as of 7.18.24) Enter version: ").strip()
        packvar = get_pack_format(version)
        if packvar == 'Unknown version':
            print("Invalid version. Please try again.")
        else:
            return version

# Get a valid version from the user
version = get_valid_version()

# Asks for image guide (See Messages.py)
askforimage = input("Would you like a guide on how to add an Icon? ").strip().lower()

# Create the main directory
os.makedirs(name, exist_ok=True)

# Create directory structure within the main directory
Directorymaker.create_directory_structure_texture(name)  # Call the function to create texture directories
Directorymaker.create_directory_structure_sounds(name)  # Call the function to create sound directories
Directorymaker.create_directory_structure_models(name)  # Call the function to create model directories
Directorymaker.create_extra_directories(name)
def get_description():  # Function to get a valid description
    while True:
        description = input("(Use ?help) Enter description: ").strip()
        description_lower = description.lower()  # Convert to lower case for case-insensitive comparison
        if description_lower == "?help":
            print(Messages.helpsc())
        else:
            return description

# If the user wants help with adding an image
if askforimage == "yes":
    # Pulls method from Utils.py
    Utils.iconmethod(name)

# Get description from above method
packdescription = get_description()

Messages.loadinganimation()

# Determine pack format (Pulls from Utils.py)
pack_format = get_pack_format(version)
packformat = str(pack_format)  # Converts the value to a string (Allows for printing)

# Create mcMeta file
file_path = os.path.join(name, 'pack.mcmeta')
with open(file_path, 'w') as file:
    file.write(f'{{ "pack": {{ "pack_format": {packformat}, "description": "{packdescription}" }} }}')

# Create summary
summary = Messages.summarymethod(name, version, packformat, packdescription)
print(summary)

time.sleep(3)
# gets directory of texture pack
cwd = Messages.getcwd(name)
print(cwd)

time.sleep(2)

wishtomove = input(f"""
Do you wish to move {name} to your desktop? (Yes or no) """)
if wishtomove.strip().lower() == "yes":
    Messages.loadinganimation()
    Utils.desktoproot(name)
    Messages.endingmessage(name)
