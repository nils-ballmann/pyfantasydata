#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-01-29 21:40:32'

scramble_filter = {
    'team': [
        'AverageDraftPosition',
        'AverageDraftPositionPPR',
        'UpcomingSalary',
        'UpcomingOpponent',
        'UpcomingOpponentRank',
        'UpcomingOpponentPositionRank',
        'UpcomingFanDuelSalary',
        'UpcomingDraftKingsSalary',
        'UpcomingYahooSalary',
    ],
}


def filter_json(json):
    # TODO: build in generic filtering
    return json


def filter_xml(xml):
    # TODO: build in generic filtering
    return xml


def _filter_json(json, part):
    for child in json:
        for elem in scramble_filter[part]:
            del child[elem]
    return json


def _filter_xml(xml, part):
    return xml
