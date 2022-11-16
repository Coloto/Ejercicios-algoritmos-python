# Ejercicio 2

# • La nota del trimestre está basada en
# • Nota hito individual = 30 %
# • Nota hito grupal = 20 %
# • Nota examen = 50 %

# Datos de entrada
    # nota hito individual
    # nota hito grupal
    # nota examen
# Datos de salida
    # Nota total = Nota hito individual*30% + Nota hito grupal*20% + Nota examen*50%


# Identificadores
    # Nota hito individual (hito_individual)
    # Nota hito grupal (hito_grupal)
    # Nota examen (examen)

    # Nota total (total)
# Proceso

    # nota_hito_individual = nota_indv*30/100
    # nota_hito_grupal = nota_grup*20/100
    # nota_examen = nota_ex*50/100


    # total = nota_grup+nota_indv+nota_ex

# Python

def notas():
    nota_hito_individual=float(input('Nota sacada en el hito individual: '))
    nota_hito_grupal=float(input('Nota sacada en el hito grupal: '))
    nota_examen=float(input('Nota sacada en el examen: '))

    nota_indv=nota_hito_individual*0.3
    nota_grup=nota_hito_grupal*0.2
    nota_ex=nota_examen*0.5

    total=nota_indv+nota_grup+nota_ex
    print(f'En el trimestre has sacado un {total}')
# notas()



# Ejercicio 3

# • Se pide calcular la nota de tu examen tipo test.
# • Serán 20 preguntas
# • Las preguntas correctas sumarán 0,5
# • Las preguntas incorrectas restarán 0,25 
# • Las preguntas sin contestar tendrán 0 

# Datos de entrada
    # preguntas correctas
    # preguntas incorrectas
    # preguntas sin contestar
# Datos de salida
    # preguntas correctas * 0.5
    # preguntas incorrectas * 0.25
    # nota total

# Identificadores
    # preguntas correctas (correctas)
    # preguntas incorrectas (incorrectas)
    # preguntas sin contestar (enblanco)
    # nota total (total)

# Proceso
    # nota_correctas=correctas*0.5
    # nota_incorrectas=incorrectas*0.25
    # nota_enblanco=0
    # total=nota_correctas-nota_incorrectas

# Python

def test():
    correctas=int(input('Cuantas preguntas has acertado: '))
    incorrectas=int(input('Cuantas preguntas has fallado: '))

    enblanco=20-(correctas+incorrectas)

    nota_correctas=correctas*0.5
    nota_incorrectas=incorrectas*0.25

    total=nota_correctas-nota_incorrectas

    print(f'De 20 preguntas se han acertado {correctas}, se han fallado {incorrectas} y no se han contestado {enblanco}. La nota final es: {total}')
# test()



# Ejercicio 4

# Diseña un algoritmo y un diagrama de flujo para:
# • Con la base y la altura de un rectángulo, se nos pide calcular su perímetro y su área

# Datos de entrada
    # Medida base
    # Medida altura
# Datos de salida
    # 