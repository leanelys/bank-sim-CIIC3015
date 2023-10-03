#!/bin/python3

# Project 1 Phase 2 of UPRM CIIC 3015 Fall 2023 

# Repeated symbol count for header messages
BORDER_COUNT = 25
# Repeats the symbol for formatted text borders
STAR_BORDER = "*" * BORDER_COUNT
DASH_BORDER = "-" * BORDER_COUNT

# Menu options to compare with choice
DEPOSIT_FUNDS_MENU_CHOICE = "1"
WITHDRAW_FUNDS_MENU_CHOICE = "2"
VIEW_BALANCE_MENU_CHOICE = "3"
# Only shown if balance is greater than or equal to zero
CLOSE_ACCOUNT_MENU_CHOICE = "4"

# Counters
penalty_cnt = 0
withdrawal_cnt = 0
deposit_cnt = 0

# Welcome message
print("\n" + STAR_BORDER + "\nWelcome to Banco Popular!\n" + STAR_BORDER)


#
# Setup Account
#

print("\n" + (DASH_BORDER) + "\nAccount Setup\n" + (DASH_BORDER) + "\n")
name = input("Account name: ")

# Selecting starting balance
while True:
  s_balance = input("Starting balance: $")

# Data validation for the starting balance
  # If starting balance is an integer:
  try:
    string_int = int(s_balance)
    if (s_balance == str(string_int) and float(s_balance) > 0):
        # Convert starting balance to float to avoid errors during .2f formatting
        s_balance = float(s_balance)
    # Show account name and starting balance
        print(
            "\nWelcome new account member!\n"
            f"Account {name} created with starting balance: ${s_balance:.2f}")
        break

  except:
  # If starting balance is a two decimal point float:
    try:
      string_format = format(float(s_balance), '.2f')
      if (s_balance == string_format and float(s_balance) > 0):
        # Convert starting balance to float to avoid errors during .2f formatting
        s_balance = float(s_balance)
    # Showing account name and starting balance
        print(
            "\nWelcome new account member!\n"
            f"Account {name} created with starting balance: ${s_balance:.2f}")
        break
      
    except:
      # Loop for invalid starting balance inputs
      continue

# Assign starting balance value to current balance
balance = s_balance


#
# Main Account Menu
#

# Main menu selection
if balance >= 0:
# Close account is available
    choice = input(
        "\nSelect option:\n"
        "(1) Deposit funds\n"
        "(2) Withdraw funds\n"
        "(3) View bank account balance\n"
        "(4) Close account\n")

    # Close account is unavailable
else:
    choice = input(
        "\nSelect option:\n"
        "(1) Deposit funds\n"
        "(2) Withdraw funds\n"
        "(3) View bank account balance\n")

