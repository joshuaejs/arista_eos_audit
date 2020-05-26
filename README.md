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

The file [audit_eos_files.py](audit_eos_files.py) currently supports the following features.  
To enable or disable them, update the file [input.yml](input.yml).

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
  - some output examples: 
```
********** Power supplies status **********

Power supply: 1 *** Status: ok *** Result: PASS
Power supply: 3 *** Status: ok *** Result: PASS
Power supply: 2 *** Status: ok *** Result: PASS
Power supply: 4 *** Status: ok *** Result: PASS
Power supply: 7 *** Status: ok *** Result: PASS
Power supply: 6 *** Status: ok *** Result: PASS
```
```
********** Power supplies status **********

All tests successfully passed
```
- check_cooling
  - feature description: include tests report about the cooling status
  - required eos command: ```show system environment cooling | json```
  - test failure conditions: A test fails if the status of a fan is not ok
  - some output examples: 
```
********** Cooling status **********

Power supplies: 
Fan: PowerSupply1/1 *** Status: ok *** Result: PASS
Fan: PowerSupply2/1 *** Status: ok *** Result: PASS
Fan: PowerSupply3/1 *** Status: ok *** Result: PASS
Fan: PowerSupply4/1 *** Status: ok *** Result: PASS
Fan: PowerSupply6/1 *** Status: ok *** Result: PASS
Fan: PowerSupply7/1 *** Status: ok *** Result: PASS

Fan modules: 
Fan: 1/1 *** Status: ok *** Result: PASS
Fan: 1/2 *** Status: ok *** Result: PASS
Fan: 1/3 *** Status: ok *** Result: PASS
Fan: 1/4 *** Status: ok *** Result: PASS
Fan: 1/5 *** Status: ok *** Result: PASS
Fan: 2/1 *** Status: ok *** Result: PASS
Fan: 2/2 *** Status: ok *** Result: PASS
Fan: 2/3 *** Status: ok *** Result: PASS
Fan: 2/4 *** Status: ok *** Result: PASS
Fan: 2/5 *** Status: ok *** Result: PASS
Fan: 3/1 *** Status: ok *** Result: PASS
Fan: 3/2 *** Status: ok *** Result: PASS
Fan: 3/3 *** Status: ok *** Result: PASS
Fan: 3/4 *** Status: ok *** Result: PASS
Fan: 3/5 *** Status: ok *** Result: PASS
Fan: 4/1 *** Status: ok *** Result: PASS
Fan: 4/2 *** Status: ok *** Result: PASS
Fan: 4/3 *** Status: ok *** Result: PASS
Fan: 4/4 *** Status: ok *** Result: PASS
Fan: 4/5 *** Status: ok *** Result: PASS
Fan: 5/1 *** Status: ok *** Result: PASS
Fan: 5/2 *** Status: ok *** Result: PASS
Fan: 5/3 *** Status: ok *** Result: PASS
Fan: 5/4 *** Status: ok *** Result: PASS
Fan: 5/5 *** Status: ok *** Result: PASS
Fan: 6/1 *** Status: ok *** Result: PASS
Fan: 6/2 *** Status: ok *** Result: PASS
Fan: 6/3 *** Status: ok *** Result: PASS
Fan: 6/4 *** Status: ok *** Result: PASS
Fan: 6/5 *** Status: ok *** Result: PASS
```
```
********** Cooling status **********

Power supplies: 
All tests successfully passed

Fan modules: 
All tests successfully passed
```
- check_temperature
  - feature description: include tests report about the temperature status
  - required eos command: ```show system environment temperature | json```
  - test failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state. The system temperature test fails if the system status is not OK
  - some output examples: 
