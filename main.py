import random

MAX_LINES = 3
MAX_BET = 2000
MIN_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A":1,
    "B":3,
    "C":5,
    "D":7
}

symbol_values = {
    "A":4,
    "B":3,
    "C":2,
    "D":1
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines

def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
                
        print()
    

def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                input("Please enter a value greater than zero. Enter to continue.")
                continue
        else:
            input("Please enter a valid number. Enter to continue.")
            continue
    return amount

def  get_num_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                input("Enter a valid number of lines. Enter to continue.")
        else:
            input("Please enter a valid number. Enter to continue.")
            
    
def get_bet():
    while True:
        amount = input("Enter the amount you would like to bet on each line : ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                input(f"Please enter a value in range {MIN_BET}Rs - {MAX_BET}Rs. Enter to continue.")
                continue
        else:
            input("Please enter a valid number. Enter to continue.")
            continue
    return amount

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            input(
                f"You do not have enough balance to bet that amount. Your balance is {balance}Rs. Press Enter to continue."
            )
        else:
            break

    print(f"You are betting {bet}Rs on {lines} lines. Total bet is {total_bet}Rs.")
    
    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots) 
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    
    print(f"You won {winnings}Rs!")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: {balance}Rs")
        choice = input("Press Enter to play! [Press 'q' to quit]: ")
        if choice.lower() == "q":
            break
        balance += spin(balance)
        print(f"You are left with {balance}Rs!\n")

main()