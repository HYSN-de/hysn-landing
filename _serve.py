#!/usr/bin/env python3
"""Local preview that tells the browser not to cache anything, so every reload shows the current build.
Usage: python3 _serve.py [port]   then open http://localhost:8080/"""
import sys, pathlib, functools, http.server

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
root = pathlib.Path(__file__).resolve().parent
print(f"http://localhost:{port}/")
http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(NoCache, directory=str(root))).serve_forever()
