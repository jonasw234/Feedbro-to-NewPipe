#!/usr/bin/env python3
"""Converts Feedbro YouTube subscriptions to NewPipe subscriptions."""
import csv
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

    # Export to NewPipe csv file
    with open(newpipe_output, "w", encoding="utf-8") as newpipe_subscriptions:
        newpipe_csv = csv.writer(newpipe_subscriptions)
        newpipe_csv.writerow(['Channel Id', 'Channel Url', 'Channel Title'])
        for title, url in youtube_channels.items():
            newpipe_csv.writerow([url[len("https://www.youtube.com/channel/"):], url, title])
    print(f"Export completed and saved to {newpipe_output}.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(
            "/mnt/f/Syncthing/Settings/Feedbro Subscriptions.opml",
            "/mnt/r/NewPipe Subscriptions.csv",
        )
    elif len(sys.argv) != 3:
        print(
            f"Usage: {basename(__file__)} Feedbro-Subscriptions.opml NewPipe-Subscriptions.csv"
        )
        sys.exit(1)
    else:
        main(*sys.argv[1:])
