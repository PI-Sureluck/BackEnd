

class Calculadora:

    def verificarSureBets(self, OddtimeA, OddtimeB):
            print(OddtimeA,OddtimeB)
            res = (1/OddtimeA) + (1/OddtimeB)
            print(res)
            if(res >= 1):
                return 0
            return 1

    def verificarValorApostar(self, OddtimeA, OddtimeB):
        res = (1 / OddtimeA) + (1 / OddtimeB)
        res2 = (1 / res) * 100
        timeA = (1 / OddtimeA) * res2
        timeB = (1 / OddtimeB) * res2
        print(timeA, timeB)
        return [timeA, timeB]

