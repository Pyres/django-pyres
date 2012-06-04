About
=====
django pyres provides a way to run workers via the django manage.py command. 

Motivation
==========
Several people have asked how to interact with the django orm from within pyres jobs. By running the
workers through the manage command, you don't have to mess around with setting variables in the os.environ object.
