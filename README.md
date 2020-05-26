![GitHub](https://img.shields.io/github/license/ksator/arista_eos_audit)   
 
## Table of content

[About this repository](#about-this-repository)  
[Requirements](#requirements)  
[How to use this repository](#how-to-use-this-repository)  
[Repository details](#repository-details)   
&nbsp;&nbsp;&nbsp;&nbsp;[Repository input](#repository-input)    
&nbsp;&nbsp;&nbsp;&nbsp;[Collect EOS commands](#collect-eos-commands)  
&nbsp;&nbsp;&nbsp;&nbsp;[Build a custom show tech-support file](#build-a-custom-show-tech-support-file)  
&nbsp;&nbsp;&nbsp;&nbsp;[Generate audit reports](#generate-audit-reports)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Overview](#overview)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Supported features](#supported-features)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Report files](#report-files)  

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

Then update the file [input.yml](input.yml). It has the required input for the various scripts available in this repository.   

Then you can run the script [collect_eos_commands.py](collect_eos_commands.py) to collect commands output from EOS devices.  

Once you collected the commands output, you can run the script [audit_eos_files.py](audit_eos_files.py) to generate reports.  

## Repository details 

### Repository input 

The file [input.yml](input.yml) has the required input for the files
- [collect_eos_commands.py](collect_eos_commands.py) 
- [custom_show_tech_support.py](custom_show_tech_support.py) 
- [audit_eos_files.py](audit_eos_files.py)   

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

### Collect EOS commands

The file [collect_eos_commands.py](collect_eos_commands.py) uses the variables defined in the file [input.yml](input.yml) to collect show commands from EOS devices.  
It supports collecting show commands in both text and JSON format.  
The commands output is saved in device directory in the [output](output) directory. 

### Build a custom show tech-support file 

The file [custom_show_tech_support.py](custom_show_tech_support.py) uses the variables defined in the file [input.yml](input.yml) to generate offline a custom show tech-support text file.  
For each devices indicated in [input.yml](input.yml), it assembles the files indicated in [input.yml](input.yml) file to generate offline a custom show tech-support text file.  
It supports only the text format (no JSON format support).  
The name of the output file is "custom show tech-support.txt".  It is saved in device directory in the [output](output) directory. 
  
### Generate audit reports

#### Overview 

The file [audit_eos_files.py](audit_eos_files.py) uses the variables defined in the file [input.yml](input.yml) to audit offline some of the collected files and to generate a report.  

#### Supported features 

The file [audit_eos_files.py](audit_eos_files.py) currently supports the following features. To enable or disable them, update the file [input.yml](input.yml).

- print_hostname
  - feature description: include the device hostname and fqdn
  - required eos command: ```show hostname | json```
  - test failure conditions: This is a report without any test so there is no failure/passing condition
  - output example: 
```
********** Device hostname **********

Hostname: switch1
FQDN: switch1.lab.local
```
- print_version
  - feature description: include some details regarding the device (HW model, SN, SW release, uptime)
  - required eos command: ```show version | json```
  - test failure conditions: This is a report without any test so there is no failure/passing condition
  - output example: 
```
********** Device details **********

Model: DCS-7150S-64-CL-F
Serial number: JPE14210677
Version: 4.22.4M-2GB
Uptime: 1 day, 6:28:38
```

- check_inventory 
  - feature description: include tests report about the hardware inventory
  - required eos command: ```show inventory | json```
  - test failure conditions: A test fails if the manufacturer of a transceiver is not Arista Networks or if a power supply slot has no power supply unit inserted

  
- check_power 
  - feature description: include tests report about the power status
  - required eos command: ```show system environment power| json```
  - test failure conditions: A test fails if the status of a power supply is not ok  
  - output example: 
```
********** Power supplies **********

Power supply: 1 *** Status: powerLoss *** Result: FAIL
Power supply: 2 *** Status: ok *** Result: PASS
```

- check_cooling
  - feature description: include tests report about the cooling status
  - required eos command: ```show system environment cooling | json```
  - test failure conditions: A test fails if the status of a fan is not ok
  - output example: 
```
********** Cooling **********

Power supplies: 
Fan: PowerSupply1/1 *** Status: ok *** Result: PASS
Fan: PowerSupply2/1 *** Status: ok *** Result: PASS

Fan modules: 
Fan: 1/1 *** Status: ok *** Result: PASS
Fan: 2/1 *** Status: ok *** Result: PASS
Fan: 3/1 *** Status: ok *** Result: PASS
Fan: 4/1 *** Status: ok *** Result: PASS
```
- check_temperature
  - feature description: include tests report about the temperature status
  - required eos command: ```show system environment temperature | json```
  - test failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state. The system temperature test fails if the system status is not OK
  
- check_temperature_transceivers
  - feature description: include tests report about the transceivers temperature status
  - required eos command: ```show system environment temperature transceiver | json```
  - test failure conditions: Failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state
  
- check_reload_cause_history
  - feature description: include tests report about the cause for the last 10 reload
  - required eos command: ```show reload cause history | json```
  - test failure conditions: A test fails if a device reload was not requested by user

- check_reload_cause_full
  - feature description: include tests report about the cause of the most recent reload
  - required eos command: ```show reload cause full | json```
  - test failure conditions: The test fails if the device reload was not requested by user

- print_lldp
  - feature description: include the lldp topology
  - required eos command: ```show lldp neighbors | json```
  - test failure conditions: This is a report without any test so there is no failure/passing condition
  - output examples
```
********** LLDP topology **********

Interface: Ethernet1 *** LLDP neighbor: switch2.lab.local *** LLDP remote port: Ethernet1
Interface: Ethernet2 *** LLDP neighbor: switch3.lab.local *** LLDP remote port: Ethernet1
Interface: Management1 *** LLDP neighbor: mgmt0a.lab.local *** LLDP remote port: Ethernet37
```
 
- check_bgp
  - feature description: include tests report about the bgp status for all configured vrf
  - required eos command: ```show ip bgp summary vrf all | json```
  - test failure conditions: A test fails if a BGP session is not established

- check_mlag
  - feature description: include tests report about the mlag status
  - required eos command: ```show mlag detail | json```
  - test failure conditions: The test fails if the MLAG state is active and the negotiation status is not connected
  - output examples: 
 
```
 ********** MLAG **********

Peer: 192.168.10.2
State: active
Negotiation Status: connected
Config Sanity: consistent

Test result: PASS
 ``` 
 ```
  ********** MLAG **********

MLAG is disabled
 ```

#### Report files

For each device defined in the file [input.yml](input.yml), the file [audit_eos_files.py](audit_eos_files.py) generates 2 reports:
- The file "main.txt" includes details regarding all the tests for this device. It is saved in device directory in the [output](output) directory. 
- The file "failures_only.txt" includes only the tests that failed for this device. It is saved in device directory in the [output](output) directory. 

Then, the file [audit_eos_files.py](audit_eos_files.py) assembles the report of each device into one file: 
- The file [main.txt](output/main.txt) includes for all the devices all the tests. It is saved at the root of the [output](output) directory. 
- The file [failures_only.txt](output/failures_only.txt) includes for all the devices only the tests that failed. It is saved at the root of the [output](output) directory.  



 
