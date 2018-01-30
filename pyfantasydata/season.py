#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-30 22:04:54'

from . import enums


class Season(object):
    def __init__(self, year, season_type):
        self.year = max(0, int(year))

        if isinstance(season_type, str):
            self.season_type = enums.SeasonType[season_type.upper()]
        else:
            self.season_type = enums.SeasonType(season_type)

    def __str__(self):
        return '{}{}'.format(self.year, self.season_type.name.upper())

    def __repr__(self):
        return '{}({}, {})'.format(
            self.__class__.__name__, repr(self.year), self.season_type
        )
