from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    @staticmethod
    def hello() -> Literal["""Send /start to begin!"""]: ...