# Loop for repeated menu selection
while choice != '4':
    # Invalid option
    if choice != '1' and choice != '2' and choice != '3' and choice != '4':
        print('Invalid option')


    #
    # Deposit
    #

    elif choice == '1':
    # Title message
        print("\n" + (DASH_BORDER) + "\nDeposit Funds\n" + (DASH_BORDER) + "\n")

    # Deposit input
        deposit_amt = input('Amount to deposit: $')

        # Data validation for the deposited amount

    # Valid deposit amounts
        # If deposited amount is an integer:
        try:
            if float(deposit_amt) > 0:
                string_int = int(deposit_amt)
                if deposit_amt == str(string_int):
                # Converting deposited amount to float to avoid errors during .2f formatting
                    deposit_amt = float(deposit_amt)
                # Show deposit details
                    print(f'Account name: {name}')
                    print(f'Deposit amount: ${deposit_amt: .2f}')
                    balance = balance + deposit_amt
                    print(f'New Balance: ${balance: .2f}')
                    deposit_cnt += 1
                else:
                    print('Transaction failed: Invalid deposit amount.')
            else:
                print('Transaction failed: Invalid deposit amount.')

        except:
        # If deposited amount is a two decimal point float:
            try:
                if float(deposit_amt) > 0:
                    string_format = format(float(deposit_amt), '.2f')
                    if deposit_amt == string_format:
                    # Convert starting balance to float to avoid errors during .2f formatting
                        deposit_amt = float(deposit_amt)
                    # Show deposit details
                        print(f'Account name: {name}')
                        print(f'Deposit amount: ${deposit_amt: .2f}')
                        balance = balance + deposit_amt
                        print(f'New Balance: ${balance: .2f}')
                        deposit_cnt += 1
                    else:
                        print('Transaction failed: Invalid deposit amount.')
                else:
                    print('Transaction failed: Invalid deposit amount.')
            except:
                # If desposited amount is invalid:
                print('Transaction failed: Invalid deposit amount.')
                pass


    #
    # Withdrawal
    #

    elif choice == '2':
    # Title message and withdraw input
        print("\n" + (DASH_BORDER) + "\nWithdraw Funds\n" + (DASH_BORDER) + "\n")
        withdraw_amt = round(float(input('Amount to withdraw: $')), 2)

    # Invalid withdrawal amounts
        if withdraw_amt <= 0:
            print('Transaction failed: Invalid withdrawal amount.')
        
    # Valid withdrawal amounts
        elif withdraw_amt > 0:
            print(f"Account Name: {name}")
            print(f'Withdrawal Amount: ${withdraw_amt: .2f}')
            balance -= withdraw_amt
        
        # No penalty
            if balance >= -100:
                print('Penalties: $0.00' + '\n' + 
                    f'New Balance: ${balance: .2f}')
                withdrawal_cnt += 1
            
        # 1% penalty
            elif balance < -100 and balance > -1000:
                penalty = withdraw_amt*0.01
                balance -= penalty
                print('Withdrawal amount is greater than account balance. Overdraft penalty of 1% applied.' + '\n' + 
                    f'Penalties: ${penalty: .2f}' + '\n' + 
                    f'New Balance: ${balance: .2f}')
                withdrawal_cnt += 1
                penalty_cnt += 1
            
        # 3% penalty
            elif balance <= -1000 and balance > -5000:
                penalty = withdraw_amt*0.03
                balance -= penalty
                print('Withdrawal amount is greater than account balance. Overdraft penalty of 3% applied.'+ '\n' + 
                    f'Penalties: ${penalty: .2f}' + '\n' + 
                    f'New Balance: ${balance: .2f}')
                withdrawal_cnt += 1
                penalty_cnt += 1
            
            # Currency in bills and coins
            if balance > -5000:
                # Multiplication by 100 to avoid rounding issues
                temp_withdraw = withdraw_amt * 100
                # $100 bills
                hundreds = temp_withdraw // 10000
                remainder = temp_withdraw % 10000

                # $50 bills
                fifties = remainder // 5000
                remainder %= 5000

                # $20 bills
                twenties = remainder // 2000
                remainder %= 2000

                # $10 bills
                tens = remainder // 1000
                remainder %= 1000

                # $5 bills
                fives = remainder // 500
                remainder %= 500

                # $1 bills
                ones = remainder // 100
                remainder %= 100

                # quarters ($0.25)
                quarters = remainder // 25
                remainder %= 25

                # nickels ($0.10)
                nickels = remainder // 10
                remainder %= 10

                # dimes ($0.05)
                dimes = remainder // 5
                remainder %= 5

                # pennies ($0.01)
                pennies = remainder // 1

                print('Currency withdrawn:')
                if hundreds > 0:
                    print(f'$100s: {hundreds}')
                if fifties > 0:
                    print(f'$50s: {fifties}')
                if twenties > 0:
                    print(f'$20s: {twenties}')
                if tens > 0:
                    print(f'$10s: {tens}')
                if fives > 0:
                    print(f'$5s: {fives}')
                if ones > 0:
                    print(f'$1s: {ones}')
                if quarters > 0:
                    print(f'quarters: {quarters}')
                if nickels > 0:
                    print(f'nickels: {nickels}')
                if dimes > 0:
                    print(f'dimes: {dimes}')
                if pennies > 0:
                    print(f'pennies: {pennies}')

        # Overdraft limit exceeded
            elif balance <= -5000:
                balance += withdraw_amt
                print('Transaction failed: withdrawal amount exceeds overdraft limit.')


    #
    # View balance
    #

    elif choice == '3':
        print("\n" + (DASH_BORDER) + "\nAccount Balance\n" + (DASH_BORDER) + "\n")
        print(f'Account Name: {name}')
        print(f'Balance: ${balance: .2f}')


    #
    # Main menu (loop)
    #
    if balance >= 0:
    # Close account is available
        choice = input(
            "\nSelect option:\n"
            "(1) Deposit funds\n"
            "(2) Withdraw funds\n"
            "(3) View bank account balance\n"
            "(4) Close account\n")

    # Close account is unavailable
    else:
        choice = input(
            "\nSelect option:\n"
            "(1) Deposit funds\n"
            "(2) Withdraw funds\n"
            "(3) View bank account balance\n")

#
# Close account
#

if choice == '4' and balance >= 0:
    print("\n" + (STAR_BORDER) + "\nClosing Account\n" + (STAR_BORDER))
    print('\n' + (DASH_BORDER) + '\nFinal Acccount Statement\n' + (DASH_BORDER))

    # Percentage of change in balance
    balance_change = (((balance - s_balance) / balance) * 100)

    # Final account statement details
    print(f'Account name: {name}' + '\n'
          f'Initial balance: ${s_balance: .2f}')
    if balance_change < 0:
        print(f'Final balance: ${balance: .2f} (-{balance_change: .2f}%)')
    else:
        print(f'Final balance: ${balance: .2f} (+{balance_change: .2f}%)')
    print(f'Deposit count: {deposit_cnt}' + '\n'
          f'Withdrawal count: {withdrawal_cnt}' + '\n'
          f'Overdraft penalty count: {penalty_cnt}')


# Exit message
print("\nThank you for banking with Banco Popular!")