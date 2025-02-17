from sympy import isprime

bilangan_yg_dicek = int(input("Masukkan angka yang ingin dicek: "))
if isprime(bilangan_yg_dicek):
    print(f"{bilangan_yg_dicek} adalah bilangan prima")
else:
    print(print(f"{bilangan_yg_dicek} bukan bilangan prima"))