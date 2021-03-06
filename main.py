import contact_util

def writing_using_try_finally():
    # important to use try/finally to make sure file will be closed 
    # even if an exception is issued
    try:
        # mode: 'r' (read), 'w' (write), 'a' (append), 
        # use '+' with the mode to write and read with the same handle
        # if choose mode is 'a+', the writing operation will be done at the
        # end of the file, ignoring any seek operation
        contact_file = open("data/contacts_iso8859-1-write.csv", encoding='latin_1', mode='w+')

        contacts = ['11,Carol,carol@carol.com.br\n'
                    '12,Ana,ana@ana.com.br\n'
                    '13,Tais,tais@tais.com.br\n'
                    '14,Felipe,felipe@felipe.com.br\n']

        for contact in contacts:
            contact_file.write(contact)

        # flushes the write operatin to file
        contact_file.flush()

        # change file pointer to position 0 (start of file)
        contact_file.seek(0)
        # read a line until '\n'
        print(contact_file.readline())

        contact_file.seek(28)
        contact_file.write('12,Ana,ana@ana.com.br\n'.upper())
        contact_file.flush()
        contact_file.seek(0)

        for line in contact_file:
            print(line, end='')

    finally:
        contact_file.close()


def writing_using_with_as():
    try:
        with open('data/contacts_iso8859-1.csv', encoding='latin_1') as contact_file:
            for line in contact_file:
                print(line, end='')
    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('Writing permission denied')


def reading_file_using_csv_to_contacts():
    try:
        contacts = contact_util.csv_to_contacts('data/contacts_iso8859-1.csv')

        for contact in contacts:
            print(f'{contact.id} - {contact.name} - {contact.email}')

    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('Writing permission denied')


def convert_contacts_to_pickle():
    try:
        # reads csv and convert it to contacts
        contacts = contact_util.csv_to_contacts('data/contacts_iso8859-1.csv')
        # save contacts to pickle file
        contact_util.contacts_to_pickle(contacts, 'data/contacts.pickle')
        # reads from pickle and convert it back to contacts
        contacts = contact_util.pickle_to_contacts('data/contacts.pickle')

        for contact in contacts:
            print(f'{contact.id} - {contact.name} - {contact.email}')

    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('Writing permission denied')


def convert_contacts_to_json():
    try:
        # reads csv and convert it to contacts
        contacts = contact_util.csv_to_contacts('data/contacts_iso8859-1.csv')
        # save contacts to json
        contact_util.contacts_to_json(contacts, 'data/contacts.json')
        # reads from json and convert it back to contacts
        contacts = contact_util.json_to_contact('data/contacts.json')

        for contact in contacts:
            print(f'{contact.id} - {contact.name} - {contact.email}')

    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('Writing permission denied')


convert_contacts_to_json()