import yaml 
from eos.audit import *

input_f = open('input.yml', 'r')
input_s = input_f.read()
input_f.close()
input = yaml.load(input_s, Loader=yaml.FullLoader)

devices = input['devices']
root_dir = input['output_directory'] 

audit_str_list = input['audit']
str_to_function = {'print_hostname': print_hostname, 'print_version': print_version, 'check_inventory': check_inventory, 'check_power': check_power, 'check_cooling': check_cooling, 'check_temperature': check_temperature, 'check_temperature_transceivers': check_temperature_transceivers, 'check_reload_cause_history': check_reload_cause_history, 'check_reload_cause_full': check_reload_cause_full, 'print_lldp': print_lldp, 'check_bgp': check_bgp, 'check_mlag': check_mlag} 
audit_func_list = []
for item in audit_str_list : 
    audit_func_list.append(str_to_function[item])

for device in devices:
    generate_main_report(device, audit_func_list, root_dir)
    generate_failures_only_report(device, audit_func_list, root_dir)

generate_network_main_report(devices, root_dir, audit_str_list)
generate_network_failures_only_report(devices, root_dir, audit_str_list)
