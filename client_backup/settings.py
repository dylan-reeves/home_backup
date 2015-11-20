#Source - Enter the source directory, make sure it is cygwin compatible
# E.G. /cygdrive/c/Backup/Mystuff

SOURCE_DIR = 'cygdrive/c/Folder'

#Destination - The destination needs to be an ssh address and file path
#E.G. username@destinationserver:/samba/destinationdirectory
#This assumes you have created an ssh key so that it will not request a password
#I will include instructions to set this up

DESTINATION_ARG = 'dylan@MW5DRP-SRV:/samba/staging'

#LocalLog is the local text based log file, again it must be compatible with cygwin

LOCAL_LOG = 'cygdrive/c/synclog/synclog.log'

#DB

#Email
