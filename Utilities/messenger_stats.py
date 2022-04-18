"""Script to generate messenger stats from the Facebook data"""

__author__ = "Louis-Justin TALLOT"


from pathlib import Path
from contextvars import ContextVar

from typing import Dict, List

import datetime
import json

import matplotlib.pyplot as plt
import numpy as np # type: ignore
import seaborn as sns

import pandas as pd

import pprint

_fb_dir_path: ContextVar[Path] = ContextVar("_fb_dir_path")
_all_convos_json: dict = {"Regular": {}, "Other": []}
# We load in memory the messages that we want
# {
#     "Regular": {
#         "dir_path_personne_1": {
#             "name": message_.json["title"], # str
#             "messages": message_.json["messages"], # list
#         },
#         "dir_path_personne_2": {
#             "name": message_.json["title"], # str
#             "messages": message_.json["messages"], # list
#         },
#     },
#     "Other": [
#         "name_group_1",
#         "name_group_2"
#     ]
# }



def _find_fb_dir_path() -> None:
    try:
        _fb_dir_path.get()
    except LookupError:
        for filepath in Path(__file__).resolve().parent.iterdir():
            if ("facebook-" in str(filepath)) and (".zip" not in str(filepath)):
                _fb_dir_path.set(filepath)


def calc_nb_messages_one_person() -> int:
    pass


def get_messages_one_convo(messages_dir_path: Path, convos_json: Dict) -> None:
    list_all_jsons = []

    for filepath in messages_dir_path.iterdir():
        if ("message_" in str(filepath)) and (".json" in str(filepath)):
            list_all_jsons.append(filepath)

    list_all_jsons.sort()
    name = ""
    list_messages = []

    for messages_json in list_all_jsons:
        with open(messages_json, "r", encoding="utf-8") as file:
            data = json.load(file)

            # short-circuit if not a 1-1 convo:
            if data["thread_type"] != "Regular":
                convos_json["Other"].append(data["title"].encode('latin1').decode('utf8'))
                return

            # get the name
            if not name:
                name = data["title"].encode('latin1').decode('utf8')
            else:
                assert name == data["title"].encode('latin1').decode('utf8')

            # get the messages 
            list_messages.extend(data["messages"])


    convos_json["Regular"][messages_dir_path] = {
        "name": name,
        "messages": list_messages
    }


def find_all_persons() -> None:
    global _all_convos_json
    _find_fb_dir_path()

    messages_dir_path = _fb_dir_path.get() / "messages" / "inbox"
    all_convos = list(messages_dir_path.iterdir())

    for i, convo in enumerate(all_convos):
        print(f"{i+1}/{len(all_convos)}", end="\r")
        get_messages_one_convo(convo, _all_convos_json)


def plot_messages_stats():
    _find_fb_dir_path()
    find_all_persons()

    messages_nb_per_person = {}
    
    for conv in _all_convos_json["Regular"].values():
        messages_list = conv["messages"]
        list_times_stamps = []

        for message in messages_list:
            ts_ms: int = message["timestamp_ms"]
            list_times_stamps.append(datetime.datetime.fromtimestamp(ts_ms/1000.0))

        list_times_stamps.sort()
        messages_nb_per_person[conv["name"]] = list_times_stamps

    max_length = max(len(v) for v in messages_nb_per_person.values())

    source = pd.DataFrame.from_dict(
        {
            person: messages_list + [np.NaN] * (max_length - len(messages_list)) \
            for person, messages_list in messages_nb_per_person.items() \
            if len(messages_list)>1000
        }
    )
   
    # one kdeplot per column
    for i, person in enumerate(source.columns):
        sns.kdeplot(
            x=source[person],
            label=person,
            shade=True,
            bw_method=0.05,
            color=sns.color_palette(as_cmap=True)[i]
        )

    plt.xlabel("")
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_messages_stats()

