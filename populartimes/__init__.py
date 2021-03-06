#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .crawler import run
from .crawler import get_current_popular_times

"""

ENTRY POINT

"""


def get(api_key, types, bound_lower, bound_upper, n_threads=20, radius=180, all_places=False):
    """
    :param api_key: str; api key from google places web service
    :param types: [str]; placetypes
    :param bound_lower: (float, float); lat/lng of southwest point
    :param bound_upper: (float, float); lat/lng of northeast point
    :param n_threads: int; number of threads to call
    :param radius: int; meters; from 1-180
    :param all_places: bool; include/exclude places without populartimes
    :return: see readme
    """

    params = {
        "API_key": api_key,
        "radius": radius,
        "type": types,
        "n_threads": n_threads,
        "all_places": all_places,
        "bounds": {
            "lower": {
                "lat": bound_lower[0],
                "lng": bound_lower[1]
            },
            "upper": {
                "lat": bound_upper[0],
                "lng": bound_upper[1]
            }
        }
    }

    return run(params)


def get_current(api_key, place_id):
    """
    retrieves the current popularity for a given place
    :param api_key:
    :param place_id:
    :return: see readme
    """
    return get_current_popular_times(api_key, place_id)
