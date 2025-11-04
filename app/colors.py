"""Color utilities for console output using colorama."""
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform support
init(autoreset=True)


class Colors:
    """Color constants for different message types."""
    
    # Success messages (Green)
    SUCCESS = Fore.GREEN
    SUCCESS_BOLD = Style.BRIGHT + Fore.GREEN
    
    # Error messages (Red)
    ERROR = Fore.RED
    ERROR_BOLD = Style.BRIGHT + Fore.RED
    
    # Warning messages (Yellow)
    WARNING = Fore.YELLOW
    WARNING_BOLD = Style.BRIGHT + Fore.YELLOW
    
    # Info messages (Blue)
    INFO = Fore.BLUE
    INFO_BOLD = Style.BRIGHT + Fore.BLUE
    
    # Cyan for headers
    HEADER = Style.BRIGHT + Fore.CYAN
    SUBHEADER = Fore.CYAN
    
    # Magenta for special
    SPECIAL = Fore.MAGENTA
    SPECIAL_BOLD = Style.BRIGHT + Fore.MAGENTA
    
    # White text
    WHITE = Fore.WHITE
    WHITE_BOLD = Style.BRIGHT + Fore.WHITE
    
    # Reset
    RESET = Style.RESET_ALL


def print_header(text: str) -> None:
    """Print a colored header."""
    print(f"\n{Colors.HEADER}{'='*60}")
    print(f"{Colors.HEADER}{text.center(60)}")
    print(f"{Colors.HEADER}{'='*60}{Colors.RESET}\n")


def print_subheader(text: str) -> None:
    """Print a colored subheader."""
    print(f"\n{Colors.SUBHEADER}{'─'*60}")
    print(f"{Colors.SUBHEADER}{text}")
    print(f"{Colors.SUBHEADER}{'─'*60}{Colors.RESET}\n")


def print_success(text: str) -> None:
    """Print a success message in green."""
    print(f"{Colors.SUCCESS_BOLD}✓ {text}{Colors.RESET}")


def print_error(text: str) -> None:
    """Print an error message in red."""
    print(f"{Colors.ERROR_BOLD}✗ {text}{Colors.RESET}")


def print_warning(text: str) -> None:
    """Print a warning message in yellow."""
    print(f"{Colors.WARNING_BOLD}⚠ {text}{Colors.RESET}")


def print_info(text: str) -> None:
    """Print an info message in blue."""
    print(f"{Colors.INFO_BOLD}ℹ {text}{Colors.RESET}")


def print_special(text: str) -> None:
    """Print a special message in magenta."""
    print(f"{Colors.SPECIAL_BOLD}★ {text}{Colors.RESET}")


def highlight(text: str, color=Colors.SPECIAL) -> str:
    """Highlight text with a color."""
    return f"{color}{text}{Colors.RESET}"


def color_text(text: str, color=Colors.WHITE) -> str:
    """Return colored text."""
    return f"{color}{text}{Colors.RESET}"
