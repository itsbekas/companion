import asyncio

from requests.exceptions import ConnectionError

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

def test():
    asyncio.create_task()

class Crypto(Widget):
    def __init__(self):
        self.cg = CoinGecko()
        self.render_text = Text('Connecting to CoinGecko...')
        self.update_text()
        super().__init__()
    
    def render(self) -> Panel:

        return Panel(
            Align.center(
                self.render_text),
            title="Crypto",
            expand=True,
            box=box.SQUARE,
            style='bright_white on grey11'
        )

    def update_text(self):
        try:
            self.render_text = self.get_currencies_text()
        except ConnectionError:
            self.render_text = Text('Connection failed.')

    @group()
    def get_currencies_text(self):
        for currency in self.cg.get_currencies():
            yield self.get_currency_text(currency)

    @group()
    def get_currency_text(self, currency):
        yield Text(
            '{}: {}€'.format(currency['name'], currency['price']),
            end=' ',
            style='bright_white'
        )
        yield PercentageText(currency['24h_change'])

class PercentageText(Text):
    def __init__(self, percentage):
        if percentage > 0:
            style="spring_green2"
        elif percentage < 0:
            style="rgb(255,75,75)"
        elif percentage == 0:
            style="bright_white"

        super().__init__("{:.2f}%".format(percentage), style=style)
