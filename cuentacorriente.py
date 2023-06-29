from cuenta import Cuenta


class CurrentCount(Cuenta):
    def __init__(self, ctanumero=None, propietario=None, saldo: float = 0.0):
        super().__init__()
        self.ctanumero = ctanumero
        self.propietario = propietario
        self.saldo = saldo
        self._chequera = []

    @property
    def chequera(self):
        return self._chequera

    def __str__(self):
        return f'CountSaving [ctanumero = {self.ctanumero}, propietario = {self.propietario}, ' \
               f'saldo = {self.saldo}, chequera = ¨{self.chequera}]'

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f'Depositaron la cantidad de $ {cantidad} dólares. Su saldo actual es : $ {self.saldo}')

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f'Retiraron $ {cantidad} dólares. Su saldo actual es: $ {self.saldo}')
        else:
            print("Saldo insuficiente")

    def cheque(self, totalcheque):
        if totalcheque <= self.saldo:
            self._chequera.append(totalcheque)
            self.saldo -= totalcheque
            print(f'Se generó un cheque por $ {totalcheque} dólares. Su saldo actual es: $ {self.saldo}')
        else:
            print("Saldo insuficiente para generar nuevo cheque")


if __name__ == '__main__':
    ct1 = CurrentCount(ctanumero='209088774', propietario='María Saldivar', saldo=10000.00)
    print(f'Su número de cuenta es: ', ct1.ctanumero)
    print(f'El nombre del propietario es : ', ct1.propietario)
    print(f'Su saldo es: $', ct1.saldo)

    ct1.depositar(1250)
    ct1.retirar(2500)
    ct1.cheque(1245.67)
    print(f'Proceso de transciones corrientes finalizada')

# by Anchundia Asencio Alex Andres
