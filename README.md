![GitHub](https://img.shields.io/github/license/ksator/arista_eos_audit)   
 
## Table of content

[About this repository](#about-this-repository)  
[Requirements](#requirements)  
[How to use this repository](#how-to-use-this-repository)  
[Repository details](#repository-details)   

## About this repository 

This repo has python content to collect eos commands from Arista devices.  
It also has python content to audit offline the data collected and to generate a report.  

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

## How to use this repository 

Install the requirements described in the above section.  

Then update the file [input.yml](input.yml). This file has the required input for the files [collect_eos_commands.py](collect_eos_commands.py) and  [audit_eos_files.py](audit_eos_files.py)   

Then run the script [collect_eos_commands.py](collect_eos_commands.py) to collect commands output from EOS devices.  

Once you collected the commands output, you can run this script [audit_eos_files.py](audit_eos_files.py) to generate reports.  

## Repository details 

### [input.yml](input.yml) file 

The file [input.yml](input.yml) has the required input for the files [collect_eos_commands.py](collect_eos_commands.py) and  [audit_eos_files.py](audit_eos_files.py)   
It is used to define these variables:    
- devices: list of EOS devices
- username: devices username 
- password: devices password
- text_cmds: list EOS commands to collect in text format
- json_cmds: list EOS commands to collect in JSON format
- text_and_json_cmds: list EOS commands to collect in text and JSON format 
- output_directory: directory to save the show commands collected and the reports generated
- custom_show_tech_support: list of files (show commands) to include in a custom show tech-support text file. 
- audit: list of topics to audit and to include in the report.  

### [collect_eos_commands.py](collect_eos_commands.py) file 

The file [collect_eos_commands.py](collect_eos_commands.py) uses the variables defined in the file [input.yml](input.yml) to collect show commands from EOS devices.  
It supports collecting show commands in both text and JSON format.  
The commands output is saved in device directory in the [output](output) directory. 

### [custom_show_tech_support.py](custom_show_tech_support.py)

The file [custom_show_tech_support.py](custom_show_tech_support.py) uses the variables defined in the file [input.yml](input.yml) to generate offline a custom show tech-support text file.  

For each devices indicated in [input.yml](input.yml), it assembles the files indicated in [input.yml](input.yml) file to generate offline a custom show tech-support text file.  
It supports only the text format (no JSON format support).  
The name of the output file is "custom show tech-support.txt".  It is saved in device directory in the [output](output) directory. 
  
### [audit_eos_files.py](audit_eos_files.py) file 

The file [audit_eos_files.py](audit_eos_files.py) uses the variables defined in the file [input.yml](input.yml) to audit offline some of the collected files and to generate a report.  

For each device it generates 2 reports: 
- The file "main.txt" includes all the tests. It is saved in device directory in the [output](output) directory. 
- The file "failures_only.txt" includes only the tests that failed. It is saved in device directory in the [output](output) directory. 

It also assembles the devices report in one file: 
- The file [main.txt](output/main.txt) includes for all the devices all the tests. It is saved at the root of the [output](output) directory. 
- The file [failures_only.txt](output/failures_only.txt) includes for all the devices only the tests that failed. It is saved at the root of the [output](output) directory.  

It currently support these features:  
- hostname
  - required eos command: ```show hostname | json```
  - feature description: include the device hostname and fqdn in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt)
  - failure conditions: This is a report without any test so there is no failure/passing condition
- version
  - required eos command: ```show version | json```
  - feature description: include some details regarding the device (HW model, SN, SW release, uptime) in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt) 
  - failure conditions: This is a report without any test so there is no failure/passing condition
- inventory 
  - required eos command: ```show inventory | json```
  - feature description: include tests report about the hardware inventory in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt)
  - failure conditions: A test fails if the manufacturer of a transceiver is not Arista Networks or if a power supply slot has no power supply unit inserted
- power 
  - required eos command: ```show system environment power| json```
  - feature description: include tests report about the power status in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt)
  - failure conditions: A test fails if the status of a power supply is not ok
- cooling
  - required eos command: ```show system environment cooling | json```
  - feature description: include tests report about the cooling status in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt)
  - failure conditions: A test fails if the status of a fan is not ok
- temperature
  - required eos command: ```show system environment temperature | json```
  - feature description: include tests report about the temperature status in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt)
  - failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state. The system temperature test fails if the system status is not OK
- temperature_transceivers
  - required eos command: ```show system environment temperature transceiver | json```
  - feature description: include tests report about the transceivers temperature status in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt)
  - failure conditions: Failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state
- reload_cause_history
  - required eos command: ```show reload cause history | json```
  - feature description: include tests report about the cause for the last 10 reload. 
  - failure conditions: A test fails if a device reload was not requested by user
- reload_cause_full
  - required eos command: ```show reload cause full | json```
  - feature description: include tests report about the cause of the most recent reload. 
  - failure conditions: The test fails if the device reload was not requested by user
- lldp
  - required eos command: ```show lldp neighbors | json```
  - feature description: include the lldp topology in the files [main.txt](output/main.txt) and [failures_only.txt](output/failures_only.txt)
  - failure conditions: This is a report without any test so there is no failure/passing condition
- bgp
  - required eos command: ```show ip bgp summary vrf all | json```
  - feature description: 
  - failure conditions: A test fails if a BGP session is not established
- mlag
  - required eos command: ```show mlag detail | json```
  - feature description: 
  - failure conditions: The test fails if the MLAG state is active and the negotiation status is not connected
  

 

