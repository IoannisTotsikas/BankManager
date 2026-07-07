from bank_system import BankSystem

def main():
    bank = BankSystem()

    while True:
        print("\n--- Τραπεζικό Σύστημα ---")
        print("1. Δημιουργία λογαριασμού")
        print("2. Κατάθεση")
        print("3. Ανάληψη")
        print("4. Μεταφορά χρημάτων")
        print("5. Υπολογισμός τόκου")
        print("6. Εμφάνιση υπολοίπου & ιστορικού")
        print("7. Έξοδος")

        choice = input("Επιλέξτε μια ενέργεια: ")

        if choice == "1":
            owner = input("Όνομα ιδιοκτήτη: ")
            initial = float(input("Αρχικό υπόλοιπο (προαιρετικό, Enter=0): ") or 0)
            account = bank.create_account(owner, initial)
            print(f"Λογαριασμός δημιουργήθηκε! Αριθμός: {account.account_number}")

        elif choice == "2":
            acc_num = input("Αριθμός λογαριασμού: ")
            amount = float(input("Ποσό κατάθεσης: "))
            if bank.deposit(acc_num, amount):
                print("Κατάθεση επιτυχής!")
            else:
                print("Σφάλμα κατάθεσης.")

        elif choice == "3":
            acc_num = input("Αριθμός λογαριασμού: ")
            amount = float(input("Ποσό ανάληψης: "))
            if bank.withdraw(acc_num, amount):
                print("Ανάληψη επιτυχής!")
            else:
                print("Σφάλμα ανάληψης. Ελέγξτε υπόλοιπο ή ποσό.")

        elif choice == "4":
            from_acc = input("Από λογαριασμό: ")
            to_acc = input("Σε λογαριασμό: ")
            amount = float(input("Ποσό μεταφοράς: "))
            if bank.transfer(from_acc, to_acc, amount):
                print("Μεταφορά επιτυχής!")
            else:
                print("Σφάλμα μεταφοράς.")

        elif choice == "5":
            acc_num = input("Αριθμός λογαριασμού: ")
            years = float(input("Χρόνια: "))
            account = bank.find_account(acc_num)
            if account:
                simple = account.calculate_simple_interest(years)
                compound = account.calculate_compound_interest(years)
                print(f"Απλός τόκος: {simple:.2f}€")
                print(f"Σύνθετος τόκος: {compound:.2f}€")
            else:
                print("Λογαριασμός δεν βρέθηκε.")

        elif choice == "6":
            acc_num = input("Αριθμός λογαριασμού: ")
            account = bank.find_account(acc_num)
            if account:
                print(f"Υπόλοιπο: {account.get_balance():.2f}€")
                print("Ιστορικό συναλλαγών:")
                for t in account.get_transactions():
                    print(f" - {t}")
            else:
                print("Λογαριασμός δεν βρέθηκε.")

        elif choice == "7":
            print("Έξοδος από το πρόγραμμα...")
            break

        else:
            print("Μη έγκυρη επιλογή. Δοκιμάστε ξανά.")


if __name__ == "__main__":
    main()