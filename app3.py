import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"    # Windows users: r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com", "www.censor.net", "censor.net"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
            < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:    # as test version the file was chosen in local directory.
            content = file.read()               # Change 'hosts_temp' to 'hosts_path' in previouse line.
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + '\n')
    else:
        with open(hosts_temp, 'r+') as file:    # Change 'hosts_temp' to 'hosts_path'.
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
