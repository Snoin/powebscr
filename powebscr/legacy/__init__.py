#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"Powerful Web Screenshot"
import os
from pathlib import Path
from subprocess import check_output
import subprocess
import sys
import tempfile
import cloudinary
import cloudinary.api
import cloudinary.uploader


# TODO: use click
def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python -m powebscr.legacy <url>")

    url = sys.argv[1]

    # for node_modules...
    os.chdir(os.path.dirname(__file__))

    CLOUDINARY = os.environ.get("CLOUDINARY_URL", "")
    if not CLOUDINARY.startswith("cloudinary://"):
        # just check for upload.js
        sys.exit("error: invaild cloudinary url (check env CLOUDINARY_URL)")

    # TODO: require custom port?
    server = None
    imgpath = Path(tempfile.mktemp(".png"))

    # TODO: vaild url
    assert url.startswith("http://") or url.startswith("https://")

    os.environ["POWEBSCR_HOMEURL"] = url
    os.environ["POWEBSCR_IMGPATH"] = str(imgpath)

    try:
        # TODO: dynamic viewport support
        check_output(["./phantomjs", "./screenshot.js"])

        upload_info = cloudinary.uploader.upload(str(imgpath))
        secure_url = upload_info.get('secure_url')
        assert secure_url, "upload_info['secure_url'] is empty"

        print(secure_url)
        return secure_url
    finally:
        if server:
            server.terminate()
            try:
                server.wait(timeout=1)
            except subprocess.TimeoutExpired:
                server.kill()

        if imgpath.exists():
            imgpath.unlink()
