#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-29 22:19:36'

import enum


@enum.unique
class Format(enum.Enum):
    JSON = enum.auto()
    XML = enum.auto()


@enum.unique
class GameType(enum.Enum):
    NFL = enum.auto()
    MLB = enum.auto()
    NBA = enum.auto()
    NHL = enum.auto()
    SOCCER = enum.auto()
    CFB = enum.auto()
    CBB = enum.auto()


@enum.unique
class Category(enum.Enum):
    SCORES = enum.auto()
    STATS = enum.auto()
    PBP = enum.auto()
    PROJECTIONS = enum.auto()
