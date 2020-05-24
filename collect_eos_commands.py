"""
python -V
Python 3.7.7

pip freeze | grep netmiko
netmiko==3.1.1
"""

from netmiko import ConnectHandler
import os
import yaml

input_f = open('input.yml', 'r')
input_s = input_f.read()
input_f.close()
input = yaml.load(input_s, Loader=yaml.FullLoader)

devices = input['devices']
output_directory = input['output_directory'] 
username = input['username']
password = input['password']
text_cmds = input['text_cmds']
json_cmds = input['json_cmds'] 
text_and_json_cmds = input['text_and_json_cmds']

# Create directories to save the commands output
cwd = os.getcwd()
output_directory = os.path.dirname(cwd + "/" + output_directory + "/")
for device in devices:
    device_directory = output_directory + '/' + device
    eos_commands_directory = device_directory + '/' + "eos_commands"
    json_directory = eos_commands_directory + '/' + "json"    
    text_directory = eos_commands_directory + '/' + "text"  
    for directory in [output_directory, device_directory, eos_commands_directory, json_directory, text_directory]: 
        if not os.path.exists(directory):
            os.makedirs(directory)
    # collect show commands
    print("opening connection to " + device)
    switch = {'device_type': 'arista_eos', 'host': device, 'username': username, 'password': password, 'port': '22', 'timeout': 180}
    connection = ConnectHandler(**switch)
    print("collecting show commands on device " + device)
    # collect text commands
    if text_cmds is not None: 
        for cmd in text_cmds: 
            print("collecting " + cmd)
            cmd_output = connection.send_command(cmd)
            f=open(text_directory + "/" + cmd + ".txt", "w")
            f.write(cmd_output)
            f.closed
    if (text_and_json_cmds is not None) and (text_cmds is not None) : 
        for cmd in text_and_json_cmds: 
            if cmd not in text_cmds: 
                print("collecting " + cmd)
                cmd_output = connection.send_command(cmd)
                f=open(text_directory + "/" + cmd + ".txt", "w")
                f.write(cmd_output)
                f.closed
    elif (text_and_json_cmds is not None) and (text_cmds is None):
        for cmd in text_and_json_cmds: 
            print("collecting " + cmd)
            cmd_output = connection.send_command(cmd)
            f=open(text_directory + "/" + cmd + ".txt", "w")
            f.write(cmd_output)
            f.closed
    # collect json commands
    if json_cmds is not None: 
        for cmd in json_cmds: 
            print("collecting " + cmd + "| json")
            cmd_output = connection.send_command(cmd + "| json")
            f=open(json_directory + "/" + cmd + ".json", "w")
            f.write(cmd_output)
            f.closed
    if (text_and_json_cmds is not None) and (json_cmds is not None) : 
        for cmd in text_and_json_cmds: 
            if cmd not in json_cmds: 
                print("collecting " + cmd + "| json")
                cmd_output = connection.send_command(cmd + "| json")
                f=open(json_directory + "/" + cmd + ".json", "w")
                f.write(cmd_output)
                f.closed
    elif (text_and_json_cmds is not None) and (json_cmds is None):
        for cmd in text_and_json_cmds: 
            print("collecting " + cmd + "| json")
            cmd_output = connection.send_command(cmd + "| json")
            f=open(json_directory + "/" + cmd + ".json", "w")
            f.write(cmd_output)
            f.closed
    print("closing connection to " + device)
    connection.disconnect()


