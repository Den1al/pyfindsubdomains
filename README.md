# PyFindSubDomains - A Pythonic wrapper over the findsubdomains service

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

## TODO
* Add more functionalities provided by the `findsubdomains` service.

## Credits

[FindSubDomains](https://findsubdomains.com/)
