import os


import os

def create_directory_structure_texture(main_dir):
    # Define the base path for the subdirectories
    base_path = os.path.join(main_dir, 'assets', 'minecraft', 'textures')

    # List of subdirectories to create under 'textures'
    subdirectories = [
        'block',
        'colormap',
        'effect',
        'entity',
        'environment',
        'font',
        'gui',
        'item',
        'map',
        'misc',
        'mob_effect',
        'models',
        'painting',
        'particle'
    ]

    # Create the main directory
    os.makedirs(base_path, exist_ok=True)

    # Create each subdirectory
    for subdir in subdirectories:
        # Construct the full path for each subdirectory
        subdir_path = os.path.join(base_path, subdir)
        # Create the subdirectory
        os.makedirs(subdir_path, exist_ok=True)


def create_directory_structure_sounds(main_dir):
    # Define the base path for the subdirectories
    base_path = os.path.join(main_dir, 'assets', 'minecraft', 'sounds')

    # List of subdirectories to create under 'sounds'
    subdirectories = [
        'ambient',
        'block',
        'damage',
        'dig',
        'enchant',
        'entity',
        'event',
        'fire',
        'fireworks',
        'item',
        'liquid',
        'minecart',
        'mob',
        'music',
        'note',
        'portal',
        'random',
        'records',
        'step',
        'tile',
        'ui'
    ]

    # Create the main 'sounds' directory
    os.makedirs(base_path, exist_ok=True)

    # Create each subdirectory
    for subdir in subdirectories:
        # Construct the full path for each subdirectory
        subdir_path = os.path.join(base_path, subdir)
        # Create the subdirectory
        os.makedirs(subdir_path, exist_ok=True)


def create_directory_structure_models(main_dir):
    # Define the base path for the 'models' subdirectories
    base_path = os.path.join(main_dir, 'assets', 'minecraft', 'models')

    # List of subdirectories to create under 'models'
    subdirectories = [
        'block',
        'item'
    ]

    # Create the main 'models' directory
    os.makedirs(base_path, exist_ok=True)

    # Create each subdirectory
    for subdir in subdirectories:
        # Construct the full path for each subdirectory
        subdir_path = os.path.join(base_path, subdir)
        # Create the subdirectory
        os.makedirs(subdir_path, exist_ok=True)


def create_extra_directories(main_dir):
    # Define the base path for the subdirectories
    base_path = os.path.join(main_dir, 'assets', 'minecraft')

    # List of subdirectories to create under 'minecraft'
    subdirectories = [
        'blockstates',
        'font',
        'icons',
        'lang',
        'particles',
        'texts'
    ]

    # Create the main directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)

    # Create each subdirectory
    for subdir in subdirectories:
        # Construct the full path for each subdirectory
        subdir_path = os.path.join(base_path, subdir)
        # Create the subdirectory
        os.makedirs(subdir_path, exist_ok=True)