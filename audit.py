
import datetime
import os
import json
import yaml 

def init (device):
    main_report = open(main_reports_directory + '/init.txt', 'w') 
    failures_only_report = open(failures_only_reports_directory + '/init.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write ('-'*13 + ' Report for device ' + device + ' ' + '-'*13 + "\n"*2)
        item.close()
    return(main_reports_directory + '/init.txt', failures_only_reports_directory + '/init.txt')

def hostname (device):
    command = "show hostname"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Device hostname " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: This is a report without any test so there is no failure/passing condition\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    hostname = data_json['hostname']
    fqdn = data_json['fqdn']
    for item in [main_report, failures_only_report]:
        item.write('Hostname: ' + hostname + '\n')
        item.write('FQDN: ' + fqdn + '\n')
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def version (device):
    command = "show version"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Device details " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: This is a report without any test so there is no failure/passing condition\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    modelName = data_json['modelName']
    version = data_json['version']
    uptime_seconds = data_json["uptime"]
    uptime = str(datetime.timedelta(seconds = int(uptime_seconds))) 
    serialNumber = data_json["serialNumber"]
    for item in [main_report, failures_only_report]:
        item.write('Model: ' + modelName + '\n')
        item.write('Serial number: ' + serialNumber + '\n')
        item.write('Version: ' + version + '\n')
        item.write('Uptime: ' + uptime + '\n')
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def inventory (device):
    command = "show inventory"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Inventory " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: A test fails if the manufacturer of a transceiver is not Arista Networks or if a power supply slot has no power supply unit inserted\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    description = data_json['systemInformation']['description']
    for item in [main_report, failures_only_report]:
        item.write('Device description: ' + description + '\n')
        item.write('\n')
    for item in [main_report, failures_only_report]:
        item.write('Power Supplies: \n')
    at_least_one_test_fail = False
    for ps in data_json['powerSupplySlots']: 
        slot = str(ps)
        name = data_json['powerSupplySlots'][ps]['name']
        serialNum = data_json['powerSupplySlots'][ps]['serialNum']
        if name == 'Not Inserted': 
            result = 'FAIL'
            at_least_one_test_fail = True
        else:
            result = 'PASS'
        message = 'Slot: ' + slot + ' *** Model: ' + name + ' *** SN: ' + serialNum + ' *** Result: ' + result + '\n'
        main_report.write(message)
        if result == 'FAIL':
            failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.write('Fan modules: \n')
    for fan_module in data_json['fanTraySlots']: 
        slot = str(fan_module)
        name = data_json['fanTraySlots'][fan_module]['name']
        main_report.write('Module: ' + slot + ' *** Model: ' + name + '\n')
    failures_only_report.write("The script doesnt run tests about the Fans modules ...\n")
    at_least_one_test_fail = False
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.write('Transceivers: \n')
    for transceiver in sorted(data_json["xcvrSlots"]):
        transceiver = str(transceiver)
        mfgName = data_json['xcvrSlots'][transceiver]['mfgName']
        serialNum = data_json['xcvrSlots'][transceiver]['serialNum']
        modelName = data_json['xcvrSlots'][transceiver]['modelName']
        if mfgName == 'Arista Networks':
            result = 'PASS'
        elif mfgName == 'Not Present': 
            result = 'PASS'
        else:
            result = 'FAIL'
            at_least_one_test_fail = True
        if mfgName != "Not Present": 
            message = "Port: " + transceiver + ' *** Manufacturer: ' + mfgName + ' *** Model: ' + modelName + ' *** SN: ' + serialNum + ' *** Result: ' + result + "\n"
            main_report.write(message)
            if result == 'FAIL':
                failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def power (device):
    command = "show system environment power"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Power supplies " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: A test fails if the status of a power supply is not ok\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    at_least_one_test_fail = False
    for powersupply in data_json['powerSupplies']:
        state = data_json['powerSupplies'][powersupply]['state']
        if state == 'ok': 
            result = 'PASS'
        else:
            result = 'FAIL'
            at_least_one_test_fail = True
        message = "Power supply: " + powersupply + ' *** Status: ' + state + ' *** Result: ' + result + "\n"
        main_report.write(message)
        if result == 'FAIL':
            failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def cooling (device):
    command = "show system environment cooling"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Cooling " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: A test fails if the status of a fan is not ok\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    for item in [main_report, failures_only_report]:
        item.write('Power supplies: \n')
    at_least_one_test_fail = False
    for ps in data_json['powerSupplySlots']:
        for fan in ps['fans']: 
            status = fan['status'] 
            label = fan['label']
            if status == 'ok': 
                result = 'PASS'
            else:
                result = 'FAIL'
                at_least_one_test_fail = True
            message = "Fan: " + label + ' *** Status: ' + status + ' *** Result: ' + result + "\n"
            main_report.write(message)
            if result == 'FAIL':
                failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    at_least_one_test_fail = False
    for item in [main_report, failures_only_report]:
        item.write('\nFan modules: \n')
    for fantrayslot in data_json['fanTraySlots']:
        for fan in fantrayslot['fans']: 
            status = fan['status'] 
            label = fan['label']
            if status == 'ok': 
                result = 'PASS'
            else:
                result = 'FAIL'
                at_least_one_test_fail = True
            message = "Fan: " + label + ' *** Status: ' + status + ' *** Result: ' + result + "\n"
            main_report.write(message)
            if result == 'FAIL':
                failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def temperature (device):
    command = "show system environment temperature"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Temperature " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state. The system temperature test fails if the system status is not OK\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    at_least_one_test_fail = False
    systemStatus = json.loads(data)['systemStatus']
    if systemStatus != 'temperatureOk': 
        result = 'FAIL'
    else:
        result = 'PASS'
        systemStatus = 'ok'
    for item in [main_report, failures_only_report]:
        item.write("System temperature: \n") 
    message = "Status: " + systemStatus + ' *** Result: ' + result + '\n'*2
    main_report.write(message)
    if result == 'FAIL': 
        failures_only_report.write(message)
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write("\nSensors: \n" ) 
    at_least_one_test_fail = False
    for sensor in data_json["tempSensors"]:
        hwStatus = sensor['hwStatus']
        alertCount = sensor['alertCount']
        description = sensor['description']
        name = sensor['name']
        maxTemperature = sensor['maxTemperature']
        inAlertState = sensor['inAlertState']
        maxTemperatureLastChange_epoch = sensor['maxTemperatureLastChange']
        maxTemperatureLastChange = datetime.datetime.fromtimestamp(maxTemperatureLastChange_epoch).strftime("%d %b %Y %H:%M:%S")
        if hwStatus != 'ok' or alertCount!= 0 or str(inAlertState) != "False": 
            result = 'FAIL'
            at_least_one_test_fail = True
        else:
            result = 'PASS'
        message = "Sensor: " + name + ' *** Description: ' + description + ' *** HW status: ' + hwStatus + ' *** Alert count: ' + str(alertCount) + ' *** In alert state: ' + str(inAlertState) + ' *** Max temperature (C): ' + str(int(maxTemperature)) + ' *** Max temperature last change: ' + maxTemperatureLastChange + ' *** Result: ' + result + "\n"
        main_report.write(message)
        if result == 'FAIL':
            failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write("\nCard Slot: \n" ) 
    at_least_one_test_fail = False
    for card in data_json["cardSlots"]: 
        entPhysicalClass = card['entPhysicalClass']
        relPos = card['relPos']
        for sensor in card["tempSensors"]: 
            hwStatus = sensor['hwStatus']
            alertCount = sensor['alertCount']
            description = sensor['description']
            name = sensor['name']
            maxTemperature = sensor['maxTemperature']
            inAlertState = sensor['inAlertState']
            maxTemperatureLastChange_epoch = sensor['maxTemperatureLastChange']
            maxTemperatureLastChange = datetime.datetime.fromtimestamp(maxTemperatureLastChange_epoch).strftime("%d %b %Y %H:%M:%S")
            if hwStatus != 'ok' or alertCount!= 0 or str(inAlertState) != "False": 
                result = 'FAIL'
                at_least_one_test_fail = True
            else:
                result = 'PASS'
            message = "Sensor: " + name + ' *** Description: ' + description + ' *** Card type: ' + entPhysicalClass + ' *** Card position: ' + relPos + ' *** HW status: ' + hwStatus + ' *** Alert count: ' + str(alertCount) + ' *** In alert state: ' + str(inAlertState) + ' *** Max temperature (C): ' + str(int(maxTemperature)) + ' *** Max temperature last change: ' + maxTemperatureLastChange + ' *** Result: ' + result + "\n"
            main_report.write(message)
            if result == 'FAIL':
                failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.write("Power Supplies: \n" ) 
    at_least_one_test_fail = False
    for item in data_json["powerSupplySlots"]: 
        for sensor in item["tempSensors"]: 
            hwStatus = sensor['hwStatus']
            alertCount = sensor['alertCount']
            description = sensor['description']
            name = sensor['name']
            maxTemperature = sensor['maxTemperature']
            inAlertState = sensor['inAlertState']
            maxTemperatureLastChange_epoch = sensor['maxTemperatureLastChange']
            maxTemperatureLastChange = datetime.datetime.fromtimestamp(maxTemperatureLastChange_epoch).strftime("%d %b %Y %H:%M:%S")
            if hwStatus != 'ok' or alertCount!= 0 or str(inAlertState) != "False": 
                result = 'FAIL'
                at_least_one_test_fail = True
            else:
                result = 'PASS'
            message = "Sensor: " + name + ' *** Description: ' + description + ' *** HW status: ' + hwStatus + ' *** Alert count: ' + str(alertCount) + ' *** In alert state: ' + str(inAlertState) + ' *** Max temperature (C): ' + str(int(maxTemperature)) + ' *** Max temperature last change: ' + maxTemperatureLastChange + ' *** Result: ' + result + "\n"
            main_report.write(message)
            if result == 'FAIL':
                failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def temperature_transceivers (device):
    command = "show system environment temperature transceiver"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Temperature transceivers " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: A test fails if a sensor HW status is not OK or if a sensor alert count is > 0 or if a sensor is currently in alert state\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    at_least_one_test_fail = False
    for sensor in data_json["tempSensors"]:
        hwStatus = sensor['hwStatus']
        alertCount = sensor['alertCount']
        description = sensor['description']
        maxTemperature = sensor['maxTemperature']
        inAlertState = sensor['inAlertState']
        maxTemperatureLastChange_epoch = sensor['maxTemperatureLastChange']
        maxTemperatureLastChange = datetime.datetime.fromtimestamp(maxTemperatureLastChange_epoch).strftime("%d %b %Y %H:%M:%S")
        if hwStatus != 'ok' or alertCount!= 0 or str(inAlertState) != "False": 
            result = 'FAIL'
            at_least_one_test_fail = True
        else:
            result = 'PASS'
        message = 'Description: ' + description + ' *** HW status: ' + hwStatus + ' *** Alert count: ' + str(alertCount) + ' *** In alert state: ' + str(inAlertState) + ' *** Max temperature (C): ' + str(int(maxTemperature)) + ' *** Max temperature last change: ' + maxTemperatureLastChange + ' *** Result: ' + result + "\n"
        main_report.write(message)
        if result == 'FAIL':
            failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    at_least_one_test_fail = False
    for card in data_json["cardSlots"]: 
        if card['entPhysicalClass'] == "Linecard":
            for sensor in card["tempSensors"]: 
                hwStatus = sensor['hwStatus']
                alertCount = sensor['alertCount']
                description = sensor['description']
                maxTemperature = sensor['maxTemperature']
                inAlertState = sensor['inAlertState']
                maxTemperatureLastChange_epoch = sensor['maxTemperatureLastChange']
                maxTemperatureLastChange = datetime.datetime.fromtimestamp(maxTemperatureLastChange_epoch).strftime("%d %b %Y %H:%M:%S")
                if hwStatus != 'ok' or alertCount!= 0 or str(inAlertState) != "False": 
                    result = 'FAIL'
                    at_least_one_test_fail = True
                else:
                    result = 'PASS'
                message = 'Description: ' + description + ' *** HW status: ' + hwStatus + ' *** Alert count: ' + str(alertCount) + ' *** In alert state: ' + str(inAlertState) + ' *** Max temperature (C): ' + str(int(maxTemperature)) + ' *** Max temperature last change: ' + maxTemperatureLastChange + ' *** Result: ' + result + "\n"
                main_report.write(message)
                if result == 'FAIL':
                    failures_only_report.write(message)
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def reload_cause_history (device):
    command = "show reload cause history"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Reload cause history " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: A test fails if a device reload was not requested by user\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    at_least_one_test_fail = False
    for reboot_id in range(0,10):
        reboot_id = str(reboot_id)
        if reboot_id in data_json["resetHistory"]:
            for reboot in data_json["resetHistory"][reboot_id]:
                description = data_json["resetHistory"][reboot_id][reboot][0]['description']
                timestamp_epoch = data_json["resetHistory"][reboot_id][reboot][0]['timestamp']
                timestamp = datetime.datetime.fromtimestamp(timestamp_epoch).strftime("%d %b %Y %H:%M:%S")
                if description != "Reload requested by the user.": 
                    result = "FAIL"
                    at_least_one_test_fail = True
                else:
                    result = "PASS" 
                message = "Time: " + timestamp  + " *** Reason: " + description + " *** Result: " + result + '\n'
                main_report.write(message)
                if result == 'FAIL':
                    failures_only_report.write(message) 
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def reload_cause_full (device):
    command = "show reload cause full"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " Reload cause full " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: The test fails if the device reload was not requested by user\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    at_least_one_test_fail = False
    for item in data_json["resetCauses"]: 
        description = item['description']
        timestamp_epoch = item['timestamp']
        timestamp = datetime.datetime.fromtimestamp(timestamp_epoch).strftime("%d %b %Y %H:%M:%S")
        if description != "Reload requested by the user.": 
            result = "FAIL"
            at_least_one_test_fail = True
        else:
            result = "PASS" 
        message = "Time: " + timestamp  + " *** Reason: " + description + " *** Result: " + result + '\n'
        main_report.write(message) 
        if result == 'FAIL':
            failures_only_report.write(message)
    if at_least_one_test_fail == True: 
        failures_only_report.write("The other tests succesfully passed\n")
    if at_least_one_test_fail == False: 
        failures_only_report.write("All tests successfully passed\n")
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def lldp (device):
    command = "show lldp neighbors"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " LLDP topology " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: This is a report without any test so there is no failure/passing condition\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    for item in data_json['lldpNeighbors']:  
        neighborDevice = item['neighborDevice']
        neighborPort = item['neighborPort']
        port = item['port']
        for f in [main_report, failures_only_report]:
            f.write("Interface: " + port + ' *** LLDP neighbor: ' + neighborDevice + " *** LLDP remote port: " + neighborPort + "\n")
    for f in [main_report, failures_only_report]:
        f.write('\n')
        f.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def bgp (device):
    command = "show ip bgp summary vrf all"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " BGP " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: A test fails if a BGP session is not established\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    for vrf in data_json['vrfs']: 
        vrf = vrf
        at_least_one_test_fail = False
        for item in [main_report, failures_only_report]:
            item.write("vrf: " + vrf + "\n") 
        for peer in data_json['vrfs'][vrf]['peers']: 
            peer = peer
            asn = data_json['vrfs'][vrf]['peers'][peer]['asn']
            peerState = data_json['vrfs'][vrf]['peers'][peer]['peerState']
            upDownTime = datetime.datetime.fromtimestamp(data_json['vrfs'][vrf]['peers'][peer]['upDownTime']).strftime("%d %b %Y %H:%M:%S")
            if peerState != 'Established': 
                result = 'FAIL'
                at_least_one_test_fail = True
            else:
                result = 'PASS'
            message = "Peer: " + peer + " *** ASN: " + asn + " *** State: " + peerState + " *** Up/Down: " + upDownTime + " *** Result: " + result + "\n"
            main_report.write(message)
            if result == 'FAIL':
                failures_only_report.write(message)
        if at_least_one_test_fail == True: 
            failures_only_report.write("The other tests succesfully passed\n")
        if at_least_one_test_fail == False: 
            failures_only_report.write("All tests successfully passed\n")
        for item in [main_report, failures_only_report]:
            item.write('\n')
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def mlag (device):
    command = "show mlag detail"
    main_report = open(main_reports_directory + '/' + command + '.txt', 'w')
    failures_only_report = open(failures_only_reports_directory + '/' + command + '.txt', 'w') 
    for item in [main_report, failures_only_report]:
        item.write('*'*10 + " MLAG " + '*'*10 + "\n"*2)
        item.write("Required EOS command: " + command + '| json\n')
        item.write("Failure conditions: The test fails if the MLAG state is active and the negotiation status is not connected\n\n")
    f = open(json_directory + '/' + command + '.json', 'r') 
    data = f.read()
    f.close()
    data_json = json.loads(data) 
    state = data_json["state"] 
    at_least_one_test_fail = False
    if state == "active": 
        negStatus = data_json["negStatus"]
        configSanity = data_json["configSanity"]
        peerAddress = data_json["peerAddress"]
        lastStateChangeTime_seconds = data_json["detail"]["lastStateChangeTime"]
        lastStateChangeTime = str(datetime.timedelta(seconds = int(lastStateChangeTime_seconds))) 
        if negStatus != 'connected': 
            result = 'FAIL'
            at_least_one_test_fail = True
        elif negStatus == 'connected':
            result = 'PASS' 
        if result == 'FAIL':
            for item in [main_report, failures_only_report]:    
                item.write("Peer: " + peerAddress + "\n")
                item.write("State: " + state + "\n")
                item.write("Negotiation Status: " + negStatus + "\n")
                item.write("Config Sanity: " + configSanity + "\n")
                item.write("Last state change: " +  str(lastStateChangeTime)+ "\n")
                item.write("\nTest result: " + result + "\n")  
        elif result == 'PASS': 
            main_report.write("Peer: " + peerAddress + "\n")
            main_report.write("State: " + state + "\n")
            main_report.write("Negotiation Status: " + negStatus + "\n")
            main_report.write("Config Sanity: " + configSanity + "\n")
            main_report.write("Last state change: " +  str(lastStateChangeTime)+ "\n")
            main_report.write("\nTest result: " + result + "\n")  
        if at_least_one_test_fail == False: 
            failures_only_report.write("All tests successfully passed\n")
    elif state != "active": 
        for item in [main_report, failures_only_report]:
            item.write("MLAG is " + state +  "\n")  
    for item in [main_report, failures_only_report]:
        item.write('\n')
        item.close()
    return(main_reports_directory + '/' + command + '.txt', failures_only_reports_directory + '/' + command + '.txt')

def generate_main_report(dev, topic): 
    outfile = open(reports_directory + "/main.txt", "w")
    infile = open(init(dev)[0], "r")
    for line in infile:  
        outfile.write(line)
    infile.close()
    for item in topic:
        infile = open(item(device)[0], "r")
        for line in infile:  
            outfile.write(line)
        infile.close()
    outfile.close()

def generate_failures_only_report(dev, topic): 
    outfile = open(reports_directory + "/failures only.txt", "w")
    infile = open(init(dev)[1], "r")
    for line in infile:  
        outfile.write(line)
    infile.close()
    for item in topic:
        infile = open(item(device)[1], "r")
        for line in infile:  
            outfile.write(line)
        infile.close()
    outfile.close()

def generate_network_main_report(devices):    
    network_report = open(output_directory + "/main.txt", "w")
    network_report.write('Report generated using Python the ' + str(datetime.datetime.now().strftime("%d %b %Y at %H:%M:%S")) + "\n"*2)
    network_report.write ('The list of devices audited is: ' + str(devices) + '\n')
    network_report.write ('The list of topics audited is: ' + str(audit_str_list) + '\n'*2)
    network_report.write('This file (main.txt) shows the details for all the tests.\n')
    network_report.write("The file failures_only.txt shows only the tests that failed." + "\n"*2)
    for device in devices:
        device_directory = output_directory + '/' + device
        reports_directory = device_directory + '/' + "reports"
        device_report = open(reports_directory + "/main.txt", "r")
        for line in device_report:  
            network_report.write(line)
        device_report.close()

def generate_network_failures_only_report(devices): 
    network_report_failures_only = open(output_directory + "/failures_only.txt", "w")
    network_report_failures_only.write('Report generated using Python the ' + str(datetime.datetime.now().strftime("%d %b %Y at %H:%M:%S")) + "\n"*2)
    network_report_failures_only.write ('The list of devices audited is: ' + str(devices) + '\n')
    network_report_failures_only.write ('The list of topics audited is: ' + str(audit_str_list) + '\n'*2)
    network_report_failures_only.write('This file (failures_only.txt) shows only the tests that failed.\n')
    network_report_failures_only.write("The file main.txt shows the details for all the tests." + "\n"*2)
    for device in devices:
        device_directory = output_directory + '/' + device
        reports_directory = device_directory + '/' + "reports"
        device_report = open(reports_directory + "/failures only.txt", "r")
        for line in device_report:  
            network_report_failures_only.write(line)
        device_report.close()

input_f = open('input.yml', 'r')
input_s = input_f.read()
input_f.close()
input = yaml.load(input_s, Loader=yaml.FullLoader)

devices = input['devices']
output_directory = input['output_directory'] 

audit_str_list = input['audit']
str_to_function = {'hostname': hostname, 'version': version, 'inventory': inventory, 'power': power, 'cooling': cooling, 'temperature': temperature, 'temperature_transceivers': temperature_transceivers, 'reload_cause_history': reload_cause_history, 'reload_cause_full': reload_cause_full, 'lldp': lldp, 'bgp': bgp, 'mlag': mlag} 
audit_func_list = []
for item in audit_str_list : 
    audit_func_list.append(str_to_function[item])

cwd = os.getcwd()
output_directory = os.path.dirname(cwd + "/" + output_directory + "/")

for device in devices:
    device_directory = output_directory + '/' + device
    eos_commands_directory = device_directory + '/' + "eos_commands"
    json_directory = eos_commands_directory + '/' + "json"    
    text_directory = eos_commands_directory + '/' + "text"  
    reports_directory = device_directory + '/' + "reports"
    main_reports_directory = reports_directory + '/' + "main"
    failures_only_reports_directory = reports_directory + '/' + "failures_only"
    for directory in [output_directory, device_directory, eos_commands_directory, json_directory, text_directory, reports_directory, main_reports_directory, failures_only_reports_directory]: 
        if not os.path.exists(directory):
            os.makedirs(directory)
    generate_main_report(device, audit_func_list)
    generate_failures_only_report(device, audit_func_list)

generate_network_main_report(devices)
generate_network_failures_only_report(devices)
