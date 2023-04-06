import inquirer
from ab import CONFIG as address
from note import CONFIG as note
from clean import CONFIG as clean
from header import Handler


main_menu = [
    inquirer.List('option',
                  message='You are in main menu. Please select an option:',
                  choices=[
                      'Address Book',
                      'Note Book',
                      'Sorter Assist',
                      'Exit'
                  ])
]


def main():
    while True:
        main_choice = inquirer.prompt(main_menu)['option']

        if main_choice == 'Address Book':
            handler = Handler(**address)
            handler.run()

        elif main_choice == 'Note Book':
            handler = Handler(**note)
            handler.run()

        elif main_choice == 'Sorter Assist':
            handler = Handler(**clean)
            handler.run()
        elif main_choice == 'Exit':
            print("Exiting program...")
            break


if __name__ == '__main__':
    main()
