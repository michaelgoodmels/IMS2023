#!/bin/bash

#-------------------------------------------------
# Author:               Luca Fabian Burger
# Organisation          IMS
# Version:              0.1
# Task:                 Hello Message
# OS:                   Linux (arch) native
# Date:                 25.02.25
# Last added feature:   Calls you by the name of the machine
# Start                 ./hello.sh
#-------------------------------------------------

# Get the hostname of the PC
hostname=$(cat /etc/hostname)

# Greet the user
echo "Hello, welcome $hostname! This is a message from Luca Burger."
