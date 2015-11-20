Thanks
First off thanks to Sebastian for creating this awesome script to execute rsync from python.

Enhancements
I have a requirements to provide near continuous protection for the data on a couple of Windows file servers in my environment,
I would like to try and modify this script from Sebastian so that it runs an infinite loop executing the rsync every 2 minutes and creating a snapshot every hour. I will also look to add in some extra logging and alerting, so that the system will log to a central MySql database and will send email alerts if there are multiple failures.

I will also write a server side script that will check the destination directory, and will clear out older snapshots. Finally the server side will also monitor write to and monitor the Mysql DB  and will send email alerts in the event of failures. 
