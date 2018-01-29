#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-29 22:36:55'

import collections
import xml.etree.ElementTree as et

import requests
import yarl

from . import scramble_filter as sf
from . import enums


class Base(object):
    def __init__(
            self,
            api_key,
            api_url=None,
            api_version='v3',
            api_response_format=enums.Format.JSON,
            **kwargs
        ): # yapf: disable
        if isinstance(api_key, str):
            self.api_keys = [api_key]
        elif isinstance(api_key, collections.Iterable):
            self.api_keys = [str(key) for key in api_key]
        else:
            self.api_keys = [str(api_key)]

        if isinstance(api_url, yarl.URL):
            self.url = api_url
        else:
            self.url = yarl.URL(
                'https://api.fantasydata.net/{}/'.format(str(api_version))
            )

        if isinstance(api_response_format, enums.Format):
            self.api_response_format = api_response_format
        else:
            self.api_response_format = enums.Format.JSON

        self.session = requests.Session(**kwargs)

    def get(self, relative_url):
        if isinstance(relative_url, str):
            relative_url = yarl.URL(relative_url)
        if not isinstance(relative_url, yarl.URL):
            raise TypeError(
                '"relative_url" must be of type "yarl.URL", but is of type "{}"'.
                format(type(relative_url).__name__)
            )
        if relative_url.is_absolute():
            raise ValueError(
                '"relative_url" must be relative url, but is absolute url "{}"'.
                format(relative_url)
            )

        # try all the keys
        for key in self.api_keys:
            response = self.session.get(
                self.url.join(relative_url),
                headers={'Ocp-Apim-Subscription-Key': key}
            )
            if response.ok:
                break
        else:
            # exit if none was working
            raise SystemExit('No api key had success')

        if self.api_response_format == enums.Format.JSON:
            return response.json()
        elif self.api_response_format == enums.Format.XML:
            return et.fromstring(response.text)

    def get_filtered(self, relative_url):
        # filter out the free subscription scrambled data
        result = self.get(relative_url)

        if self.api_response_format == enums.Format.JSON:
            return sf.filter_json(result)
        elif self.api_response_format == enums.Format.XML:
            return sf.filter_xml(result)
