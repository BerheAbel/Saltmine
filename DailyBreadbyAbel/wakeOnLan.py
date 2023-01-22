#! /usr/bin/python3

import subprocess, re, time

def wake():
    """
    Send magic packets to devices that are sleeping, add MAC addresses to devices list if needed
    """
    devices = ["A0:62:FB:99:5D:8A", "B0:37:95:4E:7F:C6", "D4:CF:F9:82:56:25", "00:D2:B1:EC:53:E0", "3C:18:A0:A3:F0:0C","FE:91:A0:D6:37:6D"]
    for device in devices:
        subprocess.call(f"sudo etherwake -i eno1 {device}", shell=True)

def discovered_devices():
    """
    very rudimentary way to count devices discovered
    """
    result_of_discover = subprocess.run(['yts', 'discover'], capture_output=True)
    list_of_devices = re.findall(r"\(\w\w\)", result_of_discover.stdout.decode())
    return len(list_of_devices)

def verify_wake():
    """
    Make sure all devices are up and connected to lan; problematic device == hisense; rudimentary solution
    """
    hisense_rdy = False
    number_of_devices_on_bread = 6 # 6 devices + 1 android that gets added after this
    number_of_devices_discovered = 0
    num_of_cycles = 0
    while number_of_devices_discovered < number_of_devices_on_bread or num_of_cycles > 200:
        wake()
        number_of_devices_discovered = discovered_devices()
        print(f"number of devices connected to internet: {number_of_devices_discovered}")
        num_of_cycles += 1
        time.sleep(10)
    else:
        print("All devices connected!")

    while hisense_rdy == False:
        hisense = subprocess.run(["yts", "test", "fb", "' '"], capture_output=True)
        rdy = re.search(r"No tests found.", hisense.stderr.decode()) 
        print("Devices not ready yet..")
        if rdy != None:
            hisense_rdy = True
    else:
        print("Hisense is ready; all others should be OK")

if __name__ == "__main__":
    verify_wake()
