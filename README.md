![GitHub](https://img.shields.io/github/license/ksator/arista_eos_audit)   
 
## Table of content

[About this repository](#about-this-repository)  
[Requirements](#requirements)  

## About this repository 

This repo has python content to collect eos commands from Arista devices.  
It also has python content to audit the data collected and to generate a report.  

The file [input.yml](input.yml) has the required input for the files [collect_eos_commands.py](collect_eos_commands.py) and  [audit_eos_files.py](audit_eos_files.py)   
 
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
