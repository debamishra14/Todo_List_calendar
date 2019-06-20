# Todo_List_calendar

steps to set up project -

1. Install python 3.6.5 , DJango 2.2.2 versions and some libraries like requests, etc.
2. download this project and go to the project folder in command prompt.
3. run the django server using command - python manage.py runserver
4. Then in browser open then link - http://127.0.0.1:8000/
5. After that you will be in the home page of the project. And do what activities you want to do (Operations like create/ retrieve /update/ delete)
6. For admin operations create superuser using command-> django-admin createsuperuser
7. Then go to the link - http://127.0.0.1:8000/admin (can see all admin details)
8. Then login to that admin portal and click on stauss and Todo lists to see all details.

9. There is a filter option by which you want to retrieve lists.
10. There is also one search button where you can search based on titles.
11. There is an another action added by which you can download the selected lists.

-------------------------------------------------------------------------------------
AND there is a file named api.py which is an API to retrieve lists from this application.
To make work this API do below steps-
1. first run the django server using above provided command
2. after server run, run that api.py -> python api.py
3. Then it will show all lists present in the database
4. if you want to see single lists then pass id inside the get_todos function in api.py as get_todos('27') and save that and run as python api.py
5. if you want to see all lists then call the function as get_todos() in api.py and do as above.

Home page -
![Capture](https://user-images.githubusercontent.com/30753467/59797280-fcab2800-92fc-11e9-9b6a-5677eec717ab.PNG)
