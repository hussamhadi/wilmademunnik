Main entry point of project is `wilmademunnik/settings/__init__.py`.

To point to development settings, add in that file:
```
from settings_dev import *
```

otherwise it will point to production settings using:
```
from settings_prod import *
```


```$ virtualenv venv && source venv/bin/activate
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver 0.0.0.0:8000
```
This should get you a development server running
