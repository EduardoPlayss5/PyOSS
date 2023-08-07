def catFile(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error on reading file. {e}")