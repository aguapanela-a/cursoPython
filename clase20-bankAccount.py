## POO EN PYTHON ##

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder  = account_holder
        self.balance = balance
        self.is_Active = True
    
    def deposit_withdraw_money(self, amount): ## Este método Viola el Principio de Responsabilidad Única: Una función debería hacer una sola cosa. Aquí, la función maneja la lógica, la interfaz (inputs) y la validación.
        if self.is_Active:
            
            while True:
                decision = input(f"¿Qué desea hacer con esos {amount}$?  ----  saldo actual: {self.balance}$ \n  Retirar dinero: A\n  Depositar dinero: B \n -> ")
                
                if decision.upper() == "A":
                    if amount > self.balance:
                        print("No e puede retirar más de lo que tiene bobo hijueputa")
                    else:
                        amount *= -1
                        break
                elif decision.upper() == "B":
                    break
                    
                
            self.balance += amount
            print(f"La acción seleccionada se realizó con {amount}. El saldo actual es {self.balance}.")
                
                
        else:
            print("No se puede realiar la acción porque la cuenta está inacitva")
    
    def deactivate_Account(self):
        if self.is_Active:
            self.is_Active = False
            print("Cuenta desactivada con éxito")
        else:
            print("Su cuenta ya está desactivada bobo hijueputa")
    
    def activate_Account(self):
        if self.is_Active:
            print("Su cuenta ya está activada bobo hijueputa")
            
        else:
            self.is_Active = True
            print("Cuenta activada con éxito")
            
            
            
cuenta1 = BankAccount("Erick", 300)

cuenta1.deposit_withdraw_money(800)

#cuenta1.deactivate_Account()

cuenta1.deposit_withdraw_money(10000)