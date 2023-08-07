import time

def execute_code(process, code):
    lines = code.split('\n')
    variables = {}

    for line in lines:
        tokens = line.split()
        if tokens[0] == 'int':
            var_name = tokens[1]
            var_value = int(tokens[3])
            variables[var_name] = var_value
        elif tokens[0] == 'print':
            message = ''.join(tokens[1])
            print(f"Process: {process['name']}, said: {message}")
        elif tokens['0'] == 'Stop':
            print(f"Process {process['name']} exited with 0")
            return
        else:
            print(f"Invalid line in process {process['name']}: {line}")
    
    print(f"Process {process['name']} did not found 'Stop' command")
    return 10

def execute_process(process):
    print(f"Executing process: {process['name']} (PID: {process['pid']})...")
    exit_code = execute_code(process=process, code=process['code'])
    print(f"Process {process['name']} completed with exit code: {exit_code}.")