# TemplatesZabbix

1. Import the template on zabbix server.

2. Add the folder with the powershell scripts inside the host, ex: C:/Zabbix/scripts

3. Insert theses lines at zabbix_agentd.conf of goal host.

  UserParameter=numberofactiveusers,powershell -File C:/Zabbix/scripts/numberofactiveusers.ps1

  UserParameter=listofactiveusers,powershell -File C:/Zabbix/scripts/listofactiveusers.ps1
  
4. Inside the Zabbix server, add the template on the host. 


