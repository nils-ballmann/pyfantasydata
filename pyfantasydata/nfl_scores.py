#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-30 00:12:43'

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

    def box_score_by_score_id_v3(self, score_id, **kwargs):
        return self.get(
            'BoxScoreByScoreIDV3/{}'.format(int(score_id)), **kwargs
        )
