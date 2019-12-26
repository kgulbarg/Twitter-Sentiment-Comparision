This is a web application called Sentiment Analyzer and is built on the Django framework.

Installations required: 
1. Download and install Python version 3.5.3 and above.
2. From the Python CLI create a virtual environment using: pip install virtualenvwrapper
3. Make a virtual environment with the command (where py1 is the name of the virual environment): mkvirtualenv py1
4. Switch to this environment using: workon py1
5. Install Django in this environment using: pip install django
6. Change directory to the folder that contains the project files and use the command (where ‘mypro’ is the name of the project): django-admin startproject mypro
7. Change directory to the project file created in step 6.
8. Install Tweepy package using: pip install tweepy
9. Install Scikit learn package using: pip install -U scikit-learn
10. Install Numpy package using: pip install numpy
11. Install Pandas package using: pip install pandas

In order to execute the project files following are the steps: 
1. Open the command prompt.
2. An optional step is to activate the virtual environment created. Change the directory to py1 which is now a folder in the ‘Envs’ folder of the system and type the command: activate
3. Change the directory to ‘mypro’.
4. Start the server with the command: python manage.py runserver
5. Open the browser and type the URL: http://localhost:8000/LSVC/home/
6. The web API is now ready to use. Choose and option: 'Compare Products' or 'Compare Brands'.
7. Fill the form with the input and submit by clicking 'Get Review Analysis'.
8. The output is shown on the browser. 
