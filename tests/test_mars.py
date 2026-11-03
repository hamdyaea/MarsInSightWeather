#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""Offline archive integrity tests."""
from PIL import Image
from MarsGUI import ARCHIVED_IMAGES, validate_archive


def test_all_archived_images_exist():
    assert validate_archive() == []


def test_images_are_readable():
    for path in ARCHIVED_IMAGES.values():
        with Image.open(path) as image:
            image.verify()


def test_no_remote_urls_in_archived_paths():
    assert all(path.is_absolute() for path in ARCHIVED_IMAGES.values())
