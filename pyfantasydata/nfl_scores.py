#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-30 22:07:11'

from . import enums, base


class NFLScores(base.NFL):
    def __init__(self, api_key, **kwargs):
        super().__init__(api_key, enums.ApiCategory.SCORES, **kwargs)

    def are_games_in_progress(self, **kwargs):
        return self.get('AreAnyGamesInProgress', **kwargs)

    def teams(self, **kwargs):
        return self.get('Teams', **kwargs)

    def all_teams(self, **kwargs):
        return self.get('AllTeams', **kwargs)

    def byes(self, season, **kwargs):
        return self.get('Byes/{}'.format(season), **kwargs)
