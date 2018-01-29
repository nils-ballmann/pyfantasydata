#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-30 00:00:20'

import collections
import xml.etree.ElementTree as et

import requests
import yarl

from . import enums


class Base(object):
    def __init__(
            self,
            api_key,
            api_name,
            api_category,
            api_base_url=None,
            api_response_format=None,
            **kwargs
        ): # yapf: disable
        if api_key is None:
            raise ValueError('"api_key" must not be None')
        elif isinstance(api_key, str):
            self.api_keys = [api_key]
        elif isinstance(api_key, collections.Iterable):
            self.api_keys = [str(key) for key in api_key]
        else:
            self.api_keys = [str(api_key)]

        if isinstance(api_name, str):
            self.api_name = enums.ApiName[api_name.upper()]
        else:
            self.api_name = enums.ApiName(api_name)

        if isinstance(api_name, str):
            self.api_category = enums.ApiCategory[api_category.upper()]
        else:
            self.api_category = enums.ApiCategory(api_category)

        if api_base_url:
            self.api_base_url = yarl.URL(api_base_url)
        else:
            self.api_base_url = yarl.URL('https://api.fantasydata.net/v3/')

        if api_response_format:
            self.api_response_format = enums.ApiResponseFormat(
                api_response_format
            )
        else:
            self.api_response_format = enums.ApiResponseFormat.JSON

        self.session = requests.Session(**kwargs)

    def _url(self, endpoint):
        endpoint = str(endpoint)
        return self.api_base_url / self.api_name.name.lower(
        ) / self.api_category.name.lower(
        ) / self.api_response_format.name.lower() / endpoint

    def _get(self, url, **kwargs):
        # try all the keys
        for key in self.api_keys:
            response = self.session.get(
                url, headers={'Ocp-Apim-Subscription-Key': key}, **kwargs
            )
            if response.ok:
                break
        else:
            # exit if none was working
            raise SystemExit('No api key had success')

        if self.api_response_format == enums.ApiResponseFormat.JSON:
            return response.json()
        elif self.api_response_format == enums.ApiResponseFormat.XML:
            return et.fromstring(response.text)

    def get(self, endpoint, **kwargs):
        url = self._url(endpoint)
        return self._get(url, **kwargs)


class NFL(Base):
    def __init__(self, api_key, api_category, **kwargs):
        super().__init__(api_key, enums.ApiName.NFL, api_category, **kwargs)
