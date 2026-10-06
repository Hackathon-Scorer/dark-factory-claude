"""Start the band's stage-4 service unchanged, then seed it with demo data once it is healthy.

The service keeps state in memory, so a fresh container (or a host that restarts it) would
otherwise show no restaurants. Seeding goes through the service's own reset endpoint.
"""
import os
import subprocess
import sys
import time
import urllib.request

port = os.environ.get("PORT", "8080")
base = f"http://127.0.0.1:{port}"
app = subprocess.Popen([sys.executable, "-u", "/app/app.py"])

for _ in range(120):
    try:
        if urllib.request.urlopen(base + "/health", timeout=2).status == 200:
            break
    except Exception:
        time.sleep(0.5)
with open("/app/demo-fixture.json", "rb") as fixture:
    req = urllib.request.Request(base + "/_test/reset", data=fixture.read(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    print("demo data loaded:", urllib.request.urlopen(req, timeout=10).status, flush=True)
sys.exit(app.wait())
