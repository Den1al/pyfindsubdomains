# PyFindSubDomains
> A Pythonic wrapper over the findsubdomains service
> Version: 0.0.2.3

## About

[FindSubDomains](https://findsubdomains.com/)'s service is pretty self explainatory. This is the unofficial python wrapper.

## Author

[Daniel Abeles](https://twitter.com/Daniel_Abeles).

## Install

First, follow the installation guide of MassDNS.
Then, get it from PyPI:

```
pip install pyfindsubdomains
```

Or, build it from source:

```bash
git clone https://github.com/Den1al/pyfindsubdomains
cd pyfindsubdomains
python setup.py build
python setup.py install
```

## Usage

```python
from findsubdomains import FindSubDomains

fsd = FindSubDomains(domain='example.com')

for result in fsd.get():
    print(result)

"""
>>> {'domain': 'example.com' ...
"""
```

Now, since version `0.0.2.3` it is possible to run the `findsubdomain` cli module from anywhere after installation:
```bash
me@lab:~/ | ⇒ cd ~/
me@lab:~/ | ⇒  findsubdomains --help
usage: findsubdomains [-h] [-s] domain

positional arguments:
  domain            the domain to look for

optional arguments:
  -h, --help        show this help message and exit
  -s, --startswith  whether to look for subdomains that starts with
me@lab:~/ | ⇒ findsubdomains example.com
{'domain': 'example.com', 'ip': 'IP 93.184.216.34', 'asn': 'AS 15133', 'org': 'MCI Communications Services, Inc. d/b/a Verizon Business'}
...

```

## TODO
* Add more functionalities provided by the `findsubdomains` service.

## Credits

[FindSubDomains](https://findsubdomains.com/)
