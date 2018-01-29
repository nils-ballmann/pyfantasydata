#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-29 19:27:26'

import enum


@enum.unique
class Format(enum.Enum):
    JSON = enum.auto()
    XML = enum.auto()


@enum.unique
class GameType(enum.Enum):
    NFL = enum.auto()


@enum.unique
class Category(enum.Enum):
    SCORES = enum.auto()
