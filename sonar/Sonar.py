from typing import Iterable

import requests

from sonar import Project, Paging, Portfolio

# Add a really important comment here
class Sonar(object):
    def __init__(self, url: str, auth=None):
        self.auth = auth
        self.root = url

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def portfolios(self) -> Iterable[Portfolio]:
        raw_body = self.views_raw(1)
        paging = Paging.from_dict(raw_body["paging"])
        components = raw_body["components"]

        for component in components:
            yield Portfolio.from_dict(component)

        page_index = 1
        while page_index < paging.nb_pages:
            page_index += 1
            components = self.views_raw(page_index)["components"]
            for component in components:
                yield Portfolio.from_dict(component)

    def views_raw(self, page: int):
        params = dict(qualifier="VW", p=page)
        url = "{}/api/components/search".format(self.root)
        response = requests.get(url, auth=self.auth, verify=False, params=params)
        return response.json()

    def projects_raw(self, page: int):
        params = dict(qualifier="VW", p=page)
        url = "{}/api/components/search".format(self.root)
        response = requests.get(url, auth=self.auth, verify=False, params=params)
        return response.json()
