email = input(":").strip()


if ' ' in email:
    print('E-mail inválido')

elif email.count('@') != 1:
    print('E-mail inválido')
elif email.startswith('@') or email.endswith('@'):
    print('"E-mail inválido')
else:
    # Divide em parte local e domínio
    local, dominio = email.split('@')
    
    # Verifica se o domínio contém um ponto
    if '.' not in dominio:
        print('E-mail inválido')
    else:
        print('E-mail válido')