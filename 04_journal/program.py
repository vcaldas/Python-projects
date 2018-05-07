import journal

def print_header():
    print('--------------------')
    print('       Diary')
    print('--------------------')


def list_entries(data):
    print("Your journal entries")

    entries = reversed(data)

    for index, entry in enumerate(entries):
        print("* {0} - {1}".format(index, entry))


def add_entry(data):
    text = input('Type your entry,  <enter> to exit: ')
    data.append(text)



def run_event_loop():
    print("What do you want to do?")
    journal_name = 'Default'
    
    journal_data = journal.load(journal_name)
    cmd = 'EMPTY'

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]add entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)

        elif cmd == 'a':
            add_entry(journal_data)

        elif cmd != 'x' and cmd:
            print(" Sorry. I can't understand {}".format(cmd))

    print("Done.Goodbye")
    journal.save(journal_name, journal_data)


def main():
    print_header()
    run_event_loop()


if __name__ == '__main__':
    main()
