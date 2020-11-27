To work properly, you need to set the User Parameter inside the "zabbix_agentd.conf" or into "zabbix_agentd.userparams.conf" as below:

UserParameter=WinVerAct,powershell -noninteractive -Command "$WinVerAct=[string](cscript /Nologo \"C:\Windows\System32\slmgr.vbs\" /xpr) -join ''; $Res1=$WinVerAct.Contains('A máquina está ativada permanentemente.'); $Res2=$WinVerAct.Contains('The machine is permanently activated.'); $Res1 -Or $res2"

The period of the item is defined in the interval of 1 day. Change it to a value that suits your needs.

Software Licensing Management Tool (slmgr) is a VBS file in Windows against which you can run commands to perform advanced Windows activation tasks. 
The /xpr parameter Show the expiry date of the current license or indicate whether activation is permanent.
