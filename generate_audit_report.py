import yaml 
from eos.audit import str_to_function, generate_main_report, generate_failures_only_report, generate_network_main_report, generate_network_failures_only_report

input_f = open('input.yml', 'r')
input_s = input_f.read()
input_f.close()
input = yaml.load(input_s, Loader=yaml.FullLoader)

devices = input['devices']
root_dir = input['output_directory'] 

audit_str_list = input['audit']

audit_func_list = str_to_function (audit_str_list)

for device in devices:
    generate_main_report(device, audit_func_list, root_dir)
    generate_failures_only_report(device, audit_func_list, root_dir)

generate_network_main_report(devices, root_dir, audit_str_list)
generate_network_failures_only_report(devices, root_dir, audit_str_list)
