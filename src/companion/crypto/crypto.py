from rich import box
from rich.align import Align
from rich.console import group, Group, RenderableType
from rich.panel import Panel
from rich.style import Style
from rich.text import Text

from textual.views import GridView, WindowView
from textual.widget import Widget
from textual.widgets import Placeholder

from .coingecko import CoinGecko

class Crypto(Widget):
    def __init__(self):
        self.cg = CoinGecko()
        super().__init__()
    
    def render(self) -> Panel:

        return Panel(
            self.get_currencies_text(),
            title="Crypto",
            expand=True,
            box=box.SQUARE
        )

    @group()
    def get_currencies_text(self):
        for currency in self.cg.get_currencies():
            yield self.get_currency_text(currency)

    @group()
    def get_currency_text(self, currency):
        yield Text('{}: {}€'.format(currency['name'], currency['price']), end=' ')
        yield Align(PercentageText(currency['24h_change']))

class PercentageText(Text):
    def __init__(self, percentage):
        if percentage > 0.0:
            style="green"
        elif percentage < 0.0:
            style="red"
        elif percentage == 0:
            style="white"

        super().__init__("{:.2f}%".format(percentage), style=Style(color="red"))
