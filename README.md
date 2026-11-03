# Mars InSight Weather — Historical Archive Viewer

Developer: Hamdy Abou El Anein
Contact: hamdy.aea@protonmail.com
License: GNU GPL v3 (see LICENSE).

The NASA InSight lander completed its mission in **December 2022**.
The original EasyGUI application attempted to fetch a live weather feed
and downloaded/overwrote images in the repository. A live InSight
weather feed is no longer available.

This version is an **offline Tkinter archive viewer**. It displays
the archived weather chart and InSight/Mars imagery already stored
in the repository. It does not claim that these are current Mars
conditions and makes no HTTP requests.

## Run

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python MarsGUI.py
```

The original historical application and NASA API logic are preserved
on branch `old`. The old `Mars.log` is retained as historical data
but is no longer overwritten at startup.

## Tests

```sh
python3 -m pytest -q
```

Tests verify the local images can be read. The GUI was also launched
on Manjaro. The archived NASA imagery may carry separate source
attribution requirements; it is not newly relicensed by this rewrite.
