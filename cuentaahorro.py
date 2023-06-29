from cuenta import Cuenta


class CountSaving(Cuenta):
    def __init__(self, ctanumero=None, propietario=None, saldo: float = 0.0,
                 interes: float = 0.00):
        super().__init__()
        self.ctanumero = ctanumero
        self.propietario = propietario
        self.saldo = saldo
        self._interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, nueva_tasa):
        self._interes = nueva_tasa

    def __str__(self):
        return f'CountSaving [ctanumero = {self.ctanumero}, propietario = {self.propietario}, ' \
               f'saldo = {self.saldo}, interes = ¨{self.interes}]'

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f'Depositaron la cantidad de $ {cantidad} dólares. Su saldo actual es : $ {self.saldo}')

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f'Retiraron $ {cantidad} dólares. Su saldo actual es: $ {self.saldo}')
        else:
            print("Saldo insuficiente")

    def cal_interes(self):
        tasainteres = self.saldo * self.interes
        self.saldo += tasainteres
        print(f'Los intereses a su favor son: ${tasainteres}. Su saldo actual: ${self.saldo}')


if __name__ == '__main__':
    ct1 = CountSaving(ctanumero='102036344', propietario='Juan Andrade', saldo=3000.00, interes=0.02)
    print(f'Su número de cuenta es: ', ct1.ctanumero)
    print(f'El nombre del propietario es : ', ct1.propietario)
    print(f'Su saldo es: $', ct1.saldo)
    print(f'La tasa de interes es: ', ct1.interes)

    ct1.depositar(250)
    ct1.retirar(400)
    ct1.interes = 0.02
    ct1.cal_interes()
    print(f'Fin de transacciones de ahorro')

# by Anchundia Asencio Alex Andres
