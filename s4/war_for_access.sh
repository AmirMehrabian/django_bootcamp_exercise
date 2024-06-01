#!/bin/bash

useradd -m user1
useradd -m user2

groupadd shared

usermod -aG shared user1
usermod -aG shared user2

mkdir /shared_files

touch /shared_files/shared_file

chown user1:shared /shared_files
chown user1:shared /shared_files/shared_file

chmod 660 /shared_files
chmod 660 /shared_files/shared_file

ls -ld /shared_files
ls -l /shared_files/shared_file

userdel -r user1
userdel -r user2

groupdel shared

rm -r /shared_files
