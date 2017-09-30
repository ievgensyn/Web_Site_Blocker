# Web_Site_Blocker
------------------
To block websites like facebook, twitter etc. during working hours -- a python3 script starting with loading your OS.
For instance, during working hours from 8.00 am till 16.00, this script will redirect links to local loop (127.0.0.1)
It is recomended to add both website addresses, including 'www' (facebook.com, www.facebook.com).
This script works with 'hosts' file. To define it inside the script the absolute path should be give -- add r befor 'C:\Windows...'.
Windows user can find it at 'C:\Windows\System32\drivers\etc\hosts', it has no extension.
Linux/Mac users: '/etc/hosts'. An original copy of this file must have!
All maniopulations with this file -- responsibility of the user.
------------------
For Windows users -- please rename the script 'app3.py' to 'app3.pyw' (simply add 'w' at the end)
Windows users could create action in Task Scheduler --> Actions-->Create Task.. 'General': Checkbox "Run with highest privileges" must be chosen. + "Configeure for": 'your system'.
'Triggers' -->"New": "Begin the task": 'At start'.
'Action' --> "Start a program' + point the script clicking at 'Browse'
'Conditions' --> uncheck "Start the task only if PC is on AC power.
-- OK --
-- Run --
