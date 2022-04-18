"""Script to generate Messenger stats from the Facebook data"""

__author__ = "Louis-Justin TALLOT"


from pathlib import Path
from contextvars import ContextVar

from typing import Dict

import datetime
import json

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

import pandas as pd


_fb_dir_path: ContextVar[Path] = ContextVar("_fb_dir_path")



def _find_fb_dir_path() -> None:
    try:
        _fb_dir_path.get()
    except LookupError:
        for filepath in Path(__file__).resolve().parent.iterdir():
            if ("facebook-" in str(filepath)) and (".zip" not in str(filepath)):
                _fb_dir_path.set(filepath)


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


def find_all_persons() -> Dict[str, Dict]:
    # We load in memory the messages that we want
    all_convos_json: dict = {"Regular": {}, "Other": []}
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

    _find_fb_dir_path()

    messages_dir_path = _fb_dir_path.get() / "messages" / "inbox"
    all_convos = list(messages_dir_path.iterdir())

    for convo in all_convos:
        get_messages_one_convo(convo, all_convos_json)

    return all_convos_json


def plot_messages_stats():
    _find_fb_dir_path()
    all_convos_json = find_all_persons()

    messages_nb_per_person = {}
    
    for conv in all_convos_json["Regular"].values():
        messages_list = conv["messages"]
        list_times_stamps = []

        for message in messages_list:
            ts_ms: int = message["timestamp_ms"]
            list_times_stamps.append(datetime.datetime.fromtimestamp(ts_ms/1000.0))

        list_times_stamps.sort()
        messages_nb_per_person[conv["name"]] = list_times_stamps

    # arrange and select the data
    list_df = []
    for person, messages_list in messages_nb_per_person.items():
        if len(messages_list) > 1000:
            list_df.append(
                pd.DataFrame(
                    list(zip([person] * len(messages_list), messages_list)),
                    columns=["name", "ts"]
                )
            )

    source = pd.concat(list_df)

    # plot the data
    sns.kdeplot(
        data=source,
        x="ts",
        hue="name",
        cut=0,
        shade=True,
        bw_method=0.05,
        common_norm=True,
    )

    # labels per name
    label_patches = []
    for i in range(len(list_df)):
        name = list_df[i]["name"].iloc[0]

        label_patches.append(
            mpatches.Patch(color=sns.color_palette(as_cmap=True)[i],
            label=f"{name} ({len(list_df[i])})")
        )

    plt.xlabel("")
    plt.yticks([])
    plt.ylabel("Number of messages")
    plt.legend(handles=label_patches, loc="upper left")
    plt.title("Number of messages exchanged on Messenger")
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    plot_messages_stats()
