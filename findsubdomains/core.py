import requests
from bs4 import BeautifulSoup
from .utils import strip_dict_items_decorator


class FindSubDomains(object):
    _base_url = 'https://findsubdomains.com/'
    _modes = {
        'full': _base_url + 'subdomains-of/',
        'startswith': _base_url + 'subdomains-starts-with/'
    }

    def __init__(self, domain, startswith=False):
        self._domain = domain
        self._selected_mode = 'startswith' if startswith else 'full'

    def get(self):
        html = self._get_data(self._build_url())

        if not html:
            return []

        return self._parse_html(html)

    def _build_url(self):
        return FindSubDomains._modes[self._selected_mode] + self._domain

    def _get_data(self, url):
        r = requests.get(url)
        result = None

        if r.status_code == 200:
            result = r.text

        return result

    @strip_dict_items_decorator
    def _build_result_from_tr(self, tr):
        return dict(
            domain=tr.find('td', {'data-field': 'Domain'}).get('title', ''),
            ip=tr.find('td', {'data-field': 'IP'}).text,
            asn=tr.find('td', {'data-field': 'AS'}).text,
            org=tr.find('td', {'data-field': 'Organization'}
                        ).find('div', {'class': 'overflow-hidden'}).text,
        )

    def _get_tr_table(self, soup):
        return soup.find('table', dict(id='table-view')).find_all('tr')[1:]

    def _parse_html(self, html):
        soup = BeautifulSoup(html, "html.parser")

        for tr in self._get_tr_table(soup):
            yield self._build_result_from_tr(tr)
