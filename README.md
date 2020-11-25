## Quick Start

Add a "configs" 1 level up from your project root:
   
```
cd..
mkdir configs
```
   
Copy example_app_configs.json into the configs folder and edit as necessary
   
Migrate:
   
 ```
 python manage.py migrate
```

Create a super user:

```
python manage.py createsuperuser
```

With that super user go to /admin and find Social Applications. You will need to add a Google and Apple application. 
Provider, Name, Client ID, and the site are all required.