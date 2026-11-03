#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""Offline viewer of archived NASA InSight Mars weather imagery."""
from pathlib import Path
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

ROOT = Path(__file__).resolve().parent
ARCHIVED_IMAGES = {
    "Weather chart": ROOT / "weatherOK.png",
    "InSight lander": ROOT / "insightLab.jpg",
    "Mars image": ROOT / "mars.png",
}


def validate_archive() -> list[Path]:
    """Return missing archived assets without contacting NASA."""
    return [path for path in ARCHIVED_IMAGES.values() if not path.is_file()]


class MarsWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mars InSight — Archived Weather")
        self.geometry("900x680")
        self.minsize(640, 480)
        self.photos: dict[str, ImageTk.PhotoImage] = {}
        self._build()

    def _build(self):
        frame = ttk.Frame(self, padding=16)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Mars InSight — Archived Weather",
                  font=("Sans", 21, "bold")).pack(pady=(0, 8))
        ttk.Label(frame, text=(
            "Historical InSight data and images. The mission ended in 2022; "
            "this is not a live Mars weather feed."
        ), wraplength=780).pack(pady=(0, 12))
        tabs = ttk.Notebook(frame)
        tabs.pack(fill="both", expand=True)
        for title, path in ARCHIVED_IMAGES.items():
            tab = ttk.Frame(tabs, padding=12)
            tabs.add(tab, text=title)
            image_label = ttk.Label(tab, anchor="center")
            image_label.pack(fill="both", expand=True)
            try:
                with Image.open(path) as source:
                    image = source.convert("RGB")
                    image.thumbnail((790, 480), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                self.photos[title] = photo
                image_label.configure(image=photo)
            except (OSError, ValueError):
                image_label.configure(text=f"Archived image unavailable: {path.name}")
        ttk.Label(frame, text=(
            "Source: archived NASA InSight materials supplied with this repository. "
            "For current Mars exploration information visit mars.nasa.gov."
        ), wraplength=780).pack(pady=(12, 4))
        ttk.Button(frame, text="Exit", command=self.destroy).pack(pady=5)


if __name__ == "__main__":
    MarsWindow().mainloop()
