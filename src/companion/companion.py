from rich.live import Live

from crypto.crypto import Crypto
from layout import RootLayout

import asyncio
from time import sleep

l = RootLayout()
c = Crypto()
l["main"].update(c)

with Live(l, refresh_per_second=10, screen=True):
    i = 0
    while i < 1000:
        sleep(1)
        i += 1
        
"""
Available Parameters:
database -- An alternative name for the database (default companion)
"""