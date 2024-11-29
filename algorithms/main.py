#1. Mamy do zapłacenia n złotych i dajemy banknot 100 zł.
#napisz funkcję num_nominals zwracającą minimalną liczbę nominałów (100-n), które sumują sie do reszty
def num_nominals(rest: int):
    result = 0
    nominals = [50,20,10,5,2,1]
    print(f"reszta = {rest} wynik = ", end="")
    while rest > 0:
        for nominal in nominals:
            if rest >= nominal:
                rest -= nominal
                break
        result += 1
    return result

print(num_nominals(76))
print(num_nominals(51))
print(num_nominals(38))
print(num_nominals(39))
print(num_nominals(40))
print(num_nominals(59))
print(num_nominals(20))
print(num_nominals(0))