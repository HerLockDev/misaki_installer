

from json import loads
from rich.prompt import Prompt
from rich.panel import Panel
from rich.live_render import LiveRender
from . import logo, console, dilsec, lsoru

def importlang ():
    console.clear()
    logo()

    dilsec(f"[1] [bold red]TÜRK[/][bold white]ÇE")
    dilsec(f"[2] [bold cyan]AZƏR[/][bold red]BAYCAN[/][bold green]CA")
    dilsec(f"[3] [bold red]ENG[/][bold white]LI[/][blue]SH")
    dilsec(f"[4] [bold cyan]O'[/][bold white]ZB[/][bold green]EK")

    lsoru(Panel(f"\n[bold yellow]💬 Bir dil seçin: \n\n💬 Please select a language: \n"))
    Dil = Prompt.ask(f"❓", choices=["1", "2", "3", "4"], default="1")

    if Dil == "1":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"
    elif Dil == "2":
        COUNTRY = "Azerbaijan"
        LANGUAGE = "AZ"
        TZ = "Asia/Baku"
    elif Dil == "3":
        COUNTRY = "United Kingdom"
        LANGUAGE = "EN"
        TZ = "Europe/London"
    elif Dil == "4":
        COUNTRY = "Uzbekistan"
        LANGUAGE = "UZ"
        TZ = "Asia/Tashkent"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./installer/language/{LANGUAGE}.dogejson", "r").read())["STRINGS"]
