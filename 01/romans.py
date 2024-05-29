rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
real = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

def int_to_roman(num):
    resultado = ""

    for i in range(12, -1, -1):
        while num >= real[i]:
            num -= real[i]
            resultado += rom[i]

    return resultado

print(int_to_roman(1994))

def roman_to_int(s):
    
    resultado = 0
    for i in range(12, -1, -1):
        while s.startswith(rom[i]):
            resultado += real[i]
            s = s[len(rom[i]):]

    return resultado

print(roman_to_int('MXMCIV'))
