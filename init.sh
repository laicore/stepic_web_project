#sudo /etc/init.d/mysql start
#mysql -uroot -e "create database testdb"
#mysql -uroot -e "create user 'user'@'localhost' identified by 'user'"
#mysql -uroot -e "grant all on testdb.* to 'user'@'localhost'"
echo "unlink default server nginx"
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo apt update
sudo apt install python3.5 libmysqlclient-dev
sudo unlink /usr/bin/python3 
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install --upgrade pip gunicorn
sudo python3 -m pip install django==2.1
#gunicorn -b 0.0.0.0:8000 --chdir ~/web/ask ask.wsgi &
#sudo /etc/init.d/nginx start
#sudo nginx
#echo "finish"

