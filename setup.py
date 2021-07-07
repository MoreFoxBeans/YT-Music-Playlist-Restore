#!/usr/bin/env python3
from jinja2 import Template

template_path = 'headers_auth.json_template'
out_path = 'headers_auth.json'

cookie = input('Paste your cookie here:')

try:
    file = open(template_path, 'r')
    template = file.read()
    file.close()
except:
    print('The headers_auth template seems to be missing or locked!')
    input()
else:
    unrendered = Template(template)
    out = unrendered.render(cookie=cookie)

    try:
        file = open(out_path, 'w')
        file.write(out)
        file.close()
    except:
        print('Could not create the headers_auth file!')
        input()
