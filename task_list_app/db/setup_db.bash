#!/bin/bash

echo "Provide mysql username"
read user

echo "Provide mysql user password"
read password

if [[ "$#" -ge 1 ]] && [[ $1 = "drop_db" ]]
then
    echo "DROPPING DATABASE 'task_list'"
    echo "===================="
    sudo mysql -u $user -p $password <<EOF
    drop database if exists task_list;
    show databases;
EOF
    echo "DROPPED DATABASE. RECREATING A NEW DATABASE."
    echo "===================="
fi

sudo mysql -u $user -p $password < ./setup_db_structure.sql
