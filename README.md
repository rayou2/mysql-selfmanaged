# mysql-selfmanaged

This repo used GCP as the cloud environment to set up the VM

In the VM: create a VM instance and name "mysql". 

Machine type: e2-medium

Boot disk: Ubuntu OS, version ubuntu 18.04 x86/64

Firewall: allow both http and https traffic 

After creating and connecting to the VM, we would open the SSH browser. First, we would run the command 'sudo apt-get update' to update and install any outdated packages in the system. Next, we would run the command 'sudo apt install mysql-server mysql-client' and this installs mysql. To get into mysql, you would run 'sudo mysql'. 

To make sure that mysql instance was avaiable in external computers, we had to go to firewalls in GCP and make a new firewall rule where we had to check TCP and add port 3306. Port 3306 is a mysql port. 

