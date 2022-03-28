#!/usr/bin/env python3
"""Converts Feedbro YouTube subscriptions to NewPipe subscriptions."""
import json
import sys
import xml.etree.ElementTree as ET
from os.path import basename


def main(feedbro_input: str, newpipe_output: str):
    """Convert Feedbro YouTube subscriptions to NewPipe subscriptions.

    Parameters
    ----------
    feedbro_input : str
        Feedbro input file
    newpipe_output : str
        NewPipe output file
    """
    # Parse Feedbro opml export
    feedbro_tree = ET.parse(feedbro_input)
    youtube_channels = {
        channel.attrib["title"]: channel.attrib["htmlUrl"]
        for channel in feedbro_tree.iter()
        if channel.attrib.get("htmlUrl")
        and channel.attrib["htmlUrl"].startswith("https://www.youtube.com/channel/")
    }

    # Export to NewPipe json file
    with open(newpipe_output, "w", encoding="utf-8") as newpipe_subscriptions:
        newpipe_data = {
            "app_version": "0.18.0",
            "app_version_int": 800,
            "subscriptions": [],
        }
        for title, url in youtube_channels.items():
            newpipe_data["subscriptions"].append(
                {"service_id": 0, "url": url, "name": title}
            )
        json.dump(newpipe_data, newpipe_subscriptions)
    print(f"Export completed and saved to {newpipe_output}.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            f"Usage: {basename(__file__)} Feedbro-Subscriptions.opml NewPipe-Subscriptions.json"
        )
        sys.exit(1)
    main(*sys.argv[1:])
