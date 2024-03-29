#!/bin/bash

# global passaword
# PASSWDDB="admin"

# database username
# USERNAME="admin"

# database name
DBNAME="dbtest"

# If /root/.my.cnf exists then it won't ask for root password
if [ -f /root/.my.cnf ]; then

    mysql -e "FLUSH PRIVILEGES;"
    mysql -e "CREATE DATABASE ${DBNAME} /*\!40100 DEFAULT CHARACTER SET utf8 */;"
    # mysql -e "CREATE USER ${USERNAME}@localhost IDENTIFIED BY '${PASSWDDB}';"
    # mysql -e "GRANT ALL PRIVILEGES ON ${DBNAME}.* TO '${USERNAME}'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"

# If /root/.my.cnf doesn't exist then it'll ask for root password   
else
    echo "Please enter root user MySQL password!"
    echo "Note: password will be hidden when typing"
    read -sp rootpasswd:
    echo ""
    mysql -uroot -p${rootpasswd} -e "FLUSH PRIVILEGES;"
    mysql -uroot -p${rootpasswd} -e "CREATE DATABASE ${DBNAME} /*\!40100 DEFAULT CHARACTER SET utf8 */;"
    # mysql -uroot -p${rootpasswd} -e "CREATE USER ${USERNAME}@localhost IDENTIFIED BY '${PASSWDDB}';"
    # mysql -uroot -p${rootpasswd} -e "GRANT ALL PRIVILEGES ON ${DBNAME}.* TO '${USERNAME}'@'localhost';"
    mysql -uroot -p${rootpasswd} -e "FLUSH PRIVILEGES;"
fi