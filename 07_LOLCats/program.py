import os
import platform
import subprocess

import cat_service


def download_cats(folder):
    dog_count = 8
    for i in range(1, dog_count + 1):
        print('Downloading Lolcat {}'.format(i))
        name = 'lolcat {}'.format(i)
        cat_service.get_cats(folder, name)
    print('Done')


def display_cats(folder):
    #open folder
    my_sys = platform.system()

    if my_sys  == 'Darwin':
        subprocess.call (['open', folder])

    elif my_sys == 'Windows':
        subprocess.call (['explorer', folder])

    elif my_sys == 'Linux':
       subprocess.call (['xdg-open', folder])

    else:
        print("We do not support your platform: {}".format(my_sys))



def main():
    print_header()
    out = get_create_output_folder()
    print('Found or created folder: {}'.format (out))
    download_cats(out)
    display_cats(out)


def print_header():
    print('--------------------')
    print('      LOL CATS')
    print('--------------------')
    print()


def get_create_output_folder():
    base_folder = os.path.dirname ('__file__')
    folder = 'cat_pictures'
    full_path = os.path.join (base_folder, folder)

    if not os.path.exists (full_path) or not os.path.isdir (full_path):
        print('Creating new directory at {}'.format (full_path))
        os.mkdir (full_path)

    return full_path


if __name__ == '__main__':
    main()