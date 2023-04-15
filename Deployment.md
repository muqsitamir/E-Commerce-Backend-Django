### Linode and Domain
1. Buy linode server with the latest ubuntu version LTS support.
2. Buy domain.
3. Point all nameservers of domain to linode nameservers.
```
ns1.linode.com
ns2.linode.com
ns3.linode.com
ns4.linode.com
ns5.linode.com
```
4. Create an A record to for the domain name and the server ip.
5. Set domain and add a cname record as 'api' with alias to '@'
6. Wait for propagation.
7. Setup ssh into linode server.

### Django

#### Create Django Project
1. Test locally.
2. Keep two settings file for separate allowed hosts and databases and
3. Use `pip freeze` and add the packages you installed yourself to requirements.txt
4. Add pycache, venv, sqlite, idea to .gitignore
5. Upload django project to git

### Setting Up Environment

1. `sudo apt-update`
2. `sudo apt-upgrade`
3. `sudo apt install python3.10-venv`
4. `python3 -m venv venv`
5. `sudo nano ~/.profile`
6. Append `source venv/bin/activate`
7. Save and close the file.
8. `source ~/.profile`
9. Reboot server and venv should be automatically activated.
10. `git --version` if git is installed, good, otherwise install git



#### Django App

11. `cd /var/www`
12. `git clone yourprojectname`
13. `pip install -r yourprojectname/requirements.txt`

#### Nginx Setup

14. `sudo apt install nginx`
15. `nginx --version`
16. `sudo service nginx start`
17. `sudo service nginx status`

#### Database

18. `sudo apt install mysql`
19. `sudo service mysql status`
20. `sudo apt-get install libmysqlclient-dev build-essential`
21. `pip install mysqlclient`

#### Mysql conf changes

22. `cat /etc/mysql/mysql.conf.d/mysqld.cnf`
23. `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf` 
24. Change bind-address to 0.0.0.0. 
    1. bind-address = 127.0.0.1    ===>>>   bind-address = 0.0.0.0
    2. Save and close file i.e., control - o and control x.
25. `sudo service mysql restart`
26. `sudo ufw allow from <server-ip> to any port 3306`

> Creating mysql user and database for the django app

1. Login to mysql `mysql`
2. `CREATE USER '<new_username>'@'<server_ip>' IDENTIFIED BY '<password>';`
3. `GRANT ALL PRIVILEGES on  *.* TO 'new_username'@'<server_ip>' WITH GRANT OPTION;`
4. `CREATE DATABASE <new_database>;`
5. `FLUSH PRIVILEGES;`
6. `exit`

* Try connecting with Mysql workbench remotely using username and password

>   Make the following changes in settings/prod.py:

`    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<new_database>',
        'USER': '<new_username>',
        'PASSWORD': '<password>',
        'HOST': '<server-ip>',
        'PORT': '3306',
    }
}
`

##### Setting up tables

1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`
4. `python manage.py runserver`: Go to <server-ip>:8000 to confirm django app is running. Stop nginx for a moment to free the 8000 port.

#### UWSGI


1. `pip install uwsgi`
2. `mkdir /etc/uwsgi`
3. `mkdir /var/log/uwsgi/`
4. `sudo nano /etc/uwsgi/<yourprojectname>.ini`

```
[uwsgi]
virtualenv=/root/venv
#uid = www-data
#gid = www-data
chmod-socket = 666
processes = 4
master = true
memory-report = true
threads = 4
chdir = /root/var/www/<yourprojectname>
env = DJANGO_SETTINGS_MODULE=<yourprojectname>.settings
module = <yourprojectname>.wsgi
socket = /tmp/<yourprojectname>.sock
stats = /tmp/stats.socket
logto = /var/log/uwsgi/access.log
daemonize = /var/log/uwsgi/access.log
safe-pidfile = /tmp/safe-pidfile.pid
```

Save and close file.

#### Nginx Configuration

1. `sudo nano /etc/nginx/sites-available/<project_name>.conf`
```
upstream django {
    server unix:///tmp/<yourprojectname>.sock; # for a file socket
}


server {
    listen api.<domain-name>:80; # 80 worked when 8000 failed on linode even though 8000 worked on megadetector machine [reason to be identified]
    server_name api.<domain-name>;
    charset     utf-8;

    client_max_body_size 75M;

    location /media  {
        alias /root/<repo>/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /root/<repo>/staticfiles; # your Django project's static files - amend as required
    }

    location / {
        uwsgi_pass django;
        include /etc/nginx/uwsgi_params;
        uwsgi_ignore_client_abort on;
        uwsgi_connect_timeout 60;
        uwsgi_read_timeout 60;
        uwsgi_send_timeout 60;
    }
}
```
Save and close file.

2. `ln -s /etc/nginx/sites-available/<yourprojectname>.conf /etc/nginx/sites-enabled/<yourprojectname>.conf`

##### Run
1. `sudo service nginx restart`
2. `uwsgi --ini /etc/uwsgi/<yourprojectname>.ini`


### Important Commands

1. `uwsgi --reload /tmp/safe-pidfile.pid` after changing code/taking a git pull.
2. `sudo service nginx restart` after changing nginx settings.
3. `mysqldump <serverdbname> > backup.sql`
4. scp commands for downloading or uploading files/folders to server or `rsync -avz --partial root@172.105.121.154:/root/wwf_snow_leopard/media/events /path/to/local/directory/`
5. `sql_restore <localdbname> < backup.sql`

### Troubleshooting
* Make sure uwsgi is serving pid file, and you can check errors by `tail -1000 /var/log/uwsgi/access.log`
* Make sure uwsgi has created the .sock file in tmp.

### Reference

https://www.digitalocean.com/community/tutorials/how-to-allow-remote-access-to-mysql


##### Downloading data and merging database commands
1. `rsync -av --partial root@172.105.121.154:/root/wwf_snow_leopard/media/events/ .` This continues downloading the content of the events folder from where the download is interrupted
2. ` mysqldump -u root -p wwf_lums --no-create-db --no-create-info --skip-triggers --insert-ignore > db2_dump.sql` This dumps the database without writing any create statements and skipping errors during inserting such as duplicate entries (insert ignore).