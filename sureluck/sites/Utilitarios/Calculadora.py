class Calculadora:

    def verificarSureBets(self, OddtimeA, OddtimeB):
        res = (1 / OddtimeA) + (1 / OddtimeB)
        if res < 1:
            return 1  # É uma surebet
        return 0  # Não é uma surebet

    def verificarValorApostar(self, OddtimeA, OddtimeB):
        res = (1 / OddtimeA) + (1 / OddtimeB)
        res2 = (1 / res) * 100
        timeA = (1 / OddtimeA) * res2
        timeB = (1 / OddtimeB) * res2
        print(timeA, timeB)
        return [timeA, timeB]
