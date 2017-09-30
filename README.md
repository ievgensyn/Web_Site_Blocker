# Web_Site_Blocker
------------------
This script was written as exsercise.
------------------
To block websites like facebook, twitter etc. during working hours -- a python3 script starts with loading your OS.
For instance, during working hours from 8.00 am till 16.00, this script will redirect links to local loop (127.0.0.1)
It is recommended to add both website addresses, including 'www' (facebook.com, www.facebook.com).
This script works with 'hosts' file. The absolute path should be given -- add r before 'C:\Windows...'. Something like: r"C\Windows\System32\drivers\etc\hosts".
Windows user can find it at 'C:\Windows\System32\drivers\etc\hosts', it has no extension.
Linux/Mac users: '/etc/hosts'. An original copy of this file must have!
All manipulations with this file -- responsibility of the user.
Actually, the script uses a local path for testing purposes. The script and the 'hosts' file were in the same direcory.
You can modify it as you wish.
------------------
For Windows users -- please rename the script 'app3.py' to 'app3.pyw' (simply add 'w' at the end)
Windows users could create action in Task Scheduler --> Actions-->Create Task.. 
'General' --> Checkbox "Run with highest privileges" must be chosen. + "Configure for": 'your system'.
'Triggers' -->"New": "Begin the task": 'At startup'.
'Action' --> "Start a program' + point the script location, clicking at 'Browse'
'Conditions' --> uncheck "Start the task only if PC is on AC power.
-- OK --
-- Run --
-----------------
Linux -like users could use crontab 'scheduler': https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/
