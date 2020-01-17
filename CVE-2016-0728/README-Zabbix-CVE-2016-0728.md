# Zabbix-Templates

Template Security Check CVE-2016-0728 Plus New!

From the "cve-2016-0728 check" template available at https://share.zabbix.com/component/mtree/cat-app/security/cve-2016-0728-check?Itemid=, I created a custom version which works by checking a kernel version and if it already has a patch fix installed. It is only compatible with operating systems similar to Red Hat like CentOS, Fedora and others that have the rpm package based.

I based this template from information available on the websites:
- https://github.com/SecWiki/linux-kernel-exploits/blob/master/2016/CVE-2016-0728/README.md
- https://www.liquidweb.com/kb/protecting-against-cve-2016-0728/
- https://docs.bitnami.com/virtual-machine/security/security-2016-01-20/

There are two triggers, the first will inform yhat "There is a risk that this kernel version is vulnerable to CVE-2016-0728" and the second: CVE-2016-0728 Vulnerability not patched. The precision only depends if you define or not the user parameter.
To the things work more precise, you must set the user parameter in the zabbix agent configuration file of the operating system you want to test. The parameter must be set as follows:

UserParameter = cve-2016-0728, rpm -qa --changelog kernel | grep CVE-2016-0728

The target kernel versions are:
3.4.0, 3.5.0, 3.6.0, 3.7.0, 3.8.x, 3.9.x, 3.10.x, 3.11.x, 3.12.x, 3.13.0, 3.13.1

You can download the template via the link:
https://github.com/slunart/Zabbix-Templates/blob/master/TemplateZabbixCVE-2016-0728-rpm-based.xml

Best Regards,

Samuel Martins
