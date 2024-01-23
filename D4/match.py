cliente = {'nombre': 'Juan',
           'edad': 26,
           'ocupación': 'Ingeniero'}

pelicula = {'titulo': 'El Padrino',
            'ficha tecnica': {'protagonistas': 'Marlon Brando',
                              'director': 'Francis Ford Coppola'}}

elementos = [cliente, pelicula, 'Hola']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupación': ocupación}:
            print('Soy un cliente')
            print(f'Me llamo {nombre}, tengo {edad} años y soy {ocupación}')
        case {'titulo': titulo,
              'ficha tecnica': {'protagonistas': protagonistas,
                                'director': director}}:
            print('Soy una película')
            print(f'Me llamo {titulo} y mis protagonista es {protagonistas}')
        case _:
            print('Soy otra cosa')
