


from .colors import print_info, Colors, highlight


def show_help() -> None:
    print_info("\nHelp - Available commands:")
    print(f"{Colors.INFO}1:{Colors.RESET} Perform a calculation (you will be prompted for numbers and an operation)")
    print(f"{Colors.INFO}2:{Colors.RESET} Show this help message")
    print(f"{Colors.INFO}3:{Colors.RESET} Show calculation history")
    print(f"{Colors.INFO}4:{Colors.RESET} Clear calculation history")
    print(f"{Colors.INFO}5:{Colors.RESET} Clear last entry from history")
    print(f"{Colors.INFO}6:{Colors.RESET} Redo last entry")
    print(f"{Colors.INFO}7:{Colors.RESET} Save history to file")
    print(f"{Colors.INFO}8:{Colors.RESET} Load history from file")
    print(f"{Colors.INFO}9:{Colors.RESET} Quit")


def show_menu() -> None:
    print(f"\n{Colors.HEADER}Menu:{Colors.RESET}")
    print(f"{Colors.SUCCESS}1){Colors.RESET} Perform calculation")
    print(f"{Colors.SUCCESS}2){Colors.RESET} Help")
    print(f"{Colors.SUCCESS}3){Colors.RESET} History")
    print(f"{Colors.SUCCESS}4){Colors.RESET} Clear History")
    print(f"{Colors.SUCCESS}5){Colors.RESET} Clear Last Entry")
    print(f"{Colors.SUCCESS}6){Colors.RESET} Redo Last Entry")
    print(f"{Colors.SUCCESS}7){Colors.RESET} Save History")
    print(f"{Colors.SUCCESS}8){Colors.RESET} Load History")
    print(f"{Colors.SUCCESS}9){Colors.RESET} Exit")