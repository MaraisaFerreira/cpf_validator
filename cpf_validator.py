cpf = input('Digite um CPF: ')

while len(cpf) != 11 or not cpf.isdigit():
    print(len(cpf))
    print('O cpf deve conter apenas 11 digitos.\nApenas números de 0 a 9, sem pontos ou traços.\n')
    cpf = input('Digite um CPF: ')


if cpf[0] * 11 == cpf:
    print("CPF inválido.")
else:
    cpf_base = cpf[:-2]

    reverse = 10
    total = 0

    for i in range(19):
        if i > 8:
            i -= 9

        total += int(cpf_base[i]) * reverse

        reverse -= 1
        if reverse < 2:
            digit = 11 - total % 11

            if digit > 9:
                digit = 0

            cpf_base += str(digit)
            reverse = 11
            total = 0

    print('CPF Válido' if cpf == cpf_base else 'CPF inválido')





