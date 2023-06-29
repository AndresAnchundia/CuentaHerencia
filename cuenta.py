from abc import ABC, abstractmethod


class Cuenta:
    class Cuenta(ABC):
        def __init__(self, ctanumero=None, propietario=None, saldo: float = 0.0):
            self._ctanumero = ctanumero
            self._propietario = propietario
            self._saldo = saldo

        @property
        def ctanumero(self):
            return self._ctanumero

        @ctanumero.setter
        def ctanumero(self, ctanumero):
            self._ctanumero = ctanumero

        @property
        def propietario(self):
            return self._propietario

        @propietario.setter
        def propietario(self, propietario):
            self._propietario = propietario

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, new_saldo):
            self._saldo = new_saldo

        def __str__(self):
            return f'Cuenta [{self.__dict__.__str__()}]'

        @abstractmethod
        def depositar(self, cantidad):
            pass

        @abstractmethod
        def retirar(self, cantidad):
            pass


if __name__ == '__main__':
    pass

# by Anchundia Asencio Alex Andres
