import os

def main():
    while True:
        print("Welcome to PyOSS Notepad!")
        print("1. Save a new note")
        print("2. Read an existing note")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Enter your note. Press 'Enter' on an empty line to finish:")
            note_lines = []
            while True:
                line = input()
                if not line:
                    break
                note_lines.append(line)

                if note_lines:
                     note_content = '\n'.join(note_lines)
                     filename = input("Enter a filename to save the note: ")
                     with open(filename, 'w') as file:
                        file.write(note_content)
                     print("Note saved successfully!")
                else:
                     print("Note is empty. Not saved.")

        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            filename = input("Enter the filename to read the note: ")
            try:
                with open(filename, 'r') as file:
                     note_content = file.read()
                print("Note:")
                print(note_content)  
            except FileNotFoundError:
                print("File not found.")
            except Exception as e:
                print(f'Error on reading note: {e}')

        elif choice == '3':
             print("Exiting the PyOSS Notepad.")
             break
        else:
            print("Invalid choice. Please try again.")

main()