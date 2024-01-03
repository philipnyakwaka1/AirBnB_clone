#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
sudo -y apt-get update && sudo -y apt-get upgrade
sudo -y apt-get install nginx
sudo ufw allow 80
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "I am learning Fabric and Deploying Static" | sudo tee /data/web_static/releases/test/index.html
symbolic_link='/data/web_static/current'
target_folder='/data/web_static/releases/test/'
sudo ln -s -f "$target_folder' '$symbolic_link"
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static/ {\n\talias data/web_static/current/\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx reload