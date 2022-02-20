from rich.layout import Layout

class RootLayout(Layout):
    def __init__(self):
        super().__init__(name="root")
        self.split(
            Layout(name="header", size=2),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3)
        )
