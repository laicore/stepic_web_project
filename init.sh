echo "unlink default server nginx"
sudo unlink ls /etc/nginx/sites-enabled/default
sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
gunicorn -b 0.0.0.0:8000 --chdir ~/web/ask ask.wsgi &
echo "gunicorn start django"
sudo /etc/init.d/nginx start
#sudo nginx
echo "nginx start"
echo "finish"

