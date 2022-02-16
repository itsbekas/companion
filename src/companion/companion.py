from textual.app import App

from crypto.crypto import Crypto

class Companion(App):

    def load_db(self, db):
        """Loads database if existing, else creates one"""
        pass
    
    async def on_mount(self) -> None:
        await self.view.dock(Crypto())

Companion.run()
"""
Available Parameters:
database -- An alternative name for the database (default companion)
"""