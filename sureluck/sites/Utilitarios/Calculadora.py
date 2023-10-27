

class Calculadora:

    def verificarSureBets(self, OddtimeA, OddtimeB):
            res = (1/OddtimeA) + (1/OddtimeB)
            if(res <= 1):
                return 0

            return 1
