import pytest

from fetch_presidents import fetch_presidents

EXPECTED_PRESIDENTS = [
    "Washington",
    "Adams",
    "Jefferson",
    "Madison",
    "Monroe",
    "Adams",
    "Jackson",
    "Buren",
    "Harrison",
    "Tyler",
    "Polk",
    "Taylor",
    "Fillmore",
    "Pierce",
    "Buchanan",
    "Lincoln",
    "Johnson",
    "Grant",
    "Hayes",
    "Garfield",
    "Arthur",
    "Cleveland",
    "Harrison",
    "McKinley",
    "Roosevelt",
    "Taft",
    "Wilson",
    "Harding",
    "Coolidge",
    "Hoover",
    "Roosevelt",
    "Truman",
    "Eisenhower",
    "Kennedy",
    "Johnson",
    "Nixon",
    "Ford",
    "Carter",
    "Reagan",
    "Bush",
    "Clinton",
    "Bush",
    "Obama",
    "Trump",
    "Biden"
]


def test_fetch_presidents():
    presidents = fetch_presidents()

    for president in presidents:
        if president in EXPECTED_PRESIDENTS:
            EXPECTED_PRESIDENTS.remove(president)

    assert len(EXPECTED_PRESIDENTS) == 0
