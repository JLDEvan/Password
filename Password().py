def password(senha):
    if len(senha) < 6:
        return('Minimo 6 caracteres')
    elif len(senha) > 12:
        return('Maximo 12 caracteres')
    elif not any(c.isupper() for c in senha): 
        return('Deve conter uma letra maiúscula')
    elif not any(c.islower() for c in senha): 
        return('Deve conter uma letra minúscula')
    elif not any(c.isdigit() for c in senha): 
        return('Deve conter um número')
    else:
        return('Sua senha é válida')

print(password(senha=''))