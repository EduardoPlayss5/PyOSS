import os
import builtins

def run_app(app_filename):
    if not os.path.exists(app_filename):
        print(f"Application '{app_filename}' not found.")
        return
    
    with open(app_filename, 'r') as app_file:
        app_code = app_file.read()

    print(f"Running app from '{app_filename}'")
    builtins.exec(app_code)
    print()
    print()
    print()
    print("App execution completed.")