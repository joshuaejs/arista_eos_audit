![GitHub](https://img.shields.io/github/license/ksator/arista_eos_audit)   
 
## Table of content

[About this repository](#about-this-repository)  
[Repository details](#repository-details)   
[Requirements](#requirements)  

## About this repository 

This repo has python content to collect eos commands from Arista devices.  
It also has python content to audit offine the data collected and to generate a report.  

## Repository details 

The file [input.yml](input.yml) has the required input for the files [collect_eos_commands.py](collect_eos_commands.py) and  [audit_eos_files.py](audit_eos_files.py)   
It is used to define these variables:    
- devices: list of EOS devices
- username: devices username 
- password: devices password
- text_cmds: list EOS commands to collect in text format
- json_cmds: list EOS commands to collect in JSON format
- text_and_json_cmds: list EOS commands to collect in text and JSON format 
- output_directory: directory to save the show commands collected and the reports generated
- custom_show_tech_support: list of files (EOS show commands) to include in a custom show tech-support support file. 
- audit: list of topics to audit and include in the report.  

The file [collect_eos_commands.py](collect_eos_commands.py) uses the variables defined in the file [input.yml](input.yml) to collect show commands from EOS devices.  
It supports collecting show commands in both text and JSON format.  
The commands output is saved in this [directory](output/eos_commands)

The file [audit_eos_files.py](audit_eos_files.py) uses the variables defined in the file [input.yml](input.yml) to audit offline some of the collected files and to generate a report.  
It generates for each device 2 reports: 
- A ```main.txt``` file. It include all the tests. Here's an example [main.txt](main.txt) 
- A ```failures only.txt``` file. It include only the test that failed. Here's an example [failures only.txt](failures only.txt)
It also assemble the devices report in one file: 
- [main.txt](main.txt) 
- [failures only.txt](failures only.txt)
It currently support these features:  
- hostname
  - description: add to the report the device hostname and fqdn 
  - requirements: ```show hostname | json```
  - failure conditions: This is a report without any test so there is no failure/passing condition
- version
  - description: add to the reports some details regarding the device (HW model, SN, SW release, uptime)
  - requirements: ```show version | json```
  - Failure conditions: This is a report without any test so there is no failure/passing condition
- inventory 
  - requirements: ```show inventory | json```
  - requirements:
  - Failure conditions: 
- power 
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- cooling
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- temperature
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- temperature_transceivers
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- reload_cause_history
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- reload_cause_full
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- lldp
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- bgp
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
- mlag
  - requirements: ```| json```
  - requirements:
  - Failure conditions: 
  
## Requirements

I am using this Python version
```
python -V
Python 3.7.7
```
And I installed netmiko to interact with EOS devices.  
```
pip freeze | grep netmiko
netmiko==3.1.1
```


