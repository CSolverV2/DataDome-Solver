import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Logger:
    def __init__(self, name):
        self.name = name

    def get_time(self):
        return time.strftime("%H:%M:%S")

    def log(self, level_color, level_name, message_color, message):
        msg = (
            f"{Fore.CYAN}[{self.name}]"
            f" {Fore.LIGHTWHITE_EX}[{self.get_time()}]"
            f" {level_color}{level_name}{Style.RESET_ALL} -> {message_color}{message}{Style.RESET_ALL}"
        )
        print(msg)

    def info(self, message):
        self.log(Fore.YELLOW, "[Info]", Fore.LIGHTBLUE_EX,f"{Fore.LIGHTWHITE_EX}[ {Fore.YELLOW+message} {Fore.LIGHTWHITE_EX}]")

    def success(self, message):
        self.log(Fore.GREEN, "[Success]",Fore.LIGHTBLUE_EX,f"{Fore.LIGHTWHITE_EX}[ {Fore.GREEN+message} {Fore.LIGHTWHITE_EX}]")