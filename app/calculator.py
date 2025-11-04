from .operations import Operations
from .calculation import perform_operation
from .help import show_help
from . import history
from .help import show_menu
from .colors import print_header, print_success, print_info, print_error, Colors


def main() -> None:    
    print_header("Simple Calculator")
    print_info("Type a menu number to interact. Type '9' or 'q' to quit.")

    while True:
        show_menu()
        choice = input(f"{Colors.INFO}Choose a number: {Colors.RESET}").strip().lower()

        if choice in ['9', 'q']:
            print_success("Goodbye!")
            break

        if choice == '2':
            show_help()
            continue

        if choice == '3':
            history.show_history()
            continue

        if choice == '4':
            history.clear_history()
            print_success("History cleared.")
            continue

        if choice == '5':
            history.clear_last_entry()
            print_success("Last entry cleared.")
            continue

        if choice == '6':
            history.clear_last_entry()
            print_info("Redoing last entry.")
            try:
                perform_operation()
            except SystemExit:
                break
            continue

        if choice == '7':
            print_info("Saving history")
            history.save_history()
            continue

        if choice == '8':
            print_info("Loaded history")
            history.load_history()
            continue
        

        if choice == '1' or choice == '':
            try:
                perform_operation()
            except SystemExit:
                break
            continue

        print_error("Unknown choice. Enter 1 to calculate, 2 for help, 3 for history, 4 to clear history.")


if __name__ == "__main__":
    main()



