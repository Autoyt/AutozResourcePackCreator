import os
import shutil

def get_pack_format(version):
    version_to_pack_format = {
        "1.6.1": 1, "1.6.2": 1, "1.6.3": 1, "1.6.4": 1, "1.7.2": 1, "1.7.4": 1, "1.7.5": 1, "1.7.6": 1, "1.7.7": 1,
        "1.7.8": 1, "1.7.9": 1, "1.7.10": 1, "1.8": 1, "1.8.1": 1, "1.8.2": 1, "1.8.3": 1, "1.8.4": 1, "1.8.5": 1,
        "1.8.6": 1, "1.8.7": 1, "1.8.8": 1, "1.8.9": 1, "1.9": 2, "1.9.1": 2, "1.9.2": 2, "1.9.3": 2, "1.9.4": 2,
        "1.10": 2, "1.10.1": 2, "1.10.2": 2, "1.11": 3, "1.11.1": 3, "1.11.2": 3, "1.12": 3, "1.12.1": 3, "1.12.2": 3,
        "1.13": 4, "1.13.1": 4, "1.13.2": 4, "1.14": 4, "1.14.1": 4, "1.14.2": 4, "1.14.3": 4, "1.14.4": 4, "1.15": 5,
        "1.15.1": 5, "1.15.2": 5, "1.16": 5, "1.16.1": 5, "1.16.2": 6, "1.16.3": 6, "1.16.4": 6, "1.16.5": 6, "1.17": 7,
        "1.17.1": 7, "1.18": 8, "1.18.1": 8, "1.18.2": 8, "1.19": 9, "1.19.1": 9, "1.19.2": 9, "1.19.3": 12,
        "1.19.4": 13,
        "1.20": 15, "1.20.1": 15, "1.20.2": 18, "1.20.3": 22, "1.20.4": 22, "1.20.5": 22, "1.20.6": 22, "1.21": 34
    }

    return version_to_pack_format.get(version, 'Unknown version')


#Finds desktop route and casts it to Main.PY
def desktoproot(name):
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    # Define the source directory and the destination path
    source_directory = name
    destination_dir = os.path.join(desktop_path, f"{name} RP")

    # Move the directory to the desktop
    shutil.move(source_directory, destination_dir)
    print(f"""
    Moved to {source_directory}\\{destination_dir}""")

def iconmethod(name):  #Method that asks if you want to create a guide for adding an icon
    image_path = os.path.join(name, "GuideforIcon.txt")  #Moves txt file into the directory
    with open(image_path, 'w') as file:
        file.write("Convert your image to a PNG File and 128x128 Pixel. Rename the file as pack.png")


