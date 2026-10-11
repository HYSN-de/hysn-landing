#!/usr/bin/env python3
"""Build the HYSN site. Every module in pages/ defines PAGES = [dict(path, title, desc, current, body, body_class, css)].
Usage: python3 _build.py            build every page
       python3 _build.py faq kontakt only build pages/faq.py and pages/kontakt.py"""
import sys, pathlib, importlib.util, traceback
sys.dont_write_bytecode = True
ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import _lib

only, ok, mods = set(sys.argv[1:]), True, []
# load every module first, so header and footer can link to pages that are built later in this run
for f in sorted((ROOT / "pages").glob("*.py")):
    try:
        spec = importlib.util.spec_from_file_location(f"page_{f.stem}", f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        _lib.PLANNED.update(p["path"] for p in mod.PAGES)
        mods.append((f, mod))
    except Exception:
        ok = False; print(f"FAILED pages/{f.name}"); traceback.print_exc()
for f, mod in mods:
    if only and f.stem not in only:
        continue
    try:
        for p in mod.PAGES:
            _lib.page(**p)
    except Exception:
        ok = False; print(f"FAILED pages/{f.name}"); traceback.print_exc()
sys.exit(0 if ok else 1)
