
TEMA1 = {
    "nombre": "Tema 1 - Formas bilineales y formas cuadraticas",

    "resumen": """
Este tema estudia formas bilineales y formas cuadraticas en espacios vectoriales reales.

1. Forma bilineal
Una forma bilineal es una aplicacion f: V x V -> K que es lineal en cada variable por separado.
Eso significa que, si fijas y, la aplicacion x -> f(x,y) es lineal; y si fijas x, la aplicacion
y -> f(x,y) tambien es lineal.

2. Matriz asociada de una forma bilineal
Si B = {b1, b2, ..., bn} es una base de V, la matriz asociada a f en la base B tiene entradas:

m_ij = f(b_i, b_j)

Si x e y son vectores, entonces:

f(x,y) = (x_B)^t * M_B^f * (y_B)

3. Cambio de base en formas bilineales
Si A es la matriz de una forma bilineal en una base y B es la matriz en otra base, el cambio
se hace por congruencia:

B = P^t * A * P

donde P es la matriz cuyas columnas son los vectores de la nueva base expresados en la base antigua.

Importante:
Para endomorfismos aparece semejanza: B = P^(-1) A P.
Para formas bilineales/cuadraticas aparece congruencia: B = P^t A P.

4. Parte simetrica y parte antisimetrica
Cualquier matriz A se puede descomponer de forma unica como:

A = A_s + A_a

donde:

A_s = (A + A^t)/2
A_a = (A - A^t)/2

A_s es simetrica y A_a es antisimetrica.

5. Forma cuadratica asociada
A partir de una forma bilineal f se puede construir una forma cuadratica:

phi(x) = f(x,x)

La parte antisimetrica no aporta nada a phi, porque x^t A_a x = 0.
Por eso, la forma cuadratica esta determinada por la parte simetrica.

6. Forma polar
La forma polar asociada a una forma cuadratica phi es una forma bilineal simetrica.
En caracteristica distinta de 2, se puede obtener con:

f_p(x,y) = 1/2 [phi(x+y) - phi(x) - phi(y)]

Si M es la matriz simetrica de phi, entonces:

f_p(x,y) = x^t M y

7. Nucleo de una forma cuadratica
El nucleo de una forma cuadratica se define como:

Nuc(phi) = {x en V / f_p(x,y) = 0 para todo y en V}

En coordenadas, si M es la matriz de la forma polar, se resuelve:

M x = 0

Por tanto:

dim Nuc(phi) = n - rango(M)

8. Rango
El rango de la forma cuadratica es el rango de su matriz simetrica asociada:

rg(phi) = rg(M)

Si rg(M) = n, la forma es no degenerada u ordinaria.
Si rg(M) < n, la forma es degenerada.

9. Vectores conjugados
Dos vectores x e y son conjugados si:

f_p(x,y) = 0

Una base es conjugada si todos sus vectores distintos son conjugados dos a dos.
En una base conjugada, la matriz de la forma cuadratica queda diagonal.

10. Diagonalizacion por congruencia
Diagonalizar una forma cuadratica significa encontrar una base donde su matriz sea diagonal.
Se hacen operaciones simultaneas de filas y columnas, manteniendo la congruencia:

D = P^t M P

No es diagonalizacion por semejanza. No se usa P^(-1) M P, sino P^t M P.

11. Signatura
Para formas cuadraticas reales, una vez diagonalizada la matriz, la signatura es:

sg(phi) = (p, q)

donde:
- p es el numero de coeficientes positivos en la diagonal.
- q es el numero de coeficientes negativos en la diagonal.

Los ceros corresponden al nucleo.

12. Clasificacion
Si p = n y q = 0: definida positiva.
Si p = 0 y q = n: definida negativa.
Si p > 0, q = 0 y hay ceros: semidefinida positiva.
Si p = 0, q > 0 y hay ceros: semidefinida negativa.
Si p > 0 y q > 0: indefinida.

Si no hay ceros, la forma es no degenerada.
Si hay ceros, la forma es degenerada.

13. Criterio de Sylvester
Para una matriz simetrica real, el criterio de Sylvester ayuda a clasificar:
- Definida positiva si todos los menores principales lideres son positivos.
- Definida negativa si los signos alternan: Delta1 < 0, Delta2 > 0, Delta3 < 0, ...
- Si los menores no permiten concluir directamente, se suele diagonalizar por congruencia.
""",

    "formulas": [
        {
            "nombre": "Matriz asociada a una forma bilineal",
            "formula": "m_ij = f(b_i, b_j)",
            "uso": "Construir la matriz de una forma bilineal en una base.",
            "cuando_usarla": [
                "Cuando te dan f(x,y) y una base.",
                "Cuando te piden M_B^f.",
                "Cuando los vectores de la base no son la base usual."
            ],
            "detalles": [
                "La fila i y columna j contiene f(b_i,b_j).",
                "Si la base es usual, normalmente se lee directamente de los coeficientes de x_i y_j."
            ]
        },
        {
            "nombre": "Expresion matricial de una forma bilineal",
            "formula": "f(x,y) = x_B^t * M_B^f * y_B",
            "uso": "Calcular f(x,y) usando coordenadas y matriz.",
            "cuando_usarla": [
                "Cuando ya tienes la matriz asociada.",
                "Cuando x e y estan dados en una base concreta."
            ],
            "detalles": [
                "Cuidado: x e y deben estar expresados en la misma base que la matriz."
            ]
        },
        {
            "nombre": "Cambio de base por congruencia",
            "formula": "M_B' = P^t * M_B * P",
            "uso": "Cambiar la matriz de una forma bilineal o cuadratica a otra base.",
            "cuando_usarla": [
                "Cuando cambias la base de una forma bilineal.",
                "Cuando estas diagonalizando una forma cuadratica.",
                "Cuando aparece una matriz simetrica y una base nueva."
            ],
            "detalles": [
                "P tiene como columnas los vectores de la nueva base expresados en la base antigua.",
                "No es semejanza. No uses P^(-1)MP para formas bilineales."
            ]
        },
        {
            "nombre": "Parte simetrica",
            "formula": "A_s = (A + A^t)/2",
            "uso": "Obtener la parte simetrica de una forma bilineal.",
            "cuando_usarla": [
                "Cuando una forma bilineal no es simetrica.",
                "Cuando necesitas la forma cuadratica asociada."
            ],
            "detalles": [
                "La forma cuadratica asociada depende solo de A_s."
            ]
        },
        {
            "nombre": "Parte antisimetrica",
            "formula": "A_a = (A - A^t)/2",
            "uso": "Obtener la parte antisimetrica de una forma bilineal.",
            "cuando_usarla": [
                "Cuando tienes que descomponer A como A_s + A_a.",
                "Cuando te piden parte simetrica y antisimetrica."
            ],
            "detalles": [
                "La parte antisimetrica no define forma cuadratica porque x^t A_a x = 0."
            ]
        },
        {
            "nombre": "Forma cuadratica asociada",
            "formula": "phi(x) = f(x,x) = x^t M_s x",
            "uso": "Obtener la forma cuadratica a partir de una forma bilineal.",
            "cuando_usarla": [
                "Cuando te piden phi asociada a f.",
                "Cuando quieres clasificar una forma cuadratica."
            ],
            "detalles": [
                "Si A no es simetrica, usa su parte simetrica A_s."
            ]
        },
        {
            "nombre": "Forma polar",
            "formula": "f_p(x,y) = 1/2 [phi(x+y) - phi(x) - phi(y)]",
            "uso": "Recuperar la forma bilineal simetrica asociada a una forma cuadratica.",
            "cuando_usarla": [
                "Cuando te dan phi y te piden la forma polar.",
                "Cuando necesitas calcular nucleos o conjugados."
            ],
            "detalles": [
                "Si M es simetrica, entonces f_p(x,y) = x^t M y."
            ]
        },
        {
            "nombre": "Nucleo de una forma cuadratica",
            "formula": "Nuc(phi) = {x / Mx = 0}",
            "uso": "Calcular el nucleo usando la matriz de la forma polar.",
            "cuando_usarla": [
                "Cuando te piden dimension del nucleo.",
                "Cuando te piden ecuaciones parametricas o cartesianas."
            ],
            "detalles": [
                "dim Nuc(phi) = n - rg(M)."
            ]
        },
        {
            "nombre": "Rango de una forma cuadratica",
            "formula": "rg(phi) = rg(M)",
            "uso": "Determinar si la forma es degenerada o no degenerada.",
            "cuando_usarla": [
                "Cuando clasificas una forma cuadratica.",
                "Cuando estudias si tiene nucleo no trivial."
            ],
            "detalles": [
                "Si rg(M) = n, es no degenerada.",
                "Si rg(M) < n, es degenerada."
            ]
        },
        {
            "nombre": "Signatura",
            "formula": "sg(phi) = (p, q)",
            "uso": "Clasificar formas cuadraticas reales.",
            "cuando_usarla": [
                "Despues de diagonalizar por congruencia.",
                "Cuando cuentas positivos y negativos en la diagonal."
            ],
            "detalles": [
                "p = numero de positivos.",
                "q = numero de negativos.",
                "Los ceros indican degeneracion."
            ]
        },
        {
            "nombre": "Criterio de Sylvester",
            "formula": "Delta_k = det(menor principal lider de orden k)",
            "uso": "Clasificar definidas positivas o negativas mediante menores principales.",
            "cuando_usarla": [
                "Cuando la matriz es simetrica real.",
                "Cuando te piden clasificar sin diagonalizar totalmente."
            ],
            "detalles": [
                "Definida positiva si todos los Delta_k son positivos.",
                "Definida negativa si los signos alternan empezando por negativo."
            ]
        }
    ],

    "metodos": [
        {
            "nombre": "Construir la matriz asociada en una base",
            "objetivo": "Pasar de una expresion f(x,y) a una matriz M_B^f.",
            "pasos": [
                "Identifica la base B = {b1, b2, ..., bn}.",
                "Calcula cada entrada m_ij = f(b_i, b_j).",
                "Coloca cada resultado en la fila i y columna j.",
                "Si estas en base usual, lee el coeficiente de x_i*y_j.",
                "Comprueba si la matriz es simetrica: A = A^t."
            ],
            "errores_comunes": [
                "Confundir m_ij con f(b_j,b_i).",
                "Olvidar que en formas bilineales el orden importa si no es simetrica."
            ]
        },
        {
            "nombre": "Cambiar de base una forma bilineal o cuadratica",
            "objetivo": "Obtener la matriz en una nueva base usando congruencia.",
            "pasos": [
                "Construye P con las columnas de la nueva base escritas en la base antigua.",
                "Calcula P^t.",
                "Multiplica M_nueva = P^t * M_antigua * P.",
                "Comprueba dimensiones.",
                "Si M era simetrica, M_nueva tambien debe ser simetrica."
            ],
            "errores_comunes": [
                "Usar P^(-1)MP en vez de P^tMP.",
                "Poner las bases como filas en vez de columnas."
            ]
        },
        {
            "nombre": "Separar parte simetrica y antisimetrica",
            "objetivo": "Escribir A = A_s + A_a.",
            "pasos": [
                "Calcula A^t.",
                "Calcula A_s = (A + A^t)/2.",
                "Calcula A_a = (A - A^t)/2.",
                "Verifica que A_s^t = A_s.",
                "Verifica que A_a^t = -A_a."
            ],
            "errores_comunes": [
                "Pensar que la parte antisimetrica contribuye a la forma cuadratica.",
                "Olvidar dividir entre 2."
            ]
        },
        {
            "nombre": "Obtener la forma cuadratica asociada",
            "objetivo": "Pasar de f(x,y) a phi(x)=f(x,x).",
            "pasos": [
                "Sustituye y = x en la forma bilineal.",
                "Simplifica terminos.",
                "Si trabajas con matriz, usa phi(x) = x^t A_s x.",
                "Recuerda que los terminos cruzados aparecen duplicados en matriz simetrica."
            ],
            "errores_comunes": [
                "Usar A completa no simetrica sin mirar la parte simetrica.",
                "Poner coeficientes cruzados incorrectos: el coeficiente de xy se reparte como m12=m21=coef/2."
            ]
        },
        {
            "nombre": "Calcular el nucleo de una forma cuadratica",
            "objetivo": "Encontrar los vectores conjugados a todo el espacio.",
            "pasos": [
                "Toma la matriz simetrica M de la forma polar.",
                "Resuelve el sistema homogeneo Mx = 0.",
                "Obtiene una base del conjunto solucion.",
                "La dimension es n - rango(M).",
                "Expresa el resultado en la base que te pidan."
            ],
            "errores_comunes": [
                "Resolver phi(x)=0 en vez de Mx=0.",
                "Olvidar cambiar los vectores a base usual si el problema lo pide."
            ]
        },
        {
            "nombre": "Diagonalizar por congruencia",
            "objetivo": "Encontrar una base conjugada donde la matriz sea diagonal.",
            "pasos": [
                "Parte de una matriz simetrica.",
                "Realiza operaciones simultaneas de filas y columnas.",
                "Guarda las mismas operaciones en la matriz identidad para obtener P.",
                "Obtiene D = P^t M P.",
                "Cuenta signos de la diagonal para la signatura.",
                "Clasifica la forma cuadratica."
            ],
            "errores_comunes": [
                "Hacer solo operaciones por filas.",
                "Confundir diagonalizacion por congruencia con diagonalizacion por autovalores."
            ]
        },
        {
            "nombre": "Clasificar una forma cuadratica",
            "objetivo": "Decidir si es definida, semidefinida, indefinida, degenerada o no degenerada.",
            "pasos": [
                "Diagonaliza por congruencia o aplica Sylvester si procede.",
                "Cuenta coeficientes positivos p y negativos q.",
                "Cuenta ceros en la diagonal.",
                "Si hay positivos y negativos, es indefinida.",
                "Si solo hay positivos y ningun cero, definida positiva.",
                "Si solo hay negativos y ningun cero, definida negativa.",
                "Si hay ceros y solo positivos, semidefinida positiva.",
                "Si hay ceros y solo negativos, semidefinida negativa.",
                "Si hay ceros, es degenerada."
            ],
            "errores_comunes": [
                "Decir que una forma con ceros es definida.",
                "Olvidar indicar rango y signatura."
            ]
        }
    ],

    "flashcards": [
        {
            "id": "alg1_fc_01",
            "frente": "¿Que significa que una forma sea bilineal?",
            "reverso": "Que es lineal en cada variable por separado.",
            "categoria": "Formas bilineales"
        },
        {
            "id": "alg1_fc_02",
            "frente": "¿Como se calcula la entrada m_ij de la matriz asociada?",
            "reverso": "m_ij = f(b_i, b_j).",
            "categoria": "Matriz asociada"
        },
        {
            "id": "alg1_fc_03",
            "frente": "¿Que formula de cambio de base se usa para formas bilineales?",
            "reverso": "M_B' = P^t M_B P.",
            "categoria": "Cambio de base"
        },
        {
            "id": "alg1_fc_04",
            "frente": "¿Es cambio por semejanza o por congruencia?",
            "reverso": "Por congruencia.",
            "categoria": "Cambio de base"
        },
        {
            "id": "alg1_fc_05",
            "frente": "¿Que parte de una forma bilineal define la forma cuadratica asociada?",
            "reverso": "La parte simetrica.",
            "categoria": "Forma cuadratica"
        },
        {
            "id": "alg1_fc_06",
            "frente": "¿Que aporta la parte antisimetrica a phi(x)=f(x,x)?",
            "reverso": "Nada, porque x^t A_a x = 0.",
            "categoria": "Parte antisimetrica"
        },
        {
            "id": "alg1_fc_07",
            "frente": "¿Como se calcula el nucleo de una forma cuadratica?",
            "reverso": "Resolviendo Mx = 0, donde M es la matriz simetrica de la forma polar.",
            "categoria": "Nucleo"
        },
        {
            "id": "alg1_fc_08",
            "frente": "¿Cuando una forma cuadratica es degenerada?",
            "reverso": "Cuando el rango de su matriz es menor que la dimension del espacio.",
            "categoria": "Clasificacion"
        },
        {
            "id": "alg1_fc_09",
            "frente": "¿Que es la signatura sg(phi)=(p,q)?",
            "reverso": "p es el numero de positivos y q el numero de negativos en la diagonal.",
            "categoria": "Signatura"
        },
        {
            "id": "alg1_fc_10",
            "frente": "¿Que significa que dos vectores sean conjugados?",
            "reverso": "Que f_p(x,y)=0.",
            "categoria": "Conjugacion"
        },
        {
            "id": "alg1_fc_11",
            "frente": "¿Cuando la matriz de una forma cuadratica queda diagonal en una base?",
            "reverso": "Cuando los vectores de esa base son conjugados dos a dos.",
            "categoria": "Diagonalizacion"
        },
        {
            "id": "alg1_fc_12",
            "frente": "¿Que formula da la forma polar a partir de phi?",
            "reverso": "f_p(x,y)=1/2[phi(x+y)-phi(x)-phi(y)].",
            "categoria": "Forma polar"
        }
    ],

    "preguntas_vf": [
        {
            "id": "alg1_vf_01",
            "pregunta": "Una forma bilineal debe ser lineal en las dos variables a la vez, pero no necesariamente por separado.",
            "respuesta": False,
            "explicacion": "Debe ser lineal en cada variable por separado.",
            "categoria": "Formas bilineales",
            "dificultad": "facil"
        },
        {
            "id": "alg1_vf_02",
            "pregunta": "La matriz asociada a una forma bilineal tiene entradas m_ij = f(b_i,b_j).",
            "respuesta": True,
            "explicacion": "Esa es la definicion de matriz asociada en una base.",
            "categoria": "Matriz asociada",
            "dificultad": "facil"
        },
        {
            "id": "alg1_vf_03",
            "pregunta": "El cambio de base de una forma bilineal se hace con P^(-1)AP.",
            "respuesta": False,
            "explicacion": "Eso es semejanza. Para formas bilineales se usa P^tAP.",
            "categoria": "Cambio de base",
            "dificultad": "media"
        },
        {
            "id": "alg1_vf_04",
            "pregunta": "Si A es simetrica, entonces P^tAP tambien es simetrica.",
            "respuesta": True,
            "explicacion": "La congruencia conserva la simetria.",
            "categoria": "Cambio de base",
            "dificultad": "media"
        },
        {
            "id": "alg1_vf_05",
            "pregunta": "La parte antisimetrica de una forma bilineal contribuye a phi(x)=f(x,x).",
            "respuesta": False,
            "explicacion": "Para una matriz antisimetrica A_a se cumple x^t A_a x = 0.",
            "categoria": "Parte antisimetrica",
            "dificultad": "media"
        },
        {
            "id": "alg1_vf_06",
            "pregunta": "La forma cuadratica asociada a una forma bilineal depende solo de la parte simetrica.",
            "respuesta": True,
            "explicacion": "La parte antisimetrica se anula en x^t A x.",
            "categoria": "Forma cuadratica",
            "dificultad": "facil"
        },
        {
            "id": "alg1_vf_07",
            "pregunta": "Para hallar el nucleo de una forma cuadratica basta resolver phi(x)=0.",
            "respuesta": False,
            "explicacion": "El nucleo se obtiene resolviendo Mx=0, no solo phi(x)=0.",
            "categoria": "Nucleo",
            "dificultad": "dificil"
        },
        {
            "id": "alg1_vf_08",
            "pregunta": "Si rg(M)=n, la forma cuadratica es no degenerada.",
            "respuesta": True,
            "explicacion": "Rango completo implica nucleo trivial.",
            "categoria": "Clasificacion",
            "dificultad": "facil"
        },
        {
            "id": "alg1_vf_09",
            "pregunta": "Una forma con positivos y negativos en su diagonal es indefinida.",
            "respuesta": True,
            "explicacion": "Si toma valores positivos y negativos, es indefinida.",
            "categoria": "Clasificacion",
            "dificultad": "facil"
        },
        {
            "id": "alg1_vf_10",
            "pregunta": "Una forma semidefinida positiva no puede ser degenerada.",
            "respuesta": False,
            "explicacion": "Si es semidefinida positiva tiene ceros no triviales, por tanto suele ser degenerada.",
            "categoria": "Clasificacion",
            "dificultad": "media"
        },
        {
            "id": "alg1_vf_11",
            "pregunta": "Una base conjugada diagonaliza la matriz de una forma cuadratica.",
            "respuesta": True,
            "explicacion": "Los terminos fuera de la diagonal son f_p(b_i,b_j), que se anulan.",
            "categoria": "Diagonalizacion",
            "dificultad": "media"
        },
        {
            "id": "alg1_vf_12",
            "pregunta": "La signatura depende de la base elegida.",
            "respuesta": False,
            "explicacion": "Por la ley de inercia de Sylvester, la signatura es invariante.",
            "categoria": "Signatura",
            "dificultad": "dificil"
        }
    ],

    "preguntas_mc": [
        {
            "id": "alg1_mc_01",
            "pregunta": "¿Como se calcula la matriz asociada a una forma bilineal en una base B?",
            "opciones": [
                "m_ij = f(b_i,b_j)",
                "m_ij = f(b_i+b_j)",
                "m_ij = det(b_i,b_j)",
                "m_ij = b_i*b_j"
            ],
            "respuesta": 1,
            "explicacion": "Por definicion, m_ij = f(b_i,b_j).",
            "categoria": "Matriz asociada",
            "dificultad": "facil"
        },
        {
            "id": "alg1_mc_02",
            "pregunta": "¿Que formula se usa para cambiar de base una forma bilineal?",
            "opciones": [
                "B = P^(-1) A P",
                "B = P A P^(-1)",
                "B = P^t A P",
                "B = A^t P A"
            ],
            "respuesta": 3,
            "explicacion": "El cambio es por congruencia: B = P^t A P.",
            "categoria": "Cambio de base",
            "dificultad": "facil"
        },
        {
            "id": "alg1_mc_03",
            "pregunta": "¿Que formula da la parte simetrica de una matriz A?",
            "opciones": [
                "(A - A^t)/2",
                "(A + A^t)/2",
                "A^t A",
                "A^(-1)"
            ],
            "respuesta": 2,
            "explicacion": "La parte simetrica es A_s = (A + A^t)/2.",
            "categoria": "Parte simetrica",
            "dificultad": "facil"
        },
        {
            "id": "alg1_mc_04",
            "pregunta": "¿Que formula da la parte antisimetrica?",
            "opciones": [
                "(A - A^t)/2",
                "(A + A^t)/2",
                "A + I",
                "P^t A P"
            ],
            "respuesta": 1,
            "explicacion": "La parte antisimetrica es A_a = (A - A^t)/2.",
            "categoria": "Parte antisimetrica",
            "dificultad": "facil"
        },
        {
            "id": "alg1_mc_05",
            "pregunta": "¿Como se obtiene la forma cuadratica asociada a f?",
            "opciones": [
                "phi(x)=f(x,0)",
                "phi(x)=f(x,x)",
                "phi(x)=f(0,x)",
                "phi(x)=det(f)"
            ],
            "respuesta": 2,
            "explicacion": "La forma cuadratica asociada es phi(x)=f(x,x).",
            "categoria": "Forma cuadratica",
            "dificultad": "facil"
        },
        {
            "id": "alg1_mc_06",
            "pregunta": "¿Como se calcula el nucleo de una forma cuadratica con matriz M?",
            "opciones": [
                "Resolviendo det(M)=0",
                "Resolviendo Mx=0",
                "Resolviendo phi(x)=1",
                "Calculando P^(-1)MP"
            ],
            "respuesta": 2,
            "explicacion": "El nucleo es el conjunto de soluciones de Mx=0.",
            "categoria": "Nucleo",
            "dificultad": "media"
        },
        {
            "id": "alg1_mc_07",
            "pregunta": "Si una diagonal tiene signos (+,+,-), ¿cual es la signatura?",
            "opciones": [
                "(3,0)",
                "(2,1)",
                "(1,2)",
                "(0,3)"
            ],
            "respuesta": 2,
            "explicacion": "Hay 2 positivos y 1 negativo.",
            "categoria": "Signatura",
            "dificultad": "facil"
        },
        {
            "id": "alg1_mc_08",
            "pregunta": "Si una forma tiene signatura (2,1), ¿como se clasifica?",
            "opciones": [
                "Definida positiva",
                "Definida negativa",
                "Indefinida",
                "Semidefinida positiva"
            ],
            "respuesta": 3,
            "explicacion": "Tiene positivos y negativos, por tanto es indefinida.",
            "categoria": "Clasificacion",
            "dificultad": "facil"
        },
        {
            "id": "alg1_mc_09",
            "pregunta": "Si una forma en R3 tiene rango 2, ¿cuanto vale la dimension del nucleo?",
            "opciones": [
                "0",
                "1",
                "2",
                "3"
            ],
            "respuesta": 2,
            "explicacion": "dim Nuc = n - rango = 3 - 2 = 1.",
            "categoria": "Nucleo",
            "dificultad": "media"
        },
        {
            "id": "alg1_mc_10",
            "pregunta": "¿Que significa que dos vectores sean conjugados respecto de phi?",
            "opciones": [
                "Que son iguales",
                "Que f_p(x,y)=0",
                "Que tienen la misma norma",
                "Que son linealmente dependientes"
            ],
            "respuesta": 2,
            "explicacion": "La conjugacion se define por f_p(x,y)=0.",
            "categoria": "Conjugacion",
            "dificultad": "media"
        },
        {
            "id": "alg1_mc_11",
            "pregunta": "¿Que tipo de cambio aparece en diagonalizacion de formas cuadraticas?",
            "opciones": [
                "Semejanza",
                "Congruencia",
                "Traslacion",
                "Rotacion solamente"
            ],
            "respuesta": 2,
            "explicacion": "Se diagonaliza por congruencia.",
            "categoria": "Diagonalizacion",
            "dificultad": "media"
        },
        {
            "id": "alg1_mc_12",
            "pregunta": "¿Que condicion de Sylvester da definida positiva?",
            "opciones": [
                "Todos los menores principales lideres positivos",
                "Todos los menores principales lideres negativos",
                "Determinante cero",
                "Trazas negativas"
            ],
            "respuesta": 1,
            "explicacion": "Para definida positiva, Delta1, Delta2, ..., Deltan deben ser positivos.",
            "categoria": "Sylvester",
            "dificultad": "dificil"
        }
    ],

    "ejercicios_guiados": [
        {
            "id": "alg1_ej_01",
            "enunciado": "Dada f(x,y)=3x1y1 - x1y2 + 5x2y1 + 2x2y2 en R2, halla la matriz asociada en la base usual.",
            "categoria": "Matriz asociada",
            "dificultad": "facil",
            "solucion": [
                "Identificamos los coeficientes de x_i*y_j.",
                "Coeficiente de x1*y1: 3, entonces m11=3.",
                "Coeficiente de x1*y2: -1, entonces m12=-1.",
                "Coeficiente de x2*y1: 5, entonces m21=5.",
                "Coeficiente de x2*y2: 2, entonces m22=2.",
                "La matriz es [[3,-1],[5,2]]."
            ]
        },
        {
            "id": "alg1_ej_02",
            "enunciado": "Para A=[[3,-1],[5,2]], calcula la parte simetrica y antisimetrica.",
            "categoria": "Parte simetrica",
            "dificultad": "media",
            "solucion": [
                "Calculamos A^t = [[3,5],[-1,2]].",
                "A_s = (A+A^t)/2 = [[3,2],[2,2]].",
                "A_a = (A-A^t)/2 = [[0,-3],[3,0]].",
                "Comprobacion: A_s es simetrica y A_a es antisimetrica.",
                "La forma cuadratica asociada depende solo de A_s."
            ]
        },
        {
            "id": "alg1_ej_03",
            "enunciado": "Dada phi(x,y)=2x^2+3xy+6y^2, halla su matriz simetrica asociada.",
            "categoria": "Forma cuadratica",
            "dificultad": "facil",
            "solucion": [
                "Los terminos cuadrados van directamente en la diagonal.",
                "m11=2 y m22=6.",
                "El termino cruzado 3xy se reparte entre m12 y m21.",
                "Como m12=m21, tenemos 2*m12=3, luego m12=3/2.",
                "La matriz es [[2,3/2],[3/2,6]]."
            ]
        },
        {
            "id": "alg1_ej_04",
            "enunciado": "Si M=diag(1,1,-1), clasifica la forma cuadratica en R3.",
            "categoria": "Clasificacion",
            "dificultad": "facil",
            "solucion": [
                "La diagonal tiene dos positivos y un negativo.",
                "La signatura es (2,1).",
                "El rango es 3 porque no hay ceros en la diagonal.",
                "Como hay positivos y negativos, la forma es indefinida.",
                "Como el rango es 3 en R3, es no degenerada."
            ]
        },
        {
            "id": "alg1_ej_05",
            "enunciado": "Si M=diag(1,1,0), clasifica la forma cuadratica en R3.",
            "categoria": "Clasificacion",
            "dificultad": "media",
            "solucion": [
                "La diagonal tiene dos positivos, cero negativos y un cero.",
                "La signatura es (2,0).",
                "El rango es 2.",
                "La dimension del nucleo es 3-2=1.",
                "Como solo toma valores no negativos, es semidefinida positiva.",
                "Como tiene nucleo no trivial, es degenerada."
            ]
        },
        {
            "id": "alg1_ej_06",
            "enunciado": "Para una forma cuadratica en R3 con matriz M de rango 2, calcula la dimension del nucleo.",
            "categoria": "Nucleo",
            "dificultad": "facil",
            "solucion": [
                "Usamos dim Nuc(phi) = n - rg(M).",
                "Aqui n=3 y rg(M)=2.",
                "Entonces dim Nuc(phi)=3-2=1."
            ]
        },
        {
            "id": "alg1_ej_07",
            "enunciado": "Explica por que una base conjugada diagonaliza una forma cuadratica.",
            "categoria": "Diagonalizacion",
            "dificultad": "media",
            "solucion": [
                "La entrada m_ij de la matriz en esa base es f_p(b_i,b_j).",
                "Si la base es conjugada, entonces f_p(b_i,b_j)=0 para i diferente de j.",
                "Eso significa que todas las entradas fuera de la diagonal son cero.",
                "Por tanto, la matriz queda diagonal."
            ]
        },
        {
            "id": "alg1_ej_08",
            "enunciado": "Si B={b1,b2} y P tiene columnas b1,b2 en base usual, escribe la matriz de una forma bilineal en B.",
            "categoria": "Cambio de base",
            "dificultad": "media",
            "solucion": [
                "Sea A la matriz en base usual.",
                "Sea P la matriz de cambio con columnas b1 y b2.",
                "La matriz en la base B es M_B = P^t A P.",
                "Esto es congruencia, no semejanza.",
                "Si A es simetrica, M_B tambien sera simetrica."
            ]
        },
        {
            "id": "alg1_ej_09",
            "enunciado": "Si la diagonal obtenida por congruencia es diag(2,-3,0), indica rango, nucleo, signatura y clasificacion.",
            "categoria": "Signatura",
            "dificultad": "media",
            "solucion": [
                "Hay un positivo, un negativo y un cero.",
                "La signatura es (1,1).",
                "El rango es 2 porque hay dos elementos no nulos en la diagonal.",
                "En R3, dim Nuc = 3-2=1.",
                "Como hay positivo y negativo, la forma es indefinida.",
                "Como hay un cero, es degenerada."
            ]
        },
        {
            "id": "alg1_ej_10",
            "enunciado": "Usa Sylvester para decidir si A=[[2,0],[0,4]] es definida positiva.",
            "categoria": "Sylvester",
            "dificultad": "facil",
            "solucion": [
                "Calculamos los menores principales lideres.",
                "Delta1 = 2 > 0.",
                "Delta2 = det(A) = 2*4 - 0 = 8 > 0.",
                "Todos los menores principales lideres son positivos.",
                "Por Sylvester, la forma es definida positiva."
            ]
        }
    ]
}
