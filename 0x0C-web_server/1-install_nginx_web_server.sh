#!/usr/bin/env bash
# Bash script to install and configure Nginx web server

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
echo "Hello World!" > /var/www/html/index.html
sudo service nginx start
