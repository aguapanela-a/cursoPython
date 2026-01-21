class CuentaBancaria:
    def __init__(self, balance, is_Active):
        self.balance = balance
        self.is_Active = is_Active

    # --- MÉTODOS LÓGICOS (No usan input, son fáciles de testear) ---
    def depositar(self, amount):
        if amount <= 0:
            return "El monto debe ser positivo."
        self.balance += amount
        return f"Depósito exitoso. Saldo: {self.balance}"

    def retirar(self, amount):
        if amount > self.balance:
            return "Saldo insuficiente." # Aquí cambiamos el mensaje agresivo por algo estándar jaja
        if amount <= 0:
            return "Monto inválido."
        self.balance -= amount
        return f"Retiro exitoso. Saldo: {self.balance}"
    
    def inactivar(self):
        self.is_Active = False
    
    def activar(self):
        self.is_Active = True

    # --- MODO INTERACTIVO (El menú que tú querías) ---
    def menu_transaccion(self, amount):
        if not self.is_Active:  ## validaciones
            print("Cuenta inactiva.")
            return

        while True:  ## inputs
            opcion = input(f"Saldo: {self.balance} | ¿Qué hacer con {amount}$?\nA) Retirar\nB) Depositar\n-> ").upper()
            
            if opcion == "A":
                print(self.retirar(amount))
                break
            elif opcion == "B":
                print(self.depositar(amount))
                break
            else:
                print("Opción no válida.")

cuentaBancaria = CuentaBancaria(10_000, True)

cuentaBancaria.menu_transaccion(11_000)

#cuentaBancaria.inactivar()

cuentaBancaria.menu_transaccion(20_000)