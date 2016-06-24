# AWAP 2016 Website

To run this website locally, you must have python installed. To do that, run this command on in your command-line/terminal depending on what operating system you use:
```
sudo apt-get install python
```
or
```
sudo yum install python
```
You will then need to install pip:
```
sudo apt-get install python-pip
```
or
```
sudo yum install python-pip
```
If you are running python3, then use the following:
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```
Now install Django with:
```
pip install Django
```
Lastly, the website utilizes Django-tables:
```
pip install django-tables2
```
Now that you have all the libraries installed, cd into the directory where manage.py is located and run:
```
python manage.py runserver 8000
```
Open a web browser of your choice and type in as the url http://localhost:8000. 
