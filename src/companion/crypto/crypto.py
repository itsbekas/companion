from rich.console import Group, RenderableType
from rich.panel import Panel
from rich.text import Text

from textual.widget import Widget
from textual.widgets import Placeholder

from .coingecko import CoinGecko

class Crypto(Widget):
    def __init__(self):
        self.cg = CoinGecko()
        super().__init__()
    
    def render(self) -> Panel:
        return Panel(
            Placeholder(),
            title="Crypto"
        )

    @group
    def get_currencies_text(self):
        currencies = self.get_favorite_currencies()
        yield Text("")

    def get_favorite_currencies(self):
        yield 
