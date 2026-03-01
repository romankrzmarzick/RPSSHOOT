from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.text import Text
console = Console()

choices = ["3", "5", "7"]
pll = Prompt.ask("hello", choices=[*choices])