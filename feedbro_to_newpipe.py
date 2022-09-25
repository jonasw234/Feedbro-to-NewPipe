#!/usr/bin/env python3
"""Converts Feedbro YouTube subscriptions to NewPipe subscriptions."""
import os
import pathlib
import sqlite3
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile
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

    # Export to NewPipe database file
    with tempfile.TemporaryDirectory() as tempdir:
        with zipfile.ZipFile("NewPipeData.zip") as inzip:
            inzip.extractall(tempdir)
            with sqlite3.connect(
                os.path.join(tempdir, "newpipe.db"), isolation_level=None
            ) as con:
                cur = con.cursor()
                cur.execute("PRAGMA journal_mode=DELETE;")
                cur.execute("DELETE FROM subscriptions;")
                for channel_name, channel_url in youtube_channels.items():
                    cur.execute(
                        'INSERT INTO subscriptions (service_id, url, name, avatar_url, subscriber_count, description) VALUES (0, ?, ?, "", 0, "");',
                        (channel_url, channel_name),
                    )
                    con.commit()
        with zipfile.ZipFile(newpipe_output, "w", zipfile.ZIP_DEFLATED) as outzip:
            tempdir_path = pathlib.Path(tempdir)
            for file_path in tempdir_path.rglob("*"):
                outzip.write(file_path, arcname=file_path.relative_to(tempdir))

    print(f"Export completed and saved to {newpipe_output}.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {basename(__file__)} Feedbro-Subscriptions.opml NewPipeData.zip")
        sys.exit(1)
    else:
        main(*sys.argv[1:])
