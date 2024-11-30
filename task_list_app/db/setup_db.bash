#!/bin/bash

echo "Provide mysql username"
read user

# echo "Provide mysql user password"
# read password

# if [[ "$#" -ge 1 ]] && [[ $1 = "drop_db" ]]
# then
#     echo "Dropping database"
#     sudo mysql -u $user -p $password drop database if exists task_list;
# fi

sudo mysql -u $user -p < ./setup_db_structure.sql
