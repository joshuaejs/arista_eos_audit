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

It is used to define the variables for the files [collect_eos_commands.py](collect_eos_commands.py) and [audit_eos_files.py](audit_eos_files.py):    
- devices: list of EOS devices
- username: devices username 
- password: devices password
- text_cmds: list EOS commands to collect in text format
- json_cmds: list EOS commands to collect in json format
- text_and_json_cmds: list EOS commands to collect in text and json format 
- output_directory: directory to save the show commands collected and the reports generated
- custom_show_tech_support: list of files (EOS show commands) to include in a custom show tech support file. 
- audit: list of audit features to use. This repository currently supports   

  

The file [collect_eos_commands.py](collect_eos_commands.py) uses the variables defined in the file [input.yml](input.yml) to collect EOS show commands from devices.   

The file [audit_eos_files.py](audit_eos_files.py) uses the variables defined in the file [input.yml](input.yml) to audit the collected files and to generate a report.   

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


