"""Script to generate messenger stats from the Facebook data"""

__author__ = "Louis-Justin TALLOT"


from pathlib import Path
from contextvars import ContextVar

from typing import List

import datetime
import matplotlib.pyplot as plt
import altair as alt


_fb_dir_path: ContextVar[Path] = ContextVar("_fb_dir_path")



def _find_fb_dir_path() -> None:
    for filepath in Path(__file__).resolve().parent.iterdir():
        if "facebook-" in str(filepath) and ".zip" not in str(filepath):
            _fb_dir_path.set(filepath)


def calc_nb_messages_one_person() -> int:
    pass


def find_all_persons() -> List:
    pass


def plot_messages_stats():  
    _find_fb_dir_path()



if __name__ == "__main__":
    plot_messages_stats()






