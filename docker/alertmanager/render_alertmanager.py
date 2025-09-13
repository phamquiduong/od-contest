from string import Template

env = {}
with open('../.env', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            k, v = line.split('=', 1)
            env[k] = v

with open('alertmanager.template.yml', encoding='utf-8') as f:
    content = Template(f.read()).substitute(env)

with open('alertmanager.yml', 'w', encoding='utf-8') as f:
    f.write(content)
