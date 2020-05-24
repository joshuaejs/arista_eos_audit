import os
import yaml

input_f = open('input.yml', 'r')
input_s = input_f.read()
input_f.close()
input = yaml.load(input_s, Loader=yaml.FullLoader)

devices = input['devices']
output_directory = input['output_directory'] 
custom_show_tech_support = input['custom_show_tech_support']

cwd = os.getcwd()
output_directory = os.path.dirname(cwd + "/" + output_directory + "/")

# assemble some of the collected txt files into one large file
for device in devices: 
    device_directory = output_directory + '/' + device
    eos_commands_directory = device_directory + '/' + "eos_commands"   
    text_directory = eos_commands_directory + '/' + "text"  
    outfile = open(text_directory + "/custom show tech-support.txt", "w")   
    for item in custom_show_tech_support: 
        infile = open(text_directory + "/" + item + ".txt", "r")
        outfile.write('-'*13 + ' ' + item + ' ' + '-'*13 + '\n'*2)
        for line in infile:  
            outfile.write(line)
        outfile.write('\n'*2)
        infile.close()
    outfile.close()
