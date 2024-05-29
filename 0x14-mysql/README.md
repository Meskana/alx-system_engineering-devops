Fresh Reset
And
Install MySQL 5.7
⚠️Before going through the guide try this command if it gonna install MySQL 5.7 correctly, when you see the white windows you can jump to step 9, and see what to choose :


sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57


If this command did not install 5.7 correctly you can continue reading the guide.



Note: during this guide, don't go to the next step if you have errors in the current step you are in, make sure there are no errors.

Some steps can be skipped if they don't apply to your case:

Very rare but following this guide, you may find some errors. You can try to copy-paste errors to AI WEBSITES, to help you debug them… 
	https://chat.openai.com/
	https://poe.com/
https://you.com/
https://www.phind.com/

Follow the guide, if you need clarity check this video : 
	https://youtu.be/if0DBq9OqtE



1- Clean Running MySQL Processes



Check for any running MySQL processes:
	sudo ps aux | grep mysql
If MySQL is running, try stopping it:
	sudo service mysql stop
Double-check if MySQL is no longer running:
	sudo ps aux | grep mysql
If MySQL processes are still running, terminate them:
	sudo kill -9 <PID>
		Example :  sudo kill -9 9072

Note: if you have this grep --color something, you can ignore it and continue.


Proceed to the next step when MySQL is not running.



2-Remove Existing MySQL Versions

Remove MySQL packages
	
sudo apt-get remove --purge mysql-server mysql-client mysql-common -y && sudo apt-get autoremove -y



If no errors occur, proceed to the next step.

If something like this shows up, Choose 'yes' and press Enter. 
(if it didn't show up it ok, continue)


After it finishes, it should show something like this: 


If no errors occur, proceed to the next step.




3-Remove MySQL Apt Configuration

	sudo rm -rf /etc/apt/sources.list.d/mysql.list*
	sudo rm -rf /var/lib/mysql-apt-config
	sudo dpkg --purge mysql-apt-config

Double-check that everything related to MySQL is removed:
	dpkg -l | grep mysql

It should be empty as in the image below, if not try redoing the previous steps.





4-Remove MySQL Configuration Files


sudo rm -rf /etc/mysql /var/lib/mysql



5-Edit sources.list to Remove MySQL Repositories

Check the sources.list file for MySQL repository entries (example: deb http://repo.mysql.com/apt/ubuntu bionic main), 
there should be none like the picture below:
		cat /etc/apt/sources.list | grep mysql


If there are entries, open the sources.list file:
	sudo vi /etc/apt/sources.list 

Look for (example: deb http://repo.mysql.com/apt/ubuntu bionic main) and delete lines referencing MySQL repositories. 


If no errors occur, proceed to the next step.




6-Update Packages
sudo apt update


If you got an error like this (if no error skip to step7) : 
	

	Do this command and kill all running processes (ignore grep color) : 
		ps aux | grep apt
		In this case, we have to kill this running process using their PID : 
	
	You can kill them by sudo kill -9 <PID>
	So in our case gonna be : 
		sudo kill -9 87243 
		sudo kill -9 87243 
		sudo kill -9 87497 
		sudo kill -9 87631
	Again do ps aux | grep apt : 
		Now it is good, we can skip that grep color process
	Do again sudo apt update
	
	Perfect, continue to step 7.



7-Clean APT Cache
sudo apt clean




8-Configure Any Pending Packages
sudo dpkg --configure -a





9-Install MySQL 5.7

Let's install MySQL 5.7 now (the next command is one line command) : 


sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57


Note: I updated the script to select Bionic and 5.7 by default, so if you find them already selected, you can just press enter and OK… if they are not selected by default, follow with the pictures below.


A few windows are going to show up. Follow the prompts to select Ubuntu Bionic, change to MySQL 5.7, and set a password if needed.

Select Ubuntu bionic and press enter:



See the picture below, notice it shows MySQL 8.0, we will need to change it to 5.7, press enter: (if it shows 5.7 you can scroll down to OK and press enter)



After you press enter, a list of versions will show up, scroll up select 5.7, and press enter:
(skip this if already have 5.7 selected) 



After you press enter you will see something like this, just scroll down to ok and press enter, but notice that version did change to 5.7 : 



The script will continue then another window gonna show up asking you about MySQL password, feel free to enter any password, (for me to avoid problems I just leave it empty which means no password ) then press enter: 




The script will continue installing

In the end will show something like this : 



Congratulations, MySQL 5.7 is now installed correctly!





After installation, check MySQL status:
	sudo service mysql status



If issues persist, use the following commands to debug: 

	journalctl -u mysql.service

	cat /var/log/mysql/error.log

	journalctl -xe

Check this post to learn more about MySQL : 
	https://shazaali.substack.com/p/database-administration

Others guide : 
https://docs.google.com/document/d/1KtK5lm2cTzs6eudFUEtBCo8Zdt3Pl-VKhlald4NzNKo/edit

Good luck!
You Got This ♥

Written by Mounssif nuuX BOUHLAOUI : 
https://twitter.com/nuux_tv/

