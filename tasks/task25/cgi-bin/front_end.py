#!/usr/bin/env python3
import cgi
print("Content-type: text/html\n")
form = cgi.FieldStorage()
login = form.getfirst('name', "не задано")
print(login)


