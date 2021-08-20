# MyBudget by: Brandon Walker

class Master:
    def __int__(self, f, c, b, o, t, total_amount, amount_food_spend, amount_clothes_spend, amount_bills_spend):
        self.total_amount = total_amount
        self.amount_food_spend = amount_food_spend
        self.amount_clothes_spend = amount_clothes_spend
        self.amount_bills_spend = amount_bills_spend
        self.fD = f
        self.cD = c
        self.bD = b
        self.oD = o
        self.tD = t

        print(f'-----------------------------------------------------------------------------'
              f'\nOverview:'
              f'\nIf you spend ${self.amount_food_spend} on food, then {(self.amount_food_spend / self.total_amount) * 100}% of the money you have available goes to food'
              f'\nIf you spend ${self.amount_clothes_spend} on clothes, then {(self.amount_clothes_spend / self.total_amount) * 100}% of the money you have available goes to clothes'
              f'\nIf you spend ${self.amount_bills_spend} on bills, then {(self.amount_bills_spend / self.total_amount) * 100}% of the money you have available goes to bills'
              f'\nYou have ${self.total_amount - (self.amount_food_spend + self.amount_bills_spend + self.amount_clothes_spend)} or {((total_amount - (amount_food_spend + amount_bills_spend + amount_clothes_spend)) / total_amount) * 100}% of your original budget to spend on whatever')


