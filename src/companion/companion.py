from rich.live import Live

from crypto.crypto import Crypto

from time import sleep

from layout import RootLayout

l = RootLayout()
l["main"].update(Crypto())

with Live(l, refresh_per_second=10, screen=True):
    i = 0
    while i < 1000:
        sleep(0.1)
        i += 1
        
"""
Available Parameters:
database -- An alternative name for the database (default companion)
"""