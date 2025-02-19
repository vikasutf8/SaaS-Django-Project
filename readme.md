### SaaS-foundation
- https://www.codingforentrepreneurs.com/blog/deploy-django-on-railway-with-this-dockerfile
Build the foundation for Software as a Service business by leveraging Dango, Tailwind, Htmx, Neon Postgres, Redis, and more.\\
The goal of this project is to learn how to create a reusable foundation for building SaaS products. When release, this course will span multiple topics and give you a solid foundation into build your business.\\

### Concept of Django and flow :
- urls.py(define urls) --> views.py(main business logic) --> home.html(render frontend page)
- inheritance templates : using `{% extends 'base.html'%}`
- body is written and include by `{block name} {endblock name}`
- create new app or microservices `python manage.py startapp "appname"`
- models.py  migrations `python manage.py makemigrations` & `python manage.py migrate`
- handling Env file  --using python-decouple  

### Detailing of Project, logic & definations:
- based function : render views.py as html
    -  its views taking argument as :request, as need ,extra *args, **kwargs
- 'str' object has no attribute 'get' :: this is django security by defualt
- pathlib ::
- Installed Apps :application definitions inbuild also ..
- python-decouple
- docker also attached 