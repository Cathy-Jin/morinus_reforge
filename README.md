# Morinus Reforge (macOS)

This is a macOS-focused refurbish of the legacy Morinus codebase to run on modern Python 3 and wxPython.

## Status
- Python 3 + wxPython 4 compatibility shims added.
- Swiss Ephemeris via `pyswisseph` (shimmed as `sweastrology`).
- Pillow compatibility shims for legacy PIL imports.

## Quick start
```sh
python3 -m pip install pyswisseph pillow wxPython
python3 morinus.py
```

## Notes
- Some legacy APIs are shimmed in `morinus.py` and `sweastrology.py`.
- If you find a runtime error, capture the traceback and patch the shim layer first.

## License
See original project license in the source files.
