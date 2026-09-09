#!/usr/bin/env python3
"""Build a standalone copy of the site with every photo inlined as a data URI.

The site itself loads photos from assets/ — that is the version to deploy.
This script exists only to produce a single-file copy for preview links that
cannot carry a folder alongside them.

    python3 build-preview.py out.html
"""
import base64, mimetypes, pathlib, re, sys

src = pathlib.Path(__file__).parent
html = (src / "index.html").read_text()

def inline(match):
    path = src / match.group(1)
    if not path.exists():
        return match.group(0)
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    data = base64.b64encode(path.read_bytes()).decode()
    return 'src="data:%s;base64,%s"' % (mime, data)

out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "preview.html")
out.write_text(re.sub(r'src="(assets/[^"]+)"', inline, html))
print("wrote %s (%.0f KB)" % (out, out.stat().st_size / 1024))
