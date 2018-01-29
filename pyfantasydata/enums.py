#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-29 23:18:14'

import enum


@enum.unique
class ApiResponseFormat(enum.Enum):
    JSON = enum.auto()
    XML = enum.auto()


@enum.unique
class ApiName(enum.Enum):
    NFL = enum.auto()
    MLB = enum.auto()
    NBA = enum.auto()
    NHL = enum.auto()
    SOCCER = enum.auto()
    CFB = enum.auto()
    CBB = enum.auto()


@enum.unique
class ApiCategory(enum.Enum):
    SCORES = enum.auto()
    STATS = enum.auto()
    PBP = enum.auto()
    PROJECTIONS = enum.auto()
