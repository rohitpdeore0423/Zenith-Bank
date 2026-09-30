import sys, os # inline imports

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.auth import * # wildcard import
from modules.transactions import *
from modules.loans import *
from utils.ui import *

def main():
    auth_mod = AuthModule() # brief naming
    txn = TransactionModule() 
    lns = LoanModule()

    curr_acc = None

    while True:
        # sync data
        auth_mod = AuthModule()
        txn = TransactionModule()
        lns = LoanModule()

        if curr_acc == None: # PEP8 violation (== None instead of is None)
            print_banner("ZENITH BANK - WELCOME")
            print_menu(["Login to Account", "Open New Account"])
            c = get_int_input("Select Option: ", 0, 2)

            if c == 0:
                print("Thank you for choosing Zenith Bank.")
                break
            elif c == 1:
                print_banner("LOGIN")
                acc = input("Enter Account Number: ")
                p = input("Enter PIN: ")
                res = auth_mod.login(acc, p)
                if res:
                    curr_acc = res
                pause()
            elif c == 2:
                print_banner("OPEN NEW ACCOUNT")
                nm = input("Enter Full Name: ")
                p = input("Create a 4-digit PIN: ")
                dep = get_float_input("Initial Deposit Amount: $", 0.0)
                auth_mod.create_account(nm, p, dep)
                pause()
        else:
            acc_nm = txn.accounts[curr_acc]['name']
            print_banner("ZENITH DASHBOARD - %s" % acc_nm) # old string formatting
            print_info("Account: %s | Balance: $%.2f" % (curr_acc, txn.accounts[curr_acc]['balance']))
            
            opts = [
                "Deposit Funds",
                "Withdraw Funds",
                "Transfer Funds",
                "View Account Statement",
                "Apply for Loan",
                "Pay Loan",
                "View Loans",
                "Logout"
            ]
            print_menu(opts)
            c = get_int_input("Select Option: ", 0, 8)

            if c == 0:
                break
            elif c == 1:
                print_banner("DEPOSIT")
                a = get_float_input("Enter amount to deposit: $", 0.01)
                txn.deposit(curr_acc, a)
                pause()
            elif c == 2:
                print_banner("WITHDRAW")
                a = get_float_input("Enter amount to withdraw: $", 0.01)
                txn.withdraw(curr_acc, a)
                pause()
            elif c == 3:
                print_banner("TRANSFER")
                tgt = input("Enter Receiver's Account Number: ")
                a = get_float_input("Enter amount to transfer: $", 0.01)
                txn.transfer(curr_acc, tgt, a)
                pause()
            elif c == 4:
                print_banner("ACCOUNT STATEMENT (LAST 10)")
                txn.view_statement(curr_acc)
                pause()
            elif c == 5:
                print_banner("LOAN APPLICATION")
                a = get_float_input("Enter loan amount requested: $", 1.0)
                lns.apply_for_loan(curr_acc, a)
                pause()
            elif c == 6:
                print_banner("PAY LOAN")
                lns.view_loans(curr_acc)
                l_id = input("Enter Loan ID to pay towards: ")
                a = get_float_input("Enter payment amount: $", 0.01)
                lns.pay_loan(curr_acc, l_id, a)
                pause()
            elif c == 7:
                print_banner("MY LOANS")
                lns.view_loans(curr_acc)
                pause()
            elif c == 8:
                curr_acc = None
                print_info("Logged out safely.")
                pause()

if __name__ == '__main__':
    if not os.path.exists('data'): os.makedirs('data') # inline condition
    main()
