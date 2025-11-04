from .operations import Operations
from .calculation import perform_operation
from .help import show_help
from . import history

def main() -> None:    


    print("Simple calculator. Type a menu number to interact. Type '4' or 'q' to quit.")

    while True:
        print("\nMenu:")
        print("1) Perform calculation")
        print("2) Help")
        print("3) History")
        print("4) Exit")

        choice = input("Choose (1/2/3/4): ").strip().lower()

        if choice in ['9', 'q']:
            print("Goodbye!")
            break

        if choice == '2':
            show_help()
            continue

        if choice == '3':
            history.show_history()
            continue

        if choice == '4':
            history.clear_history()
            print("History cleared.")
            continue

        if choice == '5':
            history.clear_last_entry()
            print("Last entry cleared.")
            continue

        if choice == '6':
            history.clear_last_entry()
            print("Redoing last entry.")
            try:
                perform_operation()
            except SystemExit:
                break
            continue

        if choice == '7':
            print("Saving history")
            history.save_history()
            continue

        if choice == '8':
            print("Loaded history")
            history.load_history()
            continue
        

        if choice == '1' or choice == '':
            try:
                perform_operation()
            except SystemExit:
                break
            continue

        print("Unknown choice. Enter 1 to calculate, 5 for help, 6 for history, 7 to exit.")


if __name__ == "__main__":
    main()