class Menu(Master):
    def startup(self):
        super().__int__(
            [0],
            [0],
            [0],
            [0],
            [0],
            int(input('Enter your starting amount: ')),
            int(input('Enter your amount you spend on food: ')),
            int(input('Enter your amount you spend on clothing: ')),
            int(input('Enter your amount you spend on bills: ')))
        self.fD.append(self.amount_food_spend)
        self.cD.append(self.amount_clothes_spend)
        self.bD.append(self.amount_bills_spend)
        self.oD.append(
            self.total_amount - (self.amount_food_spend + self.amount_bills_spend + self.amount_clothes_spend))
        self.tD.append(self.total_amount)
        store_values = open('Storage.py', 'w')
        i = [self.fD[-1], self.cD[-1], self.bD[-1], self.oD[-1], self.tD[-1]]
        for values in i:
            store_values.writelines('a = ' + str(i))
            break

    def saved(self):
        from Storage import a
        super().__int__(
            [0],
            [0],
            [0],
            [0],
            [0],
            a[4],
            a[0],
            a[1],
            a[2])
        self.fD.append(self.amount_food_spend)
        self.cD.append(self.amount_clothes_spend)
        self.bD.append(self.amount_bills_spend)
        self.oD.append(self.total_amount - (self.amount_food_spend + self.amount_bills_spend + self.amount_clothes_spend))
        self.tD.append(self.amount_food_spend + self.amount_clothes_spend + self.amount_bills_spend + (self.total_amount - (self.amount_food_spend + self.amount_bills_spend + self.amount_clothes_spend)))
    def deposit(self):
        amount_left_over = self.total_amount - (
                self.amount_food_spend + self.amount_bills_spend + self.amount_clothes_spend)
        change = input('You said you would like to make a deposit? ')
        print(change)
        if 'yes' in change:
            change_amount = int(input('How much would you like to deposit? '))
            new_total = change_amount + self.total_amount
            print('-----------------------------------------------------------------------------'
                  '\nCategories (case sensitive):'
                  '\nFood - food'
                  '\nClothes - clothes'
                  '\nBills - bills'
                  '\nMoney left over - balance')
            budget_category = input('What category should it go into? ')
            if 'food' in budget_category:
                self.fD.append(self.fD[-1] + change_amount)
                self.cD.append(self.cD[-1])
                self.bD.append(self.bD[-1])
                self.oD.append(self.oD[-1])
                self.tD.append(self.tD[-1] + change_amount)
                print(f'-----------------------------------------------------------------------------'
                      f'\nYou deposited ${change_amount} into the food category and your new total there is ${self.fD[-1]}')
            if 'clothes' in budget_category:
                self.fD.append(self.fD[-1])
                self.cD.append(self.cD[-1] + change_amount)
                self.bD.append(self.bD[-1])
                self.oD.append(self.oD[-1])
                self.tD.append(self.tD[-1] + change_amount)
                print(f'-----------------------------------------------------------------------------'
                      f'\nYou deposited ${change_amount} into the clothing category and your new total there is ${self.cD[-1]}')
            if 'bills' in budget_category:
                self.fD.append(self.fD[-1])
                self.cD.append(self.cD[-1])
                self.bD.append(self.bD[-1] + change_amount)
                self.oD.append(self.oD[-1])
                self.tD.append(self.tD[-1] + change_amount)
                print(f'-----------------------------------------------------------------------------'
                      f'\nYou deposited ${change_amount} into the bills category and your new total there is ${self.bD[-1]}')
            if 'balance' in budget_category:
                self.fD.append(self.fD[-1])
                self.cD.append(self.cD[-1])
                self.bD.append(self.bD[-1])
                self.oD.append(self.oD[-1] + change_amount)
                self.tD.append(self.tD[-1] + change_amount)
                print(f'-----------------------------------------------------------------------------'
                      f'\nYou deposited ${change_amount} into the left over category and your new total there is ${self.oD[-1]}')
            print(f'  '
                  f'\nOverview:'
                  f'\nFood, ${self.fD[-1]} -- {((self.fD[-1]) / (self.tD[-1])) * 100}% of what you have available '
                  f'\nClothes, ${self.cD[-1]} -- {((self.cD[-1]) / (self.tD[-1])) * 100}% of what you have available '
                  f'\nBills, ${self.bD[-1]} -- {((self.bD[-1]) / (self.tD[-1])) * 100}% of what you have available '
                  f'\nLeft over, ${self.oD[-1]} -- {(self.oD[-1] / (self.tD[-1])) * 100}% of what you have available')
            store_values = open('Storage.py', 'w')
            i = [self.fD[-1], self.cD[-1], self.bD[-1], self.oD[-1], self.tD[-1]]
            for values in i:
                store_values.writelines('a = ' + str(i))
                break
        else:
            pass

    def transfer(self):
        transfer_change = input('You said you would like to make a transfer? ')
        if 'yes' in transfer_change:
            transfer_amount = int(input('How much do you want to transfer? '))
            start = input('What category do you want to take from? ')
            if 'food' in start:
                self.fD.append(self.fD[-1] - transfer_amount)
            if 'clothes' in start:
                self.cD.append(self.cD[-1] - transfer_amount)
            if 'bills' in start:
                self.bD.append(self.bD[-1] - transfer_amount)
            if 'balance' in start:
                self.oD.append(self.oD[-1] - transfer_amount)
            end = input('What category do you want to move it to? ')
            end1 = end
            if 'food' in end:
                self.fD.append(self.fD[-1] + transfer_amount)
                end1 = self.fD[-1]
            if 'clothes' in end:
                self.cD.append(self.cD[-1] + transfer_amount)
                end1 = self.cD[-1]
            if 'bills' in end:
                self.bD.append(self.bD[-1] + transfer_amount)
                end1 = self.bD[-1]
            if 'balance' in end:
                self.oD.append(self.oD[-1] + transfer_amount)
                end1 = self.oD[-1]
            print(f'-----------------------------------------------------------------------------'
                  f'\nYour new balance in your {end} category is ${end1}'
                  f'\n'
                  f'\nOverview:'
                  f'\nFood, ${self.fD[-1]} -- {((self.fD[-1]) / (self.tD[-1])) * 100}% of what you have available '
                  f'\nClothes, ${self.cD[-1]} -- {((self.cD[-1]) / (self.tD[-1])) * 100}% of what you have available '
                  f'\nBills, ${self.bD[-1]} -- {((self.bD[-1]) / (self.tD[-1])) * 100}% of what you have available '
                  f'\nLeft over, ${self.oD[-1]} -- {(self.oD[-1] / (self.tD[-1])) * 100}% of what you have available')
            i = [self.fD[-1], self.cD[-1], self.bD[-1], self.oD[-1], self.tD[-1]]
            store_values = open('Storage.py', 'w')
            for values in i:
                store_values.writelines('a = ' + str(i))
                break
        else:
            pass

    def overview(self):
        print(f'-----------------------------------------------------------------------------'
              f'\nOverview:'
              f'\nFood, ${self.fD[-1]} -- {((self.fD[-1]) / (self.tD[-1])) * 100}% of what you have available '
              f'\nClothes, ${self.cD[-1]} -- {((self.cD[-1]) / (self.tD[-1])) * 100}% of what you have available '
              f'\nBills, ${self.bD[-1]} -- {((self.bD[-1]) / (self.tD[-1])) * 100}% of what you have available '
              f'\nLeft over, ${self.oD[-1]} -- {(self.oD[-1] / (self.tD[-1])) * 100}% of what you have available')

i = Menu()

print('-----------------------------------------------------------------------------'
      '\nWelcome to MyBudget'
      '\n '
      )

overwrite = input('Would you like to overwrite your data: ')
if 'no' in overwrite:
    i.saved()
if 'yes' in overwrite:
    i.startup()
while True:

    print('-----------------------------------------------------------------------------'
          '\nMenu: '
          '\nMake a deposit -- type: deposit '
          '\nMake a transfer from one category to another -- type: transfer'
          '\nSee an overview of your budget-- type: overview'
          '\nStop the program -- type: exit')
    action = input('What would you like to do today? ')
    if 'deposit' in action:
        print(i.deposit())
    else:
        pass
    if 'transfer' in action:
        print(i.transfer())
    else:
        pass
    if 'overview' in action:
        print(i.overview())
    else:
        pass
    if 'exit' in action:
        input('Press ENTER to Exit')
        break
