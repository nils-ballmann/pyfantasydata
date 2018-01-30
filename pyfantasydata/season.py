#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-30 22:00:59'

from . import enums


class Season(object):
    def __init__(self, season_type, year):
        if isinstance(season_type, str):
            self.season_type = enums.SeasonType[season_type.upper()]
        else:
            self.season_type = enums.SeasonType(season_type)

        self.year = max(0, int(year))

    def __str__(self):
        return '{}{}'.format(self.season_type.name.upper(), self.year)

    def __repr__(self):
        return '{}({}, {})'.format(
            self.__class__.__name__, self.season_type, repr(self.year)
        )
