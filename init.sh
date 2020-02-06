echo "unlink default server nginx"
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo apt update
sudo apt install python3.5
sudo unlink /usr/bin/python3 
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install django==2.1
gunicorn -b 0.0.0.0:8000 --chdir ~/web/ask ask.wsgi &
echo "gunicorn start django"
sudo /etc/init.d/nginx start
#sudo nginx
echo "nginx start"
echo "finish"

