import requests
from bs4 import BeautifulSoup


class FindSubDomains(object):
    _base_url = 'https://findsubdomains.com/'
    _modes = {
        'full': _base_url + 'subdomains-of/',
        'startswith': _base_url + 'subdomains-starts-with/'
    }

    def __init__(self, domain, startswith=False):
        self._domain = domain

        if startswith:
            self._selected_mode = 'startswith'
        else:
            self._selected_mode = 'full'


    def get(self):
        html = self._get_data(self._build_url(self._selected_mode))

        if not html:
            return []

        return self._parse_html(html)
        
        
    def _build_url(self, mode):
        return FindSubDomains._modes[mode] + self._domain

    def _get_data(self, url):
        r = requests.get(url)

        return {
            0: None,
            1: r.text
        }[r.status_code == 200]
        

    def _parse_html(self, html):
        for tr in BeautifulSoup(html, "html.parser").find('table', {
            'id': 'table-view'
        }).find_all('tr')[1:]:
            yield {
                'domain': tr.find('td', {'data-field': 'Domain'})['title'],
                'ip': tr.find('td', {'data-field': 'IP'}).text,
                'asn': tr.find('td', {'data-field': 'AS'}).text,
                'org': tr.find('td', {'data-field': 'Organization'}).text,
            }
