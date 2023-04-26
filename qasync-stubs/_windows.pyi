import asyncio
import sys

if sys.platform == "win32":
    class _ProactorEventLoop(asyncio.ProactorEventLoop): ...