```
********** Temperature status **********

System temperature: 
Status: ok *** Result: PASS

Sensors: 
Sensor: TempSensor1 *** Description: Cpu temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 30 *** Max temperature last change: 24 May 2020 18:37:45 *** Result: PASS
Sensor: TempSensor2 *** Description: Rear temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 24 *** Max temperature last change: 25 May 2020 21:36:35 *** Result: PASS
Sensor: TempSensor3 *** Description: Board temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 25 *** Max temperature last change: 26 May 2020 02:29:30 *** Result: PASS
Sensor: TempSensor4 *** Description: Front-panel temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 22 *** Max temperature last change: 25 May 2020 22:58:06 *** Result: PASS
Sensor: TempSensor5 *** Description: Board temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 25 *** Max temperature last change: 26 May 2020 02:29:42 *** Result: PASS
Sensor: TempSensor6 *** Description: FM6000 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 25 *** Max temperature last change: 25 May 2020 20:37:38 *** Result: PASS

Power Supplies: 
Sensor: TempSensorP1/1 *** Description: Power supply sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 21 *** Max temperature last change: 24 May 2020 18:38:15 *** Result: PASS
Sensor: TempSensorP2/1 *** Description: Power supply sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 24 *** Max temperature last change: 24 May 2020 18:38:15 *** Result: PASS
```
```
********** Temperature status **********

System temperature: 
All tests successfully passed

Sensors: 
All tests successfully passed

Card Slot: 
All tests successfully passed

Power Supplies: 
All tests successfully passed
```
- check_temperature_transceivers
  - feature description: include tests report about the transceivers temperature status
  - required eos command: ```show system environment temperature transceiver | json```
  - test failure conditions: Failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state
  - some output examples: 
```
********** Temperature transceivers status **********

Description: Xcvr25 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 52 *** Max temperature last change: 16 May 2020 07:41:02 *** Result: PASS
Description: Xcvr26 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 50 *** Max temperature last change: 16 May 2020 07:44:32 *** Result: PASS
Description: Xcvr49 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 48 *** Max temperature last change: 16 May 2020 07:37:06 *** Result: PASS
Description: Xcvr50 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 47 *** Max temperature last change: 16 May 2020 07:44:07 *** Result: PASS
Description: Xcvr51 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 48 *** Max temperature last change: 16 May 2020 07:44:55 *** Result: PASS
Description: Xcvr52 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 47 *** Max temperature last change: 16 May 2020 07:37:40 *** Result: PASS
```
```
********** Temperature transceivers status **********

All tests successfully passed
```
- check_reload_cause_history
  - feature description: include tests report about the cause for the last 10 reload
  - required eos command: ```show reload cause history | json```
  - test failure conditions: A test fails if a device reload was not requested by user
  - some output examples: 
```
********** Reload cause history **********

Time: 24 May 2020 18:37:55 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
Time: 22 May 2020 13:31:20 *** Reason: Reload requested by the user. *** Result: PASS
Time: 22 May 2020 13:13:42 *** Reason: Reload requested by the user. *** Result: PASS
Time: 21 May 2020 08:38:28 *** Reason: Reload requested by the user. *** Result: PASS
Time: 15 May 2020 15:30:38 *** Reason: Reload requested by the user. *** Result: PASS
Time: 12 May 2020 14:02:28 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
Time: 11 May 2020 17:30:10 *** Reason: Reload requested by the user. *** Result: PASS
Time: 06 May 2020 09:01:29 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
Time: 05 May 2020 18:00:26 *** Reason: Reload requested by the user. *** Result: PASS
Time: 05 May 2020 10:01:52 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
```
```
********** Reload cause history **********

Time: 24 May 2020 18:38:03 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
Time: 21 May 2020 12:58:43 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
Time: 19 May 2020 23:02:10 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
Time: 12 May 2020 14:01:54 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
The other tests succesfully passed

```
- check_reload_cause_full
  - feature description: include tests report about the cause of the most recent reload
  - required eos command: ```show reload cause full | json```
  - test failure conditions: The test fails if the device reload was not requested by user
  - output example: 
```
********** Reload cause full **********
Time: 24 May 2020 18:37:55 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
```
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
  - some output examples: 
```
********** BGP sessions state **********

vrf: default
Peer: 10.10.10.1 *** ASN: 65002 *** State: Established *** Up/Down: 25 May 2020 00:02:56 *** Result: PASS
Peer: 10.10.10.3 *** ASN: 65003 *** State: Established *** Up/Down: 25 May 2020 00:02:53 *** Result: PASS
```
```
********** BGP sessions state **********

vrf: default
Peer: 10.10.10.5 *** ASN: 65003 *** State: Active *** Up/Down: 26 May 2020 13:32:27 *** Result: FAIL
The other tests succesfully passed
```
- check_mlag
  - feature description: include tests report about the mlag status
  - required eos command: ```show mlag detail | json```
  - test failure conditions: The test fails if the MLAG state is active and the negotiation status is not connected
  - some output examples: 
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



 
