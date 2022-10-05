# NOTE: Desafio 3

# 0 - 600.00
# 600.01 - 900.00
# 900.01 - 1500.00
# 1500.01 - 2000.00
# Acima de 2000.00

# 17%
# 13%
# 12%
# 10%
# 5%


salario = int(input())


def trunc(value: float) -> str:
    value = str(value).split('.')
    return f'{value[0]},00'


if (salario <= 600.00):
    novo_salario = salario + salario * 0.17
    aumento = salario * 0.17
    print(
        f'Novo salario: {trunc(novo_salario)} Reajuste ganho: {trunc(aumento)}')
    print(f'Em percentual: 17 %')

elif (salario <= 900.00):
    novo_salario = salario + salario * 0.13
    aumento = salario * 0.13
    print(
        f'Novo salario: {trunc(novo_salario)} Reajuste ganho: {trunc(aumento)}')
    print(f'Em percentual: 13 %')

elif (salario <= 1500.00):
    novo_salario = salario + salario * 0.12
    aumento = salario * 0.12
    print(
        f'Novo salario: {trunc(novo_salario)} Reajuste ganho: {trunc(aumento)}')
    print(f'Em percentual: 12 %')

elif (salario <= 2000.00):
    novo_salario = salario + salario * 0.10
    aumento = salario * 0.10
    print(
        f'Novo salario: {trunc(novo_salario)} Reajuste ganho: {trunc(aumento)}')
    print(f'Em percentual: 10 %')

else:
    novo_salario = salario + salario * 0.05
    aumento = salario * 0.05
    print(
        f'Novo salario: {trunc(novo_salario)} Reajuste ganho: {trunc(aumento)}')
    print(f'Em percentual: 5 %')
