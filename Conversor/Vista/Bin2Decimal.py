class Conversor:

    def __init__(self):
        self.n = 0
        self.N = 0

    def decimalToBinary(self):
        binarylist = []
        decimal = self.n
        while decimal >= 1:
            remainder = decimal
            decimal = decimal // 2
            binarylist.append(remainder % 2)
        binarylist = map(str, list(reversed(binarylist)))
        binarylist2show = ''.join(binarylist)
        print(binarylist2show)

    def binaryToDecimal(self):
        numeroDecimal, position = 0, 0
        binary = self.N
        while (binary != 0):
            cifra = binary % 10
            numeroDecimal = (pow(2, position) * cifra) + numeroDecimal
            binary = binary // 10
            position += 1
        print(numeroDecimal)
