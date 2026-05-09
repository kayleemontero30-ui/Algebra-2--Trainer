# -*- coding: utf-8 -*-

TEMA2 = {
    "nombre": "Tema 2 - Espacios vectoriales euclideos",

    "resumen": """
Este tema estudia espacios vectoriales euclideos, es decir, espacios vectoriales reales
en los que se ha definido un producto escalar. A partir del producto escalar aparecen
conceptos geometricos: longitud, angulo, distancia, ortogonalidad, proyeccion,
complemento ortogonal y bases ortogonales/ortonormales.

1. Producto escalar

Un producto escalar en un espacio vectorial real V es una aplicacion:

< , > : V x V -> R

que cumple:
- Simetria: <x,y> = <y,x>.
- Linealidad en la primera variable: <x1+x2,y> = <x1,y> + <x2,y>.
- Homogeneidad: <lambda*x,y> = lambda*<x,y>.
- Definida positiva: <x,x> >= 0 y <x,x> = 0 si y solo si x = 0.

Por eso un producto escalar es una forma bilineal simetrica definida positiva.

2. Matriz de Gram o matriz metrica

Si B = {e1, e2, ..., en} es una base de V, la matriz de Gram del producto escalar
en esa base es:

G_B = (g_ij), con g_ij = <e_i, e_j>

Entonces, si x_B e y_B son las coordenadas de x e y en la base B:

<x,y> = x_B^t * G_B * y_B

En R^n con el producto escalar usual y la base usual, G_B = I.
En M_n(R) con el producto escalar usual <A,B> = tr(A*B^t), la matriz de Gram en
la base usual tambien es I.
En R_2[x] con <p,q> = integral_0^1 p(x)q(x) dx, la matriz de Gram en la base
{1,x,x^2} no es la identidad.

3. Cambio de base de la matriz de Gram

Si G_B es la matriz de Gram en una base B y quieres la matriz en una base B',
usas congruencia:

G_B' = P^t * G_B * P

donde P tiene por columnas las coordenadas de los vectores de B' escritos en la base B.

Esto conecta con Tema 1: las matrices de formas bilineales y cuadraticas cambian
por congruencia, no por semejanza.

4. Espacio euclideo canonico

Un espacio vectorial euclideo es canonico cuando el producto escalar usual tiene matriz
identidad en la base usual. Por eso R^n y M_n(R) con sus productos escalares usuales
son canonicos. Sin embargo, R_2[x] con <p,q> = integral_0^1 p q no es canonico en
la base {1,x,x^2}, porque su matriz de Gram no es I.

5. Norma inducida por producto escalar

Todo producto escalar induce una norma:

||x|| = sqrt(<x,x>)

Esta norma mide la longitud del vector segun el producto escalar elegido. Si cambias
el producto escalar, puede cambiar la longitud.

Propiedades de la norma:
- ||x|| >= 0 y ||x|| = 0 si y solo si x = 0.
- ||lambda*x|| = |lambda| ||x||.
- ||x+y|| <= ||x|| + ||y||.
- ||x-y|| >= || ||x|| - ||y|| ||.

6. Cauchy-Schwarz

Para todo x,y en un espacio euclideo:

|<x,y>| <= ||x|| ||y||

Esta desigualdad justifica que el cociente <x,y>/(||x||||y||) esta entre -1 y 1,
por lo que se puede definir el angulo entre vectores.

7. Angulo y distancia

El angulo entre x e y se calcula con:

alpha = arccos( <x,y> / (||x|| ||y||) )

La distancia entre x e y es:

d(x,y) = ||x-y||

En R^n con producto escalar usual, esto da la distancia euclidea usual.

8. Ortogonalidad

Dos vectores son ortogonales si:

<x,y> = 0

Si el angulo existe y los vectores no son nulos, esto equivale a alpha = 90 grados.

9. Complemento ortogonal

Si U es un subespacio de V, el complemento ortogonal es:

U_perp = {y en V / <x,y> = 0 para todo x en U}

Si U = lin{u1, ..., ur}, basta imponer:

<u1,y> = 0
<u2,y> = 0
...
<ur,y> = 0

Es decir, se transforma en un sistema lineal homogeneo.

En dimension finita:

V = U suma_directa U_perp
dim(V) = dim(U) + dim(U_perp)

10. Proyeccion ortogonal

Todo vector x puede descomponerse de manera unica como:

x = p_U(x) + componente_perpendicular

donde p_U(x) pertenece a U y la componente perpendicular pertenece a U_perp.

Si U tiene una base ortogonal {u1,...,ur}, entonces:

p_U(x) = sum( <x,u_i>/||u_i||^2 * u_i )

Para proyectar sobre un solo vector u:

p_u(x) = <x,u>/||u||^2 * u

y la componente perpendicular es:

x - p_u(x)

11. Bases ortogonales y ortonormales

Una base es ortogonal si sus vectores son ortogonales dos a dos.
Una base es ortonormal si es ortogonal y todos sus vectores tienen norma 1.

Si una base es ortogonal, su matriz de Gram es diagonal.
Si una base es ortonormal, su matriz de Gram es la identidad.

12. Coordenadas en base ortogonal y coeficientes de Fourier

Si B = {e1,...,en} es una base ortogonal, entonces:

x = sum( <x,e_i>/||e_i||^2 * e_i )

Los coeficientes <x,e_i>/||e_i||^2 se llaman coeficientes de Fourier.

Si la base es ortonormal, se simplifica a:

x = sum( <x,e_i> * e_i )

13. Gram-Schmidt

Gram-Schmidt convierte una base cualquiera en una base ortogonal. Luego, dividiendo
cada vector por su norma, se obtiene una base ortonormal.

Para B = {b1,b2,b3}:

o1 = b1
o2 = b2 - (<b2,o1>/||o1||^2)*o1
o3 = b3 - (<b3,o1>/||o1||^2)*o1 - (<b3,o2>/||o2||^2)*o2

Despues:

e_i = o_i / ||o_i||

14. Matrices ortogonales

Una matriz Q es ortogonal si:

Q^t Q = I

equivalentemente:

Q^{-1} = Q^t

Sus columnas forman una base ortonormal del espacio usual.

15. Diagonalizacion ortogonal por semejanza

Si A es una matriz real y simetrica, se puede diagonalizar ortogonalmente:

D = Q^{-1} A Q = Q^t A Q

donde Q es ortogonal y sus columnas son autovectores ortonormales de A.

Esto NO es lo mismo que diagonalizar una forma cuadratica por congruencia, aunque
en matrices simetricas aparecen juntas muchas veces:
- Endomorfismo/matriz lineal: semejanza, D = P^{-1} A P.
- Forma bilineal/cuadratica/producto escalar: congruencia, G' = P^t G P.

16. Recordatorio de Algebra I usado aqui

Para subespacios:
- Si te dan generadores, haces una matriz con esos vectores y reduces para obtener base y dimension.
- Si te dan ecuaciones cartesianas, resuelves el sistema homogeneo para obtener parametricas y base.
- Si te dan parametricas, los vectores que multiplican los parametros generan el subespacio.
- El nucleo de una matriz A es el conjunto de soluciones de Ax=0.
- La imagen de A es el subespacio generado por sus columnas.
- El rango es la dimension de la imagen.
""",

"formulas": [
        {
            "nombre": "Producto escalar mediante matriz de Gram",
            "formula": "<x,y> = x_B^t * G_B * y_B",
            "uso": "Calcular producto escalar cuando se conoce la matriz metrica en una base.",
            "cuando_usarla": [
                "Cuando el producto escalar no es el usual.",
                "Cuando te dan la matriz de Gram G_B.",
                "Cuando los vectores estan expresados en una base concreta."
            ],
            "detalles": [
                "x_B e y_B deben estar en la misma base que G_B.",
                "Si G_B = I, el producto escalar coincide con el usual en esa base."
            ]
        },
        {
            "nombre": "Matriz de Gram",
            "formula": "g_ij = <e_i, e_j>",
            "uso": "Construir la matriz metrica de un producto escalar en una base.",
            "cuando_usarla": [
                "Cuando te piden la matriz de Gram.",
                "Cuando tienes una base no usual.",
                "Cuando quieres comprobar si una base es ortogonal u ortonormal."
            ],
            "detalles": [
                "Si la base es ortogonal, G es diagonal.",
                "Si la base es ortonormal, G es la identidad."
            ]
        },
        {
            "nombre": "Cambio de base de la matriz de Gram",
            "formula": "G_Bprima = P^t * G_B * P",
            "uso": "Pasar la matriz de Gram de una base a otra.",
            "cuando_usarla": [
                "Cuando una base nueva esta escrita en la base antigua.",
                "Cuando te piden cambiar el producto escalar a otra base.",
                "Cuando trabajas con productos escalares no usuales."
            ],
            "detalles": [
                "P contiene como columnas los vectores de la base nueva escritos en la base antigua.",
                "Es congruencia, no semejanza."
            ]
        },
        {
            "nombre": "Norma inducida",
            "formula": "||x|| = sqrt(<x,x>)",
            "uso": "Calcular la longitud de un vector con respecto a un producto escalar.",
            "cuando_usarla": [
                "Cuando te dan un producto escalar.",
                "Cuando te piden longitud o modulo.",
                "Cuando necesitas normalizar un vector."
            ],
            "detalles": [
                "La norma depende del producto escalar elegido."
            ]
        },
        {
            "nombre": "Cauchy-Schwarz",
            "formula": "|<x,y>| <= ||x||*||y||",
            "uso": "Acotar el producto escalar y justificar la formula del angulo.",
            "cuando_usarla": [
                "Cuando te piden demostrar desigualdades.",
                "Cuando tienes que comprobar si un calculo de angulo tiene sentido.",
                "Cuando el ejercicio pide verificar Cauchy-Schwarz."
            ],
            "detalles": [
                "Si hay igualdad, normalmente los vectores son linealmente dependientes."
            ]
        },
        {
            "nombre": "Angulo entre dos vectores",
            "formula": "alpha = arccos(<x,y>/(||x||*||y||))",
            "uso": "Calcular el angulo entre dos vectores no nulos.",
            "cuando_usarla": [
                "Cuando te piden angulo.",
                "Cuando ya tienes producto escalar y normas.",
                "Cuando quieres comprobar ortogonalidad."
            ],
            "detalles": [
                "Si <x,y>=0, el angulo es 90 grados."
            ]
        },
        {
            "nombre": "Distancia inducida",
            "formula": "d(x,y) = ||x-y||",
            "uso": "Calcular la distancia entre dos vectores.",
            "cuando_usarla": [
                "Cuando te piden distancia o metrica.",
                "Cuando el producto escalar induce una norma.",
                "Cuando comparas distancia euclidea con otra metrica."
            ],
            "detalles": [
                "En R^n usual, d(x,y)=sqrt(sum((x_i-y_i)^2))."
            ]
        },
        {
            "nombre": "Ortogonalidad",
            "formula": "x perpendicular y <=> <x,y> = 0",
            "uso": "Comprobar si dos vectores son ortogonales.",
            "cuando_usarla": [
                "Cuando te piden base ortogonal.",
                "Cuando calculas complemento ortogonal.",
                "Cuando haces Gram-Schmidt."
            ],
            "detalles": [
                "La ortogonalidad depende del producto escalar."
            ]
        },
        {
            "nombre": "Complemento ortogonal de un subespacio",
            "formula": "U_perp = {y en V / <u,y>=0 para todo u en U}",
            "uso": "Encontrar todos los vectores ortogonales a un subespacio.",
            "cuando_usarla": [
                "Cuando te piden U_perp.",
                "Cuando debes descomponer V = U suma_directa U_perp.",
                "Cuando hay un subespacio dado por generadores."
            ],
            "detalles": [
                "Si U=lin{u1,...,ur}, basta imponer <u_i,y>=0 para todos los generadores.",
                "dim(V)=dim(U)+dim(U_perp)."
            ]
        },
        {
            "nombre": "Proyeccion sobre un vector",
            "formula": "p_u(x) = (<x,u>/||u||^2)*u",
            "uso": "Calcular la componente paralela de x sobre u.",
            "cuando_usarla": [
                "Cuando proyectas sobre una recta.",
                "Cuando te piden componente paralela y perpendicular.",
                "Cuando el subespacio tiene dimension 1."
            ],
            "detalles": [
                "La componente perpendicular es x - p_u(x)."
            ]
        },
        {
            "nombre": "Proyeccion sobre subespacio con base ortogonal",
            "formula": "p_U(x)=sum((<x,u_i>/||u_i||^2)*u_i)",
            "uso": "Proyectar un vector sobre un subespacio.",
            "cuando_usarla": [
                "Cuando U tiene base ortogonal.",
                "Cuando ya aplicaste Gram-Schmidt.",
                "Cuando quieres descomponer x en parte de U y parte de U_perp."
            ],
            "detalles": [
                "Si la base es ortonormal, los denominadores valen 1."
            ]
        },
        {
            "nombre": "Coordenadas en base ortogonal",
            "formula": "coord_i = <x,e_i>/||e_i||^2",
            "uso": "Calcular coordenadas de x en una base ortogonal.",
            "cuando_usarla": [
                "Cuando la base es ortogonal pero no necesariamente ortonormal.",
                "Cuando te piden coeficientes de Fourier.",
                "Cuando quieres reconstruir x como combinacion de la base."
            ],
            "detalles": [
                "Si la base es ortonormal, coord_i = <x,e_i>."
            ]
        },
        {
            "nombre": "Gram-Schmidt",
            "formula": "o_k = b_k - sum((<b_k,o_i>/||o_i||^2)*o_i)",
            "uso": "Convertir una base cualquiera en base ortogonal.",
            "cuando_usarla": [
                "Cuando te piden base ortogonal u ortonormal.",
                "Cuando los vectores de una base no son ortogonales.",
                "Cuando trabajas con producto escalar usual o no usual."
            ],
            "detalles": [
                "Despues de obtener base ortogonal, normaliza dividiendo cada vector por su norma."
            ]
        },
        {
            "nombre": "Matriz ortogonal",
            "formula": "Q^t Q = I",
            "uso": "Comprobar si una matriz es ortogonal.",
            "cuando_usarla": [
                "Cuando las columnas forman una base ortonormal.",
                "Cuando aparece diagonalizacion ortogonal.",
                "Cuando te dicen Q^{-1}=Q^t."
            ],
            "detalles": [
                "Una matriz ortogonal conserva longitudes y angulos en el producto usual."
            ]
        },
        {
            "nombre": "Diagonalizacion ortogonal de matriz simetrica",
            "formula": "D = Q^t * A * Q",
            "uso": "Diagonalizar una matriz real simetrica por semejanza ortogonal.",
            "cuando_usarla": [
                "Cuando A es real y simetrica.",
                "Cuando te piden diagonalizar ortogonalmente por semejanza.",
                "Cuando Q debe ser ortogonal."
            ],
            "detalles": [
                "Las columnas de Q son autovectores ortonormales de A.",
                "D contiene los autovalores correspondientes."
            ]
        },
        {
            "nombre": "Producto vectorial en R3",
            "formula": "x cross y = (x2*y3-x3*y2, x3*y1-x1*y3, x1*y2-x2*y1)",
            "uso": "Obtener un vector perpendicular a dos vectores en R3 con producto usual.",
            "cuando_usarla": [
                "Cuando necesitas un vector normal a un plano.",
                "Cuando quieres completar una base ortogonal en R3.",
                "Cuando te piden producto vectorial."
            ],
            "detalles": [
                "Solo tiene sentido como producto vectorial usual en R3."
            ]
        }

    ], 

"metodos": [
        {
            "nombre": "Comprobar si una aplicacion es producto escalar",
            "objetivo": "Ver si una forma define un producto escalar.",
            "pasos": [
                "Comprueba que es bilineal.",
                "Construye su matriz G en una base.",
                "Comprueba que G es simetrica.",
                "Comprueba que es definida positiva.",
                "Para definida positiva puedes usar Sylvester: todos los menores principales lideres positivos.",
                "Si G es simetrica definida positiva, entonces define producto escalar.",
                "Si en la base usual G=I, es el producto escalar usual."
            ],
            "errores_comunes": [
                "Pensar que cualquier matriz simetrica sirve. Debe ser definida positiva.",
                "Confundir producto escalar con cualquier forma bilineal."
            ]
        },
        {
            "nombre": "Construir la matriz de Gram",
            "objetivo": "Obtener G_B de un producto escalar en una base B.",
            "pasos": [
                "Escribe la base B={e1,...,en}.",
                "Calcula g11=<e1,e1>, g12=<e1,e2>, etc.",
                "Coloca g_ij=<e_i,e_j> en la fila i, columna j.",
                "Comprueba que la matriz sea simetrica.",
                "Si salen ceros fuera de la diagonal, la base es ortogonal.",
                "Si ademas la diagonal es toda 1, la base es ortonormal."
            ],
            "errores_comunes": [
                "Usar coordenadas de una base distinta a la matriz de Gram.",
                "Olvidar que para polinomios hay que integrar."
            ]
        },
        {
            "nombre": "Calcular longitud, angulo y distancia",
            "objetivo": "Resolver ejercicios tipo modulo, angulo y metrica.",
            "pasos": [
                "Identifica el producto escalar usado.",
                "Calcula <x,y>.",
                "Calcula ||x||=sqrt(<x,x>) y ||y||=sqrt(<y,y>).",
                "Calcula alpha=arccos(<x,y>/(||x||||y||)).",
                "Calcula d(x,y)=||x-y||.",
                "Si piden normalizar, divide cada vector por su norma."
            ],
            "errores_comunes": [
                "Usar el producto usual cuando el ejercicio da una matriz distinta.",
                "Olvidar que el angulo solo se calcula con vectores no nulos."
            ]
        },
        {
            "nombre": "Calcular complemento ortogonal de un vector",
            "objetivo": "Encontrar x_perp para un vector o una recta generada por un vector.",
            "pasos": [
                "Sea u el vector dado y sea y=(variables).",
                "Impón <u,y>=0.",
                "Escribe la ecuacion cartesiana resultante.",
                "Resuelve la ecuacion para obtener parametricas.",
                "Extrae una base del conjunto solucion.",
                "Comprueba que dim(u_perp)=dim(V)-1 si u no es nulo."
            ],
            "errores_comunes": [
                "Resolver <y,y>=0 en vez de <u,y>=0.",
                "Olvidar usar el producto escalar correcto."
            ]
        },
        {
            "nombre": "Calcular complemento ortogonal de un subespacio",
            "objetivo": "Encontrar U_perp cuando U tiene varios generadores.",
            "pasos": [
                "Consigue una base de U. Si los generadores son dependientes, reduce primero.",
                "Escribe y=(variables).",
                "Impón <u1,y>=0, <u2,y>=0, ..., para una base de U.",
                "Forma un sistema lineal homogeneo.",
                "Resuelve el sistema para obtener ecuaciones parametricas.",
                "Extrae una base de U_perp.",
                "Comprueba dim(V)=dim(U)+dim(U_perp)."
            ],
            "errores_comunes": [
                "Usar todos los generadores sin revisar dependencia no es grave, pero puede dar sistema redundante.",
                "Confundir U+U_perp con union de subespacios."
            ]
        },
        {
            "nombre": "Proyectar un vector sobre una recta",
            "objetivo": "Calcular componente paralela y perpendicular.",
            "pasos": [
                "Identifica el vector x que se proyecta y el vector u que genera la recta.",
                "Calcula <x,u>.",
                "Calcula ||u||^2=<u,u>.",
                "Calcula p_u(x)=(<x,u>/||u||^2)u.",
                "Calcula la componente perpendicular: x-p_u(x).",
                "Comprueba que <x-p_u(x),u>=0."
            ],
            "errores_comunes": [
                "Dividir por ||u|| en vez de por ||u||^2.",
                "Proyectar u sobre x cuando piden x sobre u."
            ]
        },
        {
            "nombre": "Proyectar un vector sobre un subespacio",
            "objetivo": "Calcular p_U(x) para U de dimension mayor que 1.",
            "pasos": [
                "Obtén una base de U.",
                "Si la base no es ortogonal, aplica Gram-Schmidt.",
                "Usa p_U(x)=sum((<x,u_i>/||u_i||^2)u_i).",
                "Calcula la componente perpendicular: x-p_U(x).",
                "Comprueba que la componente perpendicular sea ortogonal a todos los vectores de la base de U."
            ],
            "errores_comunes": [
                "Aplicar directamente la formula con una base no ortogonal.",
                "Olvidar comprobar que p_U(x) pertenece a U."
            ]
        },
        {
            "nombre": "Aplicar Gram-Schmidt",
            "objetivo": "Convertir una base cualquiera en base ortogonal u ortonormal.",
            "pasos": [
                "Ordena los vectores de partida b1,b2,...,bn.",
                "Toma o1=b1.",
                "Calcula o2=b2-(<b2,o1>/||o1||^2)o1.",
                "Calcula o3=b3-(<b3,o1>/||o1||^2)o1-(<b3,o2>/||o2||^2)o2.",
                "Continua igual para mas vectores.",
                "Si piden base ortonormal, divide cada o_i por ||o_i||.",
                "Comprueba que los productos <o_i,o_j> sean cero si i distinto de j."
            ],
            "errores_comunes": [
                "Usar productos escalares usuales cuando el ejercicio da matriz G.",
                "Normalizar antes de terminar no esta mal, pero hay que ser consistente.",
                "No cambiar coordenadas si el producto escalar se dio en una base distinta."
            ]
        },
        {
            "nombre": "Pasar de generadores a base y dimension",
            "objetivo": "Recordatorio de Algebra I para subespacios.",
            "pasos": [
                "Coloca los generadores como columnas de una matriz.",
                "Reduce por Gauss.",
                "Las columnas pivote originales forman una base del subespacio generado.",
                "El numero de pivotes es la dimension.",
                "Si quieres ecuaciones cartesianas, plantea que un vector general sea combinacion de la base y elimina parametros."
            ],
            "errores_comunes": [
                "Tomar como base las columnas reducidas en vez de las columnas originales correspondientes.",
                "Confundir numero de generadores con dimension."
            ]
        },
        {
            "nombre": "Pasar de ecuaciones cartesianas a parametricas",
            "objetivo": "Obtener base de un subespacio dado por ecuaciones.",
            "pasos": [
                "Escribe el sistema homogeneo.",
                "Reduce la matriz de coeficientes.",
                "Identifica variables libres.",
                "Expresa las variables pivote en funcion de las libres.",
                "Escribe el vector solucion como combinacion lineal de parametros.",
                "Los vectores que multiplican los parametros forman una base."
            ],
            "errores_comunes": [
                "Olvidar que al ser subespacio el sistema debe ser homogeneo.",
                "Perder variables libres."
            ]
        },
        {
            "nombre": "Calcular nucleo, imagen y rango de una matriz",
            "objetivo": "Recordatorio esencial para ejercicios de subespacios.",
            "pasos": [
                "Nucleo: resuelve Ax=0.",
                "Imagen: toma el subespacio generado por las columnas de A.",
                "Rango: cuenta pivotes en la reducida.",
                "dim Nuc(A)=numero de variables - rango(A).",
                "dim Im(A)=rango(A)."
            ],
            "errores_comunes": [
                "Confundir filas con columnas para la imagen.",
                "Resolver Ax=b para nucleo. El nucleo siempre usa b=0."
            ]
        },
        {
            "nombre": "Diagonalizacion por semejanza",
            "objetivo": "Diagonalizar una matriz como endomorfismo.",
            "pasos": [
                "Calcula el polinomio caracteristico det(A-lambda I).",
                "Obtén los autovalores.",
                "Para cada autovalor, resuelve (A-lambda I)x=0.",
                "Forma una base de autovectores si hay suficientes.",
                "Construye P con autovectores como columnas.",
                "Calcula D=P^{-1}AP.",
                "Si A es simetrica real, puedes escoger autovectores ortonormales y usar Q^tAQ."
            ],
            "errores_comunes": [
                "Usar P^tAP para un endomorfismo general.",
                "Olvidar normalizar si piden diagonalizacion ortogonal."
            ]
        },
        {
            "nombre": "Diagonalizacion ortogonal de una matriz simetrica",
            "objetivo": "Resolver ejercicios tipo D=Q^tAQ con Q ortogonal.",
            "pasos": [
                "Comprueba que A es simetrica.",
                "Calcula autovalores.",
                "Calcula una base de cada autoespacio.",
                "Si un autoespacio tiene dimension mayor que 1, ortogonaliza su base dentro del autoespacio.",
                "Normaliza todos los autovectores.",
                "Forma Q con esos autovectores ortonormales como columnas.",
                "Forma D=Q^tAQ. La diagonal contiene los autovalores en el mismo orden que las columnas de Q."
            ],
            "errores_comunes": [
                "Mezclar autovectores no normalizados en Q.",
                "Poner los autovalores en orden distinto al de las columnas de Q."
            ]
        }
    ],

"flashcards": [
        {
            "id": "alg2_fc_01",
            "frente": "¿Que condiciones debe cumplir un producto escalar?",
            "reverso": "Simetria, bilinealidad y definida positiva.",
            "categoria": "Producto escalar"
        },
        {
            "id": "alg2_fc_02",
            "frente": "¿Que es la matriz de Gram?",
            "reverso": "La matriz G=(g_ij) con g_ij=<e_i,e_j> en una base dada.",
            "categoria": "Matriz de Gram"
        },
        {
            "id": "alg2_fc_03",
            "frente": "¿Como calculo <x,y> usando una matriz de Gram?",
            "reverso": "<x,y>=x_B^t G_B y_B.",
            "categoria": "Matriz de Gram"
        },
        {
            "id": "alg2_fc_04",
            "frente": "¿Como cambia la matriz de Gram al cambiar de base?",
            "reverso": "Por congruencia: G_Bprima=P^t G_B P.",
            "categoria": "Cambio de base"
        },
        {
            "id": "alg2_fc_05",
            "frente": "¿Que significa que una base sea ortogonal?",
            "reverso": "Que sus vectores son ortogonales dos a dos.",
            "categoria": "Bases ortogonales"
        },
        {
            "id": "alg2_fc_06",
            "frente": "¿Que significa que una base sea ortonormal?",
            "reverso": "Que es ortogonal y todos sus vectores tienen norma 1.",
            "categoria": "Bases ortonormales"
        },
        {
            "id": "alg2_fc_07",
            "frente": "¿Que matriz de Gram tiene una base ortogonal?",
            "reverso": "Una matriz diagonal.",
            "categoria": "Matriz de Gram"
        },
        {
            "id": "alg2_fc_08",
            "frente": "¿Que matriz de Gram tiene una base ortonormal?",
            "reverso": "La identidad.",
            "categoria": "Matriz de Gram"
        },
        {
            "id": "alg2_fc_09",
            "frente": "¿Como se calcula la norma inducida?",
            "reverso": "||x||=sqrt(<x,x>).",
            "categoria": "Norma"
        },
        {
            "id": "alg2_fc_10",
            "frente": "¿Cuando son ortogonales dos vectores?",
            "reverso": "Cuando <x,y>=0.",
            "categoria": "Ortogonalidad"
        },
        {
            "id": "alg2_fc_11",
            "frente": "¿Que es U_perp?",
            "reverso": "El conjunto de vectores ortogonales a todos los vectores de U.",
            "categoria": "Complemento ortogonal"
        },
        {
            "id": "alg2_fc_12",
            "frente": "¿Formula de proyeccion sobre un vector u?",
            "reverso": "p_u(x)=(<x,u>/||u||^2)u.",
            "categoria": "Proyeccion"
        },
        {
            "id": "alg2_fc_13",
            "frente": "¿Que hace Gram-Schmidt?",
            "reverso": "Convierte una base cualquiera en una base ortogonal; luego se normaliza para obtener una ortonormal.",
            "categoria": "Gram-Schmidt"
        },
        {
            "id": "alg2_fc_14",
            "frente": "¿Que es una matriz ortogonal?",
            "reverso": "Una matriz Q tal que Q^tQ=I, o equivalentemente Q^{-1}=Q^t.",
            "categoria": "Matrices ortogonales"
        },
        {
            "id": "alg2_fc_15",
            "frente": "¿Diferencia clave entre congruencia y semejanza?",
            "reverso": "Formas bilineales/cuadraticas: P^tAP. Endomorfismos: P^{-1}AP.",
            "categoria": "Conexiones"
        },
        {
            "id": "alg2_fc_16",
            "frente": "¿Como se calcula la distancia inducida?",
            "reverso": "d(x,y)=||x-y||.",
            "categoria": "Distancia"
        }
    ],


"preguntas_vf": [
        {
            "id": "alg2_vf_01",
            "pregunta": "Todo producto escalar es una forma bilineal simetrica definida positiva.",
            "respuesta": True,
            "explicacion": "Es justamente la proposicion principal del tema.",
            "categoria": "Producto escalar",
            "dificultad": "facil"
        },
        {
            "id": "alg2_vf_02",
            "pregunta": "Si una matriz de Gram en una base es la identidad, esa base es ortonormal.",
            "respuesta": True,
            "explicacion": "Identidad significa productos cruzados cero y normas cuadradas iguales a 1.",
            "categoria": "Matriz de Gram",
            "dificultad": "facil"
        },
        {
            "id": "alg2_vf_03",
            "pregunta": "Si una base es ortogonal, su matriz de Gram es diagonal.",
            "respuesta": True,
            "explicacion": "Los productos <e_i,e_j> con i distinto de j son cero.",
            "categoria": "Bases ortogonales",
            "dificultad": "facil"
        },
        {
            "id": "alg2_vf_04",
            "pregunta": "La norma inducida por un producto escalar es ||x||=<x,x>.",
            "respuesta": False,
            "explicacion": "Es la raiz cuadrada positiva: ||x||=sqrt(<x,x>).",
            "categoria": "Norma",
            "dificultad": "facil"
        },
        {
            "id": "alg2_vf_05",
            "pregunta": "El angulo entre vectores depende del producto escalar elegido.",
            "respuesta": True,
            "explicacion": "El numerador y las normas dependen del producto escalar.",
            "categoria": "Angulo",
            "dificultad": "media"
        },
        {
            "id": "alg2_vf_06",
            "pregunta": "Si dos vectores son ortogonales no nulos, son linealmente independientes.",
            "respuesta": True,
            "explicacion": "Un sistema de vectores no nulos ortogonales dos a dos es linealmente independiente.",
            "categoria": "Ortogonalidad",
            "dificultad": "media"
        },
        {
            "id": "alg2_vf_07",
            "pregunta": "Para calcular U_perp basta imponer ortogonalidad con una base de U.",
            "respuesta": True,
            "explicacion": "Si es ortogonal a una base de U, lo es a todas sus combinaciones lineales.",
            "categoria": "Complemento ortogonal",
            "dificultad": "media"
        },
        {
            "id": "alg2_vf_08",
            "pregunta": "Siempre se cumple V = U union U_perp.",
            "respuesta": False,
            "explicacion": "La relacion correcta es suma directa: V = U ⊕ U_perp.",
            "categoria": "Complemento ortogonal",
            "dificultad": "media"
        },
        {
            "id": "alg2_vf_09",
            "pregunta": "La formula de proyeccion p_U(x)=sum((<x,u_i>/||u_i||^2)u_i) requiere que la base de U sea ortogonal.",
            "respuesta": True,
            "explicacion": "Si la base no es ortogonal, primero hay que ortogonalizar o resolver un sistema.",
            "categoria": "Proyeccion",
            "dificultad": "dificil"
        },
        {
            "id": "alg2_vf_10",
            "pregunta": "Si Q es ortogonal, entonces Q^{-1}=Q^t.",
            "respuesta": True,
            "explicacion": "Es una caracterizacion de matrices ortogonales.",
            "categoria": "Matrices ortogonales",
            "dificultad": "facil"
        },
        {
            "id": "alg2_vf_11",
            "pregunta": "Una matriz real simetrica siempre se puede diagonalizar ortogonalmente.",
            "respuesta": True,
            "explicacion": "El teorema espectral garantiza diagonalizacion ortogonal.",
            "categoria": "Diagonalizacion",
            "dificultad": "media"
        },
        {
            "id": "alg2_vf_12",
            "pregunta": "En una base ortonormal, las coordenadas de x son <x,e_i>.",
            "respuesta": True,
            "explicacion": "Porque ||e_i||^2=1.",
            "categoria": "Coeficientes de Fourier",
            "dificultad": "media"
        },
        {
            "id": "alg2_vf_13",
            "pregunta": "Para formas bilineales se cambia de base con P^{-1}AP.",
            "respuesta": False,
            "explicacion": "Eso es semejanza; en formas bilineales se usa P^tAP.",
            "categoria": "Conexiones",
            "dificultad": "facil"
        },
        {
            "id": "alg2_vf_14",
            "pregunta": "El complemento ortogonal de un subespacio de dimension r en R^n tiene dimension n-r.",
            "respuesta": True,
            "explicacion": "En espacios euclideos finitos, dim V = dim U + dim U_perp.",
            "categoria": "Complemento ortogonal",
            "dificultad": "media"
        },
        {
            "id": "alg2_vf_15",
            "pregunta": "Gram-Schmidt cambia el subespacio generado por los primeros k vectores.",
            "respuesta": False,
            "explicacion": "Gram-Schmidt conserva lin{b1,...,bk}=lin{o1,...,ok}.",
            "categoria": "Gram-Schmidt",
            "dificultad": "dificil"
        }
    ],

"preguntas_mc": [
        {
            "id": "alg2_mc_01",
            "pregunta": "¿Que expresion calcula el producto escalar usando una matriz de Gram G?",
            "opciones": [
                "x^t G y",
                "G^t x y",
                "x^t y G",
                "Gx + Gy"
            ],
            "respuesta": 1,
            "explicacion": "La expresion correcta es <x,y>=x^tGy.",
            "categoria": "Matriz de Gram",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_02",
            "pregunta": "Si una base es ortonormal, su matriz de Gram es:",
            "opciones": [
                "Diagonal cualquiera",
                "La identidad",
                "La matriz nula",
                "Una matriz triangular"
            ],
            "respuesta": 2,
            "explicacion": "Ortonormal significa productos cruzados cero y norma 1.",
            "categoria": "Bases ortonormales",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_03",
            "pregunta": "¿Cual es la norma inducida por un producto escalar?",
            "opciones": [
                "sqrt(<x,x>)",
                "<x,x>",
                "abs(<x,y>)",
                "x^t y"
            ],
            "respuesta": 1,
            "explicacion": "La norma inducida es la raiz positiva de <x,x>.",
            "categoria": "Norma",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_04",
            "pregunta": "Para calcular U_perp si U=lin{u1,u2}, debes resolver:",
            "opciones": [
                "<y,y>=0",
                "<u1,y>=0 y <u2,y>=0",
                "u1+u2=0",
                "det(U)=0"
            ],
            "respuesta": 2,
            "explicacion": "Un vector y esta en U_perp si es ortogonal a todos los generadores de U.",
            "categoria": "Complemento ortogonal",
            "dificultad": "media"
        },
        {
            "id": "alg2_mc_05",
            "pregunta": "¿Que formula proyecta x sobre un vector u?",
            "opciones": [
                "(<u,u>/<x,u>)x",
                "(<x,u>/||u||^2)u",
                "(<x,u>/||x||^2)x",
                "x-u"
            ],
            "respuesta": 2,
            "explicacion": "La proyeccion paralela sobre u es p_u(x)=(<x,u>/||u||^2)u.",
            "categoria": "Proyeccion",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_06",
            "pregunta": "¿Que algoritmo se usa para convertir una base en ortogonal?",
            "opciones": [
                "Gauss-Jordan",
                "Gram-Schmidt",
                "Newton-Raphson",
                "Regla de Cramer"
            ],
            "respuesta": 2,
            "explicacion": "Gram-Schmidt ortogonaliza una base.",
            "categoria": "Gram-Schmidt",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_07",
            "pregunta": "Si Q es ortogonal, entonces:",
            "opciones": [
                "Q^{-1}=Q^t",
                "Q^2=0",
                "det(Q)=0",
                "Q no tiene inversa"
            ],
            "respuesta": 1,
            "explicacion": "La inversa de una matriz ortogonal es su traspuesta.",
            "categoria": "Matrices ortogonales",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_08",
            "pregunta": "Para diagonalizar ortogonalmente una matriz real simetrica A se usa:",
            "opciones": [
                "D=Q^tAQ",
                "D=Q+A",
                "D=AQ",
                "D=Q^t+AQ"
            ],
            "respuesta": 1,
            "explicacion": "Como Q es ortogonal, Q^{-1}=Q^t, por eso D=Q^tAQ.",
            "categoria": "Diagonalizacion",
            "dificultad": "media"
        },
        {
            "id": "alg2_mc_09",
            "pregunta": "En una base ortogonal, las coordenadas de x son:",
            "opciones": [
                "<x,e_i>",
                "<x,e_i>/||e_i||^2",
                "||x||/||e_i||",
                "det(x,e_i)"
            ],
            "respuesta": 2,
            "explicacion": "Son los coeficientes de Fourier en base ortogonal.",
            "categoria": "Coeficientes de Fourier",
            "dificultad": "media"
        },
        {
            "id": "alg2_mc_10",
            "pregunta": "¿Que cambio se usa para matrices de formas bilineales o Gram?",
            "opciones": [
                "Semejanza P^{-1}AP",
                "Congruencia P^tAP",
                "Producto AP",
                "Suma A+P"
            ],
            "respuesta": 2,
            "explicacion": "Las matrices de Gram cambian por congruencia.",
            "categoria": "Cambio de base",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_11",
            "pregunta": "¿Cual es la norma infinito de x=(2,-3,15)?",
            "opciones": [
                "20",
                "sqrt(238)",
                "15",
                "3"
            ],
            "respuesta": 3,
            "explicacion": "La norma infinito es el maximo de los valores absolutos: max{2,3,15}=15.",
            "categoria": "Normas",
            "dificultad": "facil"
        },
        {
            "id": "alg2_mc_12",
            "pregunta": "¿Que significa que un espacio euclideo sea canonico?",
            "opciones": [
                "Que no tiene producto escalar",
                "Que la matriz del producto escalar usual en la base usual es I",
                "Que todos sus vectores son nulos",
                "Que solo existe en R2"
            ],
            "respuesta": 2,
            "explicacion": "Canonico significa que el producto escalar usual tiene matriz identidad en la base usual.",
            "categoria": "Espacio canonico",
            "dificultad": "media"
        }
    ],
     
        "ejercicios_guiados": [
        {
            "id": "alg2_ej_01",
            "enunciado": "En R2 con <x,y>=2x1y1+x1y2+x2y1+2x2y2, calcula la matriz de Gram en la base usual.",
            "categoria": "Matriz de Gram",
            "dificultad": "facil",
            "solucion": [
                "Tomamos e1=(1,0) y e2=(0,1).",
                "g11=<e1,e1>=2.",
                "g12=<e1,e2>=1.",
                "g21=<e2,e1>=1.",
                "g22=<e2,e2>=2.",
                "La matriz de Gram es [[2,1],[1,2]].",
                "Es simetrica y definida positiva, por tanto define producto escalar."
            ]
        },
        {
            "id": "alg2_ej_02",
            "enunciado": "Con G=[[2,1],[1,2]], calcula <x,y> para x=(1,-3), y=(3,-2).",
            "categoria": "Producto escalar",
            "dificultad": "facil",
            "solucion": [
                "Usamos <x,y>=x^t G y.",
                "Primero G y = [[2,1],[1,2]]*(3,-2) = (4,-1).",
                "Luego x^t(Gy)=(1,-3)·(4,-1)=4+3=7.",
                "Por tanto <x,y>=7."
            ]
        },
        {
            "id": "alg2_ej_03",
            "enunciado": "En R2 usual, calcula longitud, distancia y angulo entre x=(1,-3) e y=(3,-2).",
            "categoria": "Longitud, angulo y distancia",
            "dificultad": "media",
            "solucion": [
                "Producto usual: <x,y>=1*3+(-3)*(-2)=9.",
                "||x||=sqrt(1^2+(-3)^2)=sqrt(10).",
                "||y||=sqrt(3^2+(-2)^2)=sqrt(13).",
                "Angulo: alpha=arccos(9/(sqrt(10)*sqrt(13))).",
                "Distancia: d(x,y)=||x-y||=||(-2,-1)||=sqrt(5)."
            ]
        },
        {
            "id": "alg2_ej_04",
            "enunciado": "Halla el complemento ortogonal de u=(2,5,-4) en R3 usual.",
            "categoria": "Complemento ortogonal",
            "dificultad": "media",
            "solucion": [
                "Tomamos y=(x,y,z).",
                "Imponemos <u,y>=0.",
                "2x+5y-4z=0.",
                "Esa es la ecuacion cartesiana de u_perp.",
                "Parametrizamos: toma x=alpha, y=beta.",
                "Entonces z=(2alpha+5beta)/4.",
                "Una base posible es {(2,0,1),(0,4,5)} si evitamos fracciones."
            ]
        },
        {
            "id": "alg2_ej_05",
            "enunciado": "Sea U=lin{(1,2,-3),(0,-1,5)} en R3 usual. Halla U_perp.",
            "categoria": "Complemento ortogonal",
            "dificultad": "media",
            "solucion": [
                "Tomamos y=(x,y,z).",
                "Imponemos ortogonalidad con los dos generadores.",
                "<(1,2,-3),(x,y,z)>=x+2y-3z=0.",
                "<(0,-1,5),(x,y,z)>=-y+5z=0.",
                "De la segunda ecuacion y=5z.",
                "En la primera x+10z-3z=0, luego x=-7z.",
                "Parametrizamos con z=t: y=t*(-7,5,1).",
                "Por tanto U_perp=lin{(-7,5,1)}."
            ]
        },
        {
            "id": "alg2_ej_06",
            "enunciado": "Proyecta x=(3,0,-2) sobre u=(1,-2,1) en R3 usual.",
            "categoria": "Proyeccion",
            "dificultad": "media",
            "solucion": [
                "Calculamos <x,u>=3*1+0*(-2)+(-2)*1=1.",
                "Calculamos ||u||^2=1^2+(-2)^2+1^2=6.",
                "p_u(x)=(1/6)u=(1/6,-1/3,1/6).",
                "Componente perpendicular: x-p_u(x)=(17/6,1/3,-13/6).",
                "Comprobacion: la componente perpendicular tiene producto escalar cero con u."
            ]
        },
        {
            "id": "alg2_ej_07",
            "enunciado": "Aplica Gram-Schmidt a B={(1,1,1),(1,1,0),(1,0,0)} en R3 usual.",
            "categoria": "Gram-Schmidt",
            "dificultad": "dificil",
            "solucion": [
                "b1=(1,1,1), b2=(1,1,0), b3=(1,0,0).",
                "o1=b1=(1,1,1).",
                "<b2,o1>=2 y ||o1||^2=3.",
                "o2=b2-(2/3)o1=(1/3,1/3,-2/3), proporcional a (1,1,-2).",
                "Tomamos o2=(1,1,-2).",
                "<b3,o1>=1 y ||o1||^2=3.",
                "<b3,o2>=1 y ||o2||^2=6.",
                "o3=b3-(1/3)o1-(1/6)o2=(1/2,-1/2,0), proporcional a (1,-1,0).",
                "Base ortogonal: {(1,1,1),(1,1,-2),(1,-1,0)}.",
                "Base ortonormal: divide cada vector por su norma."
            ]
        },
        {
            "id": "alg2_ej_08",
            "enunciado": "Normaliza la base ortogonal {(1,1,1),(1,1,-2),(1,-1,0)}.",
            "categoria": "Base ortonormal",
            "dificultad": "facil",
            "solucion": [
                "Norma de (1,1,1): sqrt(3).",
                "Norma de (1,1,-2): sqrt(6).",
                "Norma de (1,-1,0): sqrt(2).",
                "Base ortonormal: {(1/sqrt(3))(1,1,1), (1/sqrt(6))(1,1,-2), (1/sqrt(2))(1,-1,0)}."
            ]
        },
        {
            "id": "alg2_ej_09",
            "enunciado": "Comprueba si Q es ortogonal sabiendo que sus columnas son una base ortonormal.",
            "categoria": "Matrices ortogonales",
            "dificultad": "facil",
            "solucion": [
                "Si las columnas son ortonormales, el producto escalar de una columna consigo misma es 1.",
                "El producto escalar entre columnas distintas es 0.",
                "Por tanto Q^tQ tiene 1 en la diagonal y 0 fuera de la diagonal.",
                "Entonces Q^tQ=I.",
                "Luego Q es ortogonal y Q^{-1}=Q^t."
            ]
        },
        {
            "id": "alg2_ej_10",
            "enunciado": "En R2[x] con base {1,x,x^2}, calcula la matriz de Gram para <p,q>=integral_0^1 p(x)q(x)dx.",
            "categoria": "Polinomios",
            "dificultad": "media",
            "solucion": [
                "Base: e1=1, e2=x, e3=x^2.",
                "g11=integral_0^1 1 dx=1.",
                "g12=integral_0^1 x dx=1/2.",
                "g13=integral_0^1 x^2 dx=1/3.",
                "g22=integral_0^1 x^2 dx=1/3.",
                "g23=integral_0^1 x^3 dx=1/4.",
                "g33=integral_0^1 x^4 dx=1/5.",
                "Matriz: [[1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]]."
            ]
        },
        {
            "id": "alg2_ej_11",
            "enunciado": "Calcula la norma infinito de x=(2,-3,15) y la norma 1.",
            "categoria": "Normas",
            "dificultad": "facil",
            "solucion": [
                "Norma infinito: max{|2|,|-3|,|15|}=15.",
                "Norma 1: |2|+|-3|+|15|=20."
            ]
        },
        {
            "id": "alg2_ej_12",
            "enunciado": "Halla la imagen y el rango de A=[[1,2,0],[0,1,1]].",
            "categoria": "Algebra I - Imagen y rango",
            "dificultad": "media",
            "solucion": [
                "La imagen esta generada por las columnas: c1=(1,0), c2=(2,1), c3=(0,1).",
                "Observamos que c3=c2-2c1.",
                "Una base de la imagen es {(1,0),(2,1)}.",
                "Por tanto rango(A)=2."
            ]
        },
        {
            "id": "alg2_ej_13",
            "enunciado": "Calcula el nucleo de A=[[1,2,0],[0,1,1]].",
            "categoria": "Algebra I - Nucleo",
            "dificultad": "media",
            "solucion": [
                "Resolvemos Ax=0 con x=(x,y,z).",
                "Sistema: x+2y=0, y+z=0.",
                "De la segunda, z=-y.",
                "De la primera, x=-2y.",
                "Tomando y=t: (x,y,z)=t*(-2,1,-1).",
                "Nucleo=lin{(-2,1,-1)}.",
                "dim Nuc=1."
            ]
        },
        {
            "id": "alg2_ej_14",
            "enunciado": "Diagonaliza ortogonalmente M=[[1,-1,-1],[-1,1,-1],[-1,-1,1]] sabiendo que tiene autovalores -1,2,2.",
            "categoria": "Diagonalizacion ortogonal",
            "dificultad": "dificil",
            "solucion": [
                "Para lambda=-1, un autovector es v1=(1,1,1).",
                "Para lambda=2, el autoespacio es el plano x+y+z=0.",
                "Escogemos dos vectores ortogonales en ese plano, por ejemplo v2=(1,-1,0) y v3=(1,1,-2).",
                "Normalizamos: e1=(1/sqrt(3))(1,1,1), e2=(1/sqrt(2))(1,-1,0), e3=(1/sqrt(6))(1,1,-2).",
                "Formamos Q con columnas e1,e2,e3.",
                "Entonces D=Q^t M Q=diag(-1,2,2), en el mismo orden de columnas."
            ]
        },
        {
            "id": "alg2_ej_15",
            "enunciado": "Explica por que una matriz de cambio entre bases ortonormales es ortogonal.",
            "categoria": "Matrices ortogonales",
            "dificultad": "media",
            "solucion": [
                "Las columnas de la matriz de cambio son las coordenadas de los vectores de una base respecto a la otra.",
                "Como ambas bases son ortonormales, esas columnas son ortonormales con el producto usual de coordenadas.",
                "Por tanto la matriz Q cumple Q^tQ=I.",
                "Entonces Q es ortogonal y Q^{-1}=Q^t."
            ]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "producto escalar",
            "que_significa": "Te estan dando o pidiendo una forma bilineal simetrica definida positiva.",
            "que_suele_pedir": [
                "Comprobar si una expresion define producto escalar.",
                "Calcular matriz de Gram.",
                "Calcular norma, angulo, distancia u ortogonalidad.",
                "Trabajar con bases ortogonales u ortonormales."
            ],
            "operaciones_recomendadas": [
                "Escribe la matriz asociada G.",
                "Comprueba que G sea simetrica.",
                "Comprueba que G sea definida positiva.",
                "Usa <x,y> = x^t G y."
            ],
            "pista_examen": "Si aparece producto escalar, casi siempre vas a usar una matriz de Gram o una formula de norma/proyeccion."
        },
        {
            "palabra_clave": "matriz metrica / matriz de Gram",
            "que_significa": "Es la matriz asociada al producto escalar en una base concreta.",
            "que_suele_pedir": [
                "Calcular G en una base.",
                "Cambiar G a otra base.",
                "Decidir si una base es ortogonal u ortonormal."
            ],
            "operaciones_recomendadas": [
                "Si te dan la base B={e1,...,en}, calcula g_ij=<e_i,e_j>.",
                "Si cambias de base, usa G_nueva = P^t G_antigua P.",
                "Si G es diagonal, la base es ortogonal.",
                "Si G es la identidad, la base es ortonormal."
            ],
            "pista_examen": "La matriz de Gram siempre depende de la base y del producto escalar."
        },
        {
            "palabra_clave": "base ortogonal",
            "que_significa": "Los vectores de la base son perpendiculares dos a dos.",
            "que_suele_pedir": [
                "Comprobar ortogonalidad.",
                "Calcular coordenadas de un vector usando coeficientes de Fourier.",
                "Facilitar proyecciones."
            ],
            "operaciones_recomendadas": [
                "Calcula <e_i,e_j> para i distinto de j.",
                "Si todos dan 0, la base es ortogonal.",
                "Las coordenadas se calculan como <x,e_i>/||e_i||^2.",
                "La matriz de Gram en esa base debe ser diagonal."
            ],
            "pista_examen": "Ortogonal no significa norma 1. Eso seria ortonormal."
        },
        {
            "palabra_clave": "base ortonormal",
            "que_significa": "Es una base ortogonal donde todos los vectores tienen norma 1.",
            "que_suele_pedir": [
                "Comprobar que una base es ortonormal.",
                "Calcular matriz de cambio entre bases ortonormales.",
                "Usar coordenadas simples de Fourier."
            ],
            "operaciones_recomendadas": [
                "Comprueba <e_i,e_j>=0 si i distinto de j.",
                "Comprueba ||e_i||=1 para todos.",
                "Si formas una matriz Q con esos vectores como columnas, Q debe ser ortogonal.",
                "En base ortonormal, las coordenadas son simplemente <x,e_i>."
            ],
            "pista_examen": "Si el problema dice que dos bases son ortonormales, piensa en Q^{-1}=Q^t."
        },
        {
            "palabra_clave": "Gram-Schmidt",
            "que_significa": "Te piden convertir una base cualquiera en una base ortogonal u ortonormal.",
            "que_suele_pedir": [
                "Obtener una base ortogonal.",
                "Obtener una base ortonormal.",
                "Partir de la base usual o de una base dada."
            ],
            "operaciones_recomendadas": [
                "Toma o1=b1.",
                "Calcula o2=b2 - proy_o1(b2).",
                "Calcula o3=b3 - proy_o1(b3) - proy_o2(b3).",
                "Al final normaliza: e_i = o_i/||o_i||.",
                "Si el producto escalar no es usual, usa <x,y>=x^t G y."
            ],
            "pista_examen": "Gram-Schmidt es basicamente ir quitando las proyecciones para que lo nuevo quede perpendicular a lo anterior."
        },
        {
            "palabra_clave": "complemento ortogonal",
            "que_significa": "Te piden todos los vectores perpendiculares a un vector o subespacio.",
            "que_suele_pedir": [
                "Dimension.",
                "Ecuaciones parametricas.",
                "Ecuaciones cartesianas.",
                "Descomponer un vector como u + u_perp."
            ],
            "operaciones_recomendadas": [
                "Si U=lin{u1,...,ur}, escribe un vector generico x=(x,y,z,...)",
                "Impone <u1,x>=0, <u2,x>=0, etc.",
                "Resuelve el sistema homogeneo.",
                "La solucion es U_perp.",
                "Comprueba dim(V)=dim(U)+dim(U_perp)."
            ],
            "pista_examen": "Complemento ortogonal casi siempre se transforma en resolver un sistema lineal."
        },
        {
            "palabra_clave": "proyeccion ortogonal",
            "que_significa": "Te piden separar un vector en parte paralela y parte perpendicular.",
            "que_suele_pedir": [
                "Componente paralela.",
                "Componente perpendicular.",
                "Proyeccion sobre un vector.",
                "Proyeccion sobre un subespacio."
            ],
            "operaciones_recomendadas": [
                "Si proyectas sobre un vector u: p_u(x)=(<x,u>/||u||^2)u.",
                "La parte perpendicular es x-p_u(x).",
                "Si proyectas sobre un subespacio, primero consigue una base ortogonal.",
                "Luego suma las proyecciones sobre cada vector de esa base."
            ],
            "pista_examen": "Si te pide paralela y perpendicular, no te quedes solo con la proyeccion: calcula tambien x - proyeccion."
        },
        {
            "palabra_clave": "cambio de base",
            "que_significa": "Tienes que pasar coordenadas o matrices de una base a otra.",
            "que_suele_pedir": [
                "Coordenadas de un vector en otra base.",
                "Matriz de una forma bilineal en otra base.",
                "Matriz de Gram en otra base.",
                "Ecuacion de cambio de coordenadas."
            ],
            "operaciones_recomendadas": [
                "Construye la matriz P con columnas iguales a los vectores de la nueva base escritos en la base antigua.",
                "Para vectores: x_antigua = P*x_nueva.",
                "Para pasar de antigua a nueva: x_nueva = P^{-1}*x_antigua.",
                "Para Gram/formas bilineales: G_nueva = P^t G_antigua P.",
                "Para endomorfismos: A_nueva = P^{-1} A_antigua P."
            ],
            "pista_examen": "La pregunta clave es: ¿estoy cambiando coordenadas de vectores, una forma bilineal, o una aplicacion lineal?"
        },
        {
            "palabra_clave": "endomorfismo",
            "que_significa": "Es una aplicacion lineal de un espacio en si mismo: f: V -> V.",
            "que_suele_pedir": [
                "Matriz asociada.",
                "Nucleo e imagen.",
                "Autovalores y autovectores.",
                "Diagonalizacion por semejanza."
            ],
            "operaciones_recomendadas": [
                "Representa la aplicacion con una matriz A.",
                "Nucleo: resuelve Ax=0.",
                "Imagen: estudia las columnas de A.",
                "Rango: cuenta pivotes.",
                "Si diagonalizas: busca autovalores y autovectores.",
                "Cambio de base de endomorfismo: A_nueva = P^{-1} A P."
            ],
            "pista_examen": "Endomorfismo = matriz de aplicacion lineal. Piensa en semejanza, no en congruencia."
        },
        {
            "palabra_clave": "automorfismo",
            "que_significa": "Es un endomorfismo invertible.",
            "que_suele_pedir": [
                "Comprobar si es invertible.",
                "Calcular inversa.",
                "Ver si el nucleo es trivial.",
                "Ver si el determinante es distinto de cero."
            ],
            "operaciones_recomendadas": [
                "Calcula det(A).",
                "Si det(A) != 0, es automorfismo.",
                "Equivalente: Nuc(A)={0}.",
                "Equivalente: rango(A)=n.",
                "Si hace falta, calcula A^{-1}."
            ],
            "pista_examen": "Automorfismo = endomorfismo que no pierde informacion."
        },
        {
            "palabra_clave": "isomorfismo",
            "que_significa": "Es una aplicacion lineal invertible entre dos espacios vectoriales.",
            "que_suele_pedir": [
                "Comprobar si dos espacios son isomorfos.",
                "Ver si la aplicacion es biyectiva.",
                "Comprobar dimensiones.",
                "Estudiar nucleo e imagen."
            ],
            "operaciones_recomendadas": [
                "Si los espacios tienen distinta dimension, no pueden ser isomorfos.",
                "Si tienen la misma dimension, comprueba rango completo.",
                "Comprueba que el nucleo sea {0}.",
                "Si hay matriz cuadrada, calcula determinante."
            ],
            "pista_examen": "Isomorfismo = cambio de nombre/coordenadas sin perder estructura."
        },
        {
            "palabra_clave": "diagonaliza por semejanza",
            "que_significa": "Estas tratando una matriz como aplicacion lineal o endomorfismo.",
            "que_suele_pedir": [
                "Autovalores.",
                "Autovectores.",
                "Matriz P.",
                "Matriz diagonal D.",
                "Comprobar D=P^{-1}AP."
            ],
            "operaciones_recomendadas": [
                "Calcula det(A-lambda I).",
                "Encuentra autovalores.",
                "Para cada autovalor resuelve (A-lambda I)x=0.",
                "Forma P con autovectores como columnas.",
                "Forma D con autovalores en el mismo orden.",
                "Si pide ortogonalmente y A es simetrica, normaliza los autovectores y usa D=Q^t A Q."
            ],
            "pista_examen": "Semejanza = P^{-1}AP. Si dice ortogonalmente, entonces P=Q y Q^{-1}=Q^t."
        },
        {
            "palabra_clave": "diagonaliza por congruencia",
            "que_significa": "Estas tratando una forma bilineal, forma cuadratica o matriz de Gram.",
            "que_suele_pedir": [
                "Forma diagonal.",
                "Base donde la matriz queda diagonal.",
                "Signatura.",
                "Clasificacion de forma cuadratica.",
                "Base ortogonal respecto al producto escalar."
            ],
            "operaciones_recomendadas": [
                "Usa operaciones simultaneas de filas y columnas.",
                "O construye una base ortogonal respecto a esa forma.",
                "La matriz cambia como D=P^t A P.",
                "Cuenta signos si es forma cuadratica.",
                "Si es producto escalar, deberia quedar con positivos en diagonal."
            ],
            "pista_examen": "Congruencia = P^tAP. No mezclar con P^{-1}AP."
        },
        {
            "palabra_clave": "nucleo",
            "que_significa": "Te piden los vectores que se van a cero.",
            "que_suele_pedir": [
                "Base del nucleo.",
                "Dimension del nucleo.",
                "Ecuaciones parametricas.",
                "Comprobar inyectividad."
            ],
            "operaciones_recomendadas": [
                "Escribe Ax=0.",
                "Reduce por Gauss.",
                "Identifica variables libres.",
                "Expresa la solucion con parametros.",
                "Los vectores que multiplican los parametros forman una base."
            ],
            "pista_examen": "Nucleo siempre va con sistema homogeneo."
        },
        {
            "palabra_clave": "imagen",
            "que_significa": "Te piden todos los vectores que puede producir la aplicacion.",
            "que_suele_pedir": [
                "Base de la imagen.",
                "Dimension de la imagen.",
                "Rango.",
                "Comprobar sobreyectividad."
            ],
            "operaciones_recomendadas": [
                "Mira las columnas de A.",
                "Reduce para detectar columnas pivote.",
                "Las columnas pivote originales forman base de la imagen.",
                "El numero de pivotes es el rango."
            ],
            "pista_examen": "Imagen = espacio generado por las columnas de la matriz."
        },
        {
            "palabra_clave": "rango",
            "que_significa": "Es la dimension de la imagen.",
            "que_suele_pedir": [
                "Dimension de imagen.",
                "Comprobar independencia de columnas.",
                "Teorema rango-nulidad."
            ],
            "operaciones_recomendadas": [
                "Reduce la matriz por Gauss.",
                "Cuenta pivotes.",
                "Usa dim Nuc(A) = numero de columnas - rango(A)."
            ],
            "pista_examen": "Rango = numero de pivotes = dimension de la imagen."
        }
    ]
}