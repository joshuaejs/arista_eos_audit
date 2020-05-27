![GitHub](https://img.shields.io/github/license/ksator/arista_eos_audit)   
 
## Table of content

[About this repository](#about-this-repository)  
[Requirements](#requirements)  
[How to use this repository](#how-to-use-this-repository)  
[Repository details](#repository-details)  
&nbsp;&nbsp;&nbsp;&nbsp;[input.yml file](#inputyml-file)  
&nbsp;&nbsp;&nbsp;&nbsp;[audit directory](#audit-directory)   
&nbsp;&nbsp;&nbsp;&nbsp;[collect_eos_commands.py file](#collect_eos_commandspy-file)  
&nbsp;&nbsp;&nbsp;&nbsp;[custom_show_tech_support.py file](#custom_show_tech_supportpy-file)  
&nbsp;&nbsp;&nbsp;&nbsp;[generate_audit_report.py file](#generate_audit_reportpy-file)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Overview](#overview)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Report files](#report-files)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Supported audit features](#supported-audit-features)  

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

If you want to generate offline a custom show tech-support text file, run the script [custom_show_tech_support.py](custom_show_tech_support.py).  

Once you collected the commands output, you can run the script [generate_audit_report.py](generate_audit_report.py) to generate reports.  

## Repository details 

### [input.yml](input.yml) file 

This is the repository input.   

The file [input.yml](input.yml) has the required input for the files
- [collect_eos_commands.py](collect_eos_commands.py) 
- [custom_show_tech_support.py](custom_show_tech_support.py) 
- [generate_audit_report.py](generate_audit_report.py)   

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

### audit directory 

The [audit](audit) directory is a python package that has python functions.  
Some of these functions are imported by the pythons scritps of this repository ([collect_eos_commands.py](collect_eos_commands.py), [custom_show_tech_support.py](custom_show_tech_support.py), [generate_audit_report.py](generate_audit_report.py))

### [collect_eos_commands.py](collect_eos_commands.py) file 

It is used to collect EOS commands.  

It uses the variables defined in the file [input.yml](input.yml) to collect show commands from EOS devices.  
It supports collecting show commands in both text and JSON format.  
The commands output is saved in device directory in the [output](output) directory. 

<details><summary>click me to see the output structure</summary>
<p>

```
output/10.83.28.122/eos_commands
├── json
│   ├── show\ hostname.json
│   ├── show\ interfaces\ description.json
│   ├── show\ inventory.json
│   ├── show\ ip\ bgp\ summary\ vrf\ all.json
│   ├── show\ lldp\ neighbors.json
│   ├── show\ mlag\ detail.json
│   ├── show\ reload\ cause\ full.json
│   ├── show\ reload\ cause\ history.json
│   ├── show\ system\ environment\ cooling.json
│   ├── show\ system\ environment\ power.json
│   ├── show\ system\ environment\ temperature\ transceiver.json
│   ├── show\ system\ environment\ temperature.json
│   └── show\ version.json
└── text
    ├── custom\ show\ tech-support.txt
    ├── show\ hostname.txt
    ├── show\ interfaces\ description.txt
    ├── show\ inventory.txt
    ├── show\ ip\ bgp\ summary\ vrf\ all.txt
    ├── show\ lldp\ neighbors.txt
    ├── show\ logging\ system.txt
    ├── show\ mlag\ detail.txt
    ├── show\ reload\ cause\ full.txt
    ├── show\ reload\ cause\ history.txt
    ├── show\ running-config.txt
    ├── show\ system\ environment\ cooling.txt
    ├── show\ system\ environment\ power.txt
    ├── show\ system\ environment\ temperature\ transceiver.txt
    ├── show\ system\ environment\ temperature.txt
    └── show\ version.txt
output/10.83.28.203/eos_commands
├── json
│   ├── show\ hostname.json
│   ├── show\ interfaces\ description.json
│   ├── show\ inventory.json
│   ├── show\ ip\ bgp\ summary\ vrf\ all.json
│   ├── show\ lldp\ neighbors.json
│   ├── show\ mlag\ detail.json
│   ├── show\ reload\ cause\ full.json
│   ├── show\ reload\ cause\ history.json
│   ├── show\ system\ environment\ cooling.json
│   ├── show\ system\ environment\ power.json
│   ├── show\ system\ environment\ temperature\ transceiver.json
│   ├── show\ system\ environment\ temperature.json
│   └── show\ version.json
└── text
    ├── custom\ show\ tech-support.txt
    ├── show\ hostname.txt
    ├── show\ interfaces\ description.txt
    ├── show\ inventory.txt
    ├── show\ ip\ bgp\ summary\ vrf\ all.txt
    ├── show\ lldp\ neighbors.txt
    ├── show\ logging\ system.txt
    ├── show\ mlag\ detail.txt
    ├── show\ reload\ cause\ full.txt
    ├── show\ reload\ cause\ history.txt
    ├── show\ running-config.txt
    ├── show\ system\ environment\ cooling.txt
    ├── show\ system\ environment\ power.txt
    ├── show\ system\ environment\ temperature\ transceiver.txt
    ├── show\ system\ environment\ temperature.txt
    └── show\ version.txt
output/10.83.28.217/eos_commands
├── json
│   ├── show\ hostname.json
│   ├── show\ interfaces\ description.json
│   ├── show\ inventory.json
│   ├── show\ ip\ bgp\ summary\ vrf\ all.json
│   ├── show\ lldp\ neighbors.json
│   ├── show\ mlag\ detail.json
│   ├── show\ reload\ cause\ full.json
│   ├── show\ reload\ cause\ history.json
│   ├── show\ system\ environment\ cooling.json
│   ├── show\ system\ environment\ power.json
│   ├── show\ system\ environment\ temperature\ transceiver.json
│   ├── show\ system\ environment\ temperature.json
│   └── show\ version.json
└── text
    ├── custom\ show\ tech-support.txt
    ├── show\ hostname.txt
    ├── show\ interfaces\ description.txt
    ├── show\ inventory.txt
    ├── show\ ip\ bgp\ summary\ vrf\ all.txt
    ├── show\ lldp\ neighbors.txt
    ├── show\ logging\ system.txt
    ├── show\ mlag\ detail.txt
    ├── show\ reload\ cause\ full.txt
    ├── show\ reload\ cause\ history.txt
    ├── show\ running-config.txt
    ├── show\ system\ environment\ cooling.txt
    ├── show\ system\ environment\ power.txt
    ├── show\ system\ environment\ temperature\ transceiver.txt
    ├── show\ system\ environment\ temperature.txt
    └── show\ version.txt
```
</p>
</details>

### [custom_show_tech_support.py](custom_show_tech_support.py) file 

It is used to build a custom show tech-support file.  

It uses the variables defined in the file [input.yml](input.yml) to generate offline a custom show tech-support text file.  
For each devices indicated in [input.yml](input.yml), it assembles the files (based on what is indicated in [input.yml](input.yml) file) to generate offline a custom show tech-support text file.  
It supports only the text format (no JSON format support).  
The name of the output file is "custom show tech-support.txt".  It is saved in device directory in the [output](output) directory. 

```
tree output/*/eos_commands/text -f  | grep custom
├── output/10.83.28.122/eos_commands/text/custom\ show\ tech-support.txt
├── output/10.83.28.203/eos_commands/text/custom\ show\ tech-support.txt
├── output/10.83.28.217/eos_commands/text/custom\ show\ tech-support.txt
```

### [generate_audit_report.py](generate_audit_report.py) file 

It is used to generate audit reports.  

#### Overview 

The file [generate_audit_report.py](generate_audit_report.py) uses the variables defined in the file [input.yml](input.yml) to audit offline some of the collected files and to generate a report.  

#### Report files

For each device defined in the file [input.yml](input.yml), the file [generate_audit_report.py](generate_audit_report.py) generates 2 reports in the "report" directory:
- The file "main.txt" includes details regarding all the tests [generate_audit_report.py](generate_audit_report.py) ran for this device. 
- The file "failures_only.txt" includes only the tests that failed for this device. 

<details><summary>click me to see the output structure</summary>
<p>

```
output/10.83.28.122/reports
├── failures_only
│   ├── check_bgp.txt
│   ├── check_cooling.txt
│   ├── check_inventory.txt
│   ├── check_mlag.txt
│   ├── check_power.txt
│   ├── check_reload_cause_full.txt
│   ├── check_reload_cause_history.txt
│   ├── check_temperature.txt
│   ├── check_temperature_transceivers.txt
│   ├── init.txt
│   ├── print_hostname.txt
│   ├── print_lldp.txt
│   └── print_version.txt
├── failures_only.txt
├── main
│   ├── check_bgp.txt
│   ├── check_cooling.txt
│   ├── check_inventory.txt
│   ├── check_mlag.txt
│   ├── check_power.txt
│   ├── check_reload_cause_full.txt
│   ├── check_reload_cause_history.txt
│   ├── check_temperature.txt
│   ├── check_temperature_transceivers.txt
│   ├── init.txt
│   ├── print_hostname.txt
│   ├── print_lldp.txt
│   └── print_version.txt
└── main.txt
output/10.83.28.203/reports
├── failures_only
│   ├── check_bgp.txt
│   ├── check_cooling.txt
│   ├── check_inventory.txt
│   ├── check_mlag.txt
│   ├── check_power.txt
│   ├── check_reload_cause_full.txt
│   ├── check_reload_cause_history.txt
│   ├── check_temperature.txt
│   ├── check_temperature_transceivers.txt
│   ├── init.txt
│   ├── print_hostname.txt
│   ├── print_lldp.txt
│   └── print_version.txt
├── failures_only.txt
├── main
│   ├── check_bgp.txt
│   ├── check_cooling.txt
│   ├── check_inventory.txt
│   ├── check_mlag.txt
│   ├── check_power.txt
│   ├── check_reload_cause_full.txt
│   ├── check_reload_cause_history.txt
│   ├── check_temperature.txt
│   ├── check_temperature_transceivers.txt
│   ├── init.txt
│   ├── print_hostname.txt
│   ├── print_lldp.txt
│   └── print_version.txt
└── main.txt
output/10.83.28.217/reports
├── failures_only
│   ├── check_bgp.txt
│   ├── check_cooling.txt
│   ├── check_inventory.txt
│   ├── check_mlag.txt
│   ├── check_power.txt
│   ├── check_reload_cause_full.txt
│   ├── check_reload_cause_history.txt
│   ├── check_temperature.txt
│   ├── check_temperature_transceivers.txt
│   ├── init.txt
│   ├── print_hostname.txt
│   ├── print_lldp.txt
│   └── print_version.txt
├── failures_only.txt
├── main
│   ├── check_bgp.txt
│   ├── check_cooling.txt
│   ├── check_inventory.txt
│   ├── check_mlag.txt
│   ├── check_power.txt
│   ├── check_reload_cause_full.txt
│   ├── check_reload_cause_history.txt
│   ├── check_temperature.txt
│   ├── check_temperature_transceivers.txt
│   ├── init.txt
│   ├── print_hostname.txt
│   ├── print_lldp.txt
│   └── print_version.txt
└── main.txt
```
</p>
</details>

Then, the file [generate_audit_report.py](generate_audit_report.py): 
- Assembles the "main.txt" report of each device into one [main.txt](output/main.txt) file. So [main.txt](output/main.txt) includes all the tests [generate_audit_report.py](generate_audit_report.py) ran for all the devices. It is saved at the root of the [output](output) directory.  
- Assembles the "failures_only.txt" report of each device into one [failures_only.txt](output/failures_only.txt) file. So [failures_only.txt](output/failures_only.txt) includes for all the devices only the tests that failed. It is saved at the root of the [output](output) directory. 

#### Supported audit features 

The file [generate_audit_report.py](generate_audit_report.py) imports python functions from the [audit](audit) python package

To enable or disable audit features on [generate_audit_report.py](generate_audit_report.py), update the file [input.yml](input.yml).  

The following audit features are currently supported: 

##### print_hostname

Description: include the device hostname and fqdn  
Required eos command: ```show hostname | json```  
Test failure conditions: This is a report without any test so there is no failure/passing condition  
<details><summary>click me to see an output example</summary>
<p>

```
********** Device hostname **********

Hostname: switch1
FQDN: switch1.lab.local
```
</p>
</details>

##### print_version

Description: include some details regarding the device (HW model, SN, SW release, uptime)  
Required eos command: ```show version | json```  
Test failure conditions: This is a report without any test so there is no failure/passing condition  
<details><summary>click me to see an output example</summary>
<p>

```
********** Device details **********

Model: DCS-7150S-64-CL-F
Serial number: JPE14210677
Version: 4.22.4M-2GB
Uptime: 1 day, 19:56:35
```
</p>
</details>

##### check_inventory 

Description: include tests report about the hardware inventory  
Required eos command: ```show inventory | json```  
Test failure conditions: A test fails if the manufacturer of a transceiver is neither "Arista Networks" nor "Arastra, Inc", or if a power supply slot has no power supply unit inserted  
<details><summary>click me to see an output example</summary>
<p>

```
********** Device inventory **********

Device description: 48-port SFP+ 40GigE 1RU + Clock

Power Supplies: 
Slot: 1 *** Model: PWR-460AC-F *** SN: K192MD00A31CZ *** Result: PASS
Slot: 2 *** Model: PWR-460AC-F *** SN: K192MD00A21CZ *** Result: PASS

Fan modules: 
Module: 1 *** Model: FAN-7000-F
Module: 3 *** Model: FAN-7000-F
Module: 2 *** Model: FAN-7000-F
Module: 4 *** Model: FAN-7000-F

Transceivers: 
Port: 1 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-2M *** SN: XHC14082G37V *** Result: PASS
Port: 15 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-3M *** SN: XHC110330103 *** Result: PASS
Port: 2 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-3M *** SN: XHC16463G3XJ *** Result: PASS
Port: 24 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-1M *** SN: XHC14031G1CX *** Result: PASS
Port: 3 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-2M *** SN: XHC13262G2D1 *** Result: PASS
Port: 4 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-2M *** SN: XHC12422G2EJ *** Result: PASS
Port: 47 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-1M *** SN: XHC105110215 *** Result: PASS
Port: 48 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-1M *** SN: XHC14031G1DA *** Result: PASS
Port: 5 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-3M *** SN: XHC110330104 *** Result: PASS
Port: 6 *** Manufacturer: Arista Networks *** Model: CAB-SFP-SFP-2M *** SN: XHC103220430 *** Result: PASS
Port: 7 *** Manufacturer: Arista Networks *** Model: CAB-Q-S-2M *** SN: XHC1133L007Q *** Result: PASS
Port: 8 *** Manufacturer: Arista Networks *** Model: CAB-Q-S-2M *** SN: XHC1133L0082 *** Result: PASS
```
</p>
</details>

##### check_power 

Description: include tests report about the power status  
Required eos command: ```show system environment power| json```  
Test failure conditions: A test fails if the status of a power supply is not ok   
<details><summary>click me to see an output example</summary>
<p>

```
********** Power supplies status **********

Power supply: 1 *** Status: powerLoss *** Result: FAIL
Power supply: 2 *** Status: ok *** Result: PASS
```  
</p>
</details>

##### check_cooling

Description: include tests report about the cooling status  
Required eos command: ```show system environment cooling | json```  
Test failure conditions: A test fails if the status of a fan is not ok  
<details><summary>click me to see an output example</summary>
<p>

```
********** Cooling status **********

Power supplies: 
Fan: PowerSupply1/1 *** Status: ok *** Result: PASS
Fan: PowerSupply2/1 *** Status: ok *** Result: PASS

Fan modules: 
Fan: 1/1 *** Status: ok *** Result: PASS
Fan: 2/1 *** Status: ok *** Result: PASS
Fan: 3/1 *** Status: ok *** Result: PASS
Fan: 4/1 *** Status: ok *** Result: PASS
```
</p>
</details>

##### check_temperature
  
Description: include tests report about the temperature status  
Required eos command: ```show system environment temperature | json```  
Test failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state. The system temperature test fails if the system status is not OK  
<details><summary>click me to see an output example</summary>
<p>

```
********** Temperature status **********

System temperature: 
Status: ok *** Result: PASS

Sensors: 
Sensor: TempSensor1 *** Description: Cpu temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 30 *** Max temperature last change: 24 May 2020 18:37:45 *** Result: PASS
Sensor: TempSensor2 *** Description: Rear temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 26 *** Max temperature last change: 26 May 2020 11:27:55 *** Result: PASS
Sensor: TempSensor3 *** Description: Board temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 27 *** Max temperature last change: 26 May 2020 11:39:07 *** Result: PASS
Sensor: TempSensor4 *** Description: Front-panel temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 23 *** Max temperature last change: 26 May 2020 11:38:01 *** Result: PASS
Sensor: TempSensor5 *** Description: Board temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 27 *** Max temperature last change: 26 May 2020 11:38:01 *** Result: PASS
Sensor: TempSensor6 *** Description: FM6000 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 28 *** Max temperature last change: 26 May 2020 11:12:32 *** Result: PASS

Power Supplies: 
Sensor: TempSensorP1/1 *** Description: Power supply sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 22 *** Max temperature last change: 26 May 2020 11:39:06 *** Result: PASS
Sensor: TempSensorP2/1 *** Description: Power supply sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 24 *** Max temperature last change: 24 May 2020 18:38:15 *** Result: PASS
```
</p>
</details>

##### check_temperature_transceivers

Description: include tests report about the transceivers temperature status  
Required eos command: ```show system environment temperature transceiver | json```  
Test failure conditions: Failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state  
<details><summary>click me to see an output example</summary>
<p>

```

********** Temperature transceivers status **********

Description: Xcvr25 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 43 *** Max temperature last change: 14 May 2020 05:41:12 *** Result: PASS
Description: Xcvr26 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 54 *** Max temperature last change: 14 May 2020 05:30:17 *** Result: PASS
Description: Xcvr50 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 46 *** Max temperature last change: 14 May 2020 05:45:23 *** Result: PASS
Description: Xcvr51 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 48 *** Max temperature last change: 14 May 2020 05:36:20 *** Result: PASS
Description: Xcvr52 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 47 *** Max temperature last change: 14 May 2020 04:24:51 *** Result: PASS
Description: Xcvr54 temp sensor *** HW status: ok *** Alert count: 0 *** In alert state: False *** Max temperature (C): 43 *** Max temperature last change: 14 May 2020 05:43:38 *** Result: PASS
```
</p>
</details>

##### check_reload_cause_history

Description: include tests report about the cause for the last 10 reload  
Required eos command: ```show reload cause history | json```  
Test failure conditions: A test fails if a device reload was not requested by user  

<details><summary>click me to see an output example</summary>
<p>

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
</p>
</details>

##### check_reload_cause_full

Description: include tests report about the cause of the most recent reload  
Required eos command: ```show reload cause full | json```  
Test failure conditions: The test fails if the device reload was not requested by user  
<details><summary>click me to see an output example</summary>
<p>

```
********** Reload cause full **********

Time: 24 May 2020 18:37:55 *** Reason: The system rebooted due to a Power Loss *** Result: FAIL
```
</p>
</details>

##### print_lldp

Description: include the lldp topology  
Required eos command: ```show lldp neighbors | json```  
Test failure conditions: This is a report without any test so there is no failure/passing condition  
<details><summary>click me to see an output example</summary>
<p>

```
********** LLDP topology **********

Interface: Ethernet1 *** LLDP neighbor: switch2.lab.local *** LLDP remote port: Ethernet1
Interface: Ethernet2 *** LLDP neighbor: switch3.lab.local *** LLDP remote port: Ethernet1
Interface: Management1 *** LLDP neighbor: mgmt0a.lab.local *** LLDP remote port: Ethernet37
```
</p>
</details>

##### check_bgp

Description: include tests report about the bgp status for all configured vrf  
Required eos command: ```show ip bgp summary vrf all | json```  
Test failure conditions: A test fails if a BGP session is not established  
<details><summary>click me to see an output example</summary>
<p>

```
********** BGP sessions state **********

vrf: default
Peer: 10.10.10.1 *** ASN: 65002 *** State: Established *** Up/Down: 25 May 2020 00:02:57 *** Result: PASS
Peer: 10.10.10.3 *** ASN: 65003 *** State: Established *** Up/Down: 25 May 2020 00:02:54 *** Result: PASS
```
</p>
</details>

##### check_mlag

Description: include tests report about the mlag status  
Required eos command: ```show mlag detail | json```  
Test failure conditions: The test fails if the MLAG state is active and the negotiation status is not connected  
<details><summary>click me to see an output example</summary>
<p>

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
</p>
</details>

 
