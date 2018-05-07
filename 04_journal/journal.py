"""
This is the journal module.
"""
import os


def load(name):
    """
    This method loads or create a new journal
    :param name: Journal name to load
    :return: Journal data populated
    """
    filename = get_full_pathname(name)
    data = []

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for entry in file.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method saves the journal to a file
    :param name: The journal name to save
    :param journal_data: The data of the journal
    """
    filename = get_full_pathname(name)

    print('Saving to: {}'.format(filename))

    with open(filename, 'w') as file:

        for entry in journal_data:
            file.write(entry + '\n')


def get_full_pathname(name):
    """

    :param name: Name of the file
    :return:
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
