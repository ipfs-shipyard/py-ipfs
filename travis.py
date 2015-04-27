from tox._config import parseconfig

TOX_ENVS = list()
for env in parseconfig(None, 'tox').envlist:
    TOX_ENVS.append("  - TOX_ENV={0}".format(env))

TEMPLATE = '''
language: python
python: 2.7
env:
{0}
install:
  - pip install tox
script:
  - tox -e $TOX_ENV
'''

print(TEMPLATE.format('\n'.join(TOX_ENVS)))
