from jinja2 import Template
from yaml import load

f=open('devices.yml', 'r')
my_vars = load(f.read())
f.close()

f=open('devices.j2')
my_template = Template(f.read())
f.close()

f=open('network_devices.json','w')
f.write(my_template.render(my_vars))
f.close()
