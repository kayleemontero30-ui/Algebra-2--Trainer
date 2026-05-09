# -*- coding: utf-8 -*-

TEMA3 = {
    "nombre": "Tema 3 - Espacios afines y afines euclideos",

    "resumen": """
Este tema estudia espacios afines y espacios afines euclideos. La idea principal es
separar punto y vector:

- Punto: posicion.
- Vector: desplazamiento entre puntos.

En un espacio afin no se suman puntos directamente. Lo que si tiene sentido es:
- Restar dos puntos para obtener un vector: AB = B - A.
- Sumar un vector a un punto para obtener otro punto.

1. Espacio afin

Un espacio afin Omega sobre un espacio vectorial V es un conjunto de puntos donde
cada par de puntos A,B determina un vector AB en V.

Propiedades clave:
- Para todo punto A y todo vector v existe un unico punto B tal que AB = v.
- Para puntos A,B,C se cumple AB + BC = AC.
- La dimension del espacio afin es la dimension de V.

2. Espacio afin euclideo o metrico

Si V tiene producto escalar, el espacio afin permite hablar de distancia, angulo,
ortogonalidad y proyeccion.

3. Sistema de referencia afin

Una referencia afin tiene:
- un origen O,
- una base B del espacio vectorial asociado.

Las coordenadas de un punto P son las coordenadas del vector OP en la base B.

En cambio de referencia afin NO basta cambiar base: tambien cambia el origen.

4. Variedad afin

Una variedad afin se escribe como:

L = P0 + W

donde P0 es un punto y W es el subespacio de direccion.
La dimension de L es dim(W).

Ejemplos:
- dim 0: punto.
- dim 1: recta.
- dim 2: plano.
- dim n-1: hiperplano.

5. Rectas

Una recta se escribe como:

r: P = P0 + lambda*u

P0 es un punto de paso y u es el vector director.
Cuando el objeto es una recta, casi siempre necesitas su vector director porque indica
la direccion de la recta.

El vector director sirve para:
- escribir ecuaciones parametricas,
- calcular angulos entre rectas,
- estudiar paralelismo,
- calcular distancia punto-recta mediante proyeccion.

6. Planos

Un plano parametrico se escribe:

pi: P = P0 + lambda*u + mu*v

Un plano cartesiano se escribe:

ax + by + cz = d

En la forma cartesiana, n=(a,b,c) es el vector normal.
Cuando el objeto es un plano en cartesiana, casi siempre necesitas su normal porque
el normal es perpendicular al plano.

El normal sirve para:
- distancia punto-plano,
- angulo entre planos,
- recta perpendicular al plano,
- comprobar paralelismo de planos.

7. Posiciones relativas

Para estudiar intersecciones se usa un sistema lineal Ax=b:

- Si rg(A) != rg(A|b), no hay interseccion.
- Si rg(A) = rg(A|b), hay interseccion.
- Dimension de la solucion = n - rg(A).

En R3:
- dimension 0: punto.
- dimension 1: recta.
- dimension 2: plano.

Recta-recta:
- Coincidentes: misma recta.
- Paralelas: mismo director, sin puntos comunes.
- Secantes: se cortan en un punto.
- Cruzadas: no son paralelas y no se cortan.

Plano-plano:
- Paralelos o coincidentes si sus normales son proporcionales.
- Secantes si sus normales no son proporcionales; se cortan en una recta.

Recta-plano:
- Si u·n != 0, la recta corta al plano en un punto.
- Si u·n = 0, la recta es paralela al plano o esta contenida.

8. Distancias

Punto-recta:
Se usa el vector director de la recta. Se proyecta el vector desde un punto de la recta
hasta el punto exterior sobre el director, y la distancia es la componente perpendicular.

Punto-plano:
Se usa el vector normal porque la distancia minima al plano va en direccion perpendicular.

Rectas paralelas:
Se toma un punto de una recta y se mide su distancia a la otra.

Rectas cruzadas:
La direccion de la distancia minima es perpendicular a ambos directores, por eso se usa
u_r x u_s.

9. Angulos

Recta-recta:
Se usan los vectores directores.

Plano-plano:
Se usan los vectores normales.

Recta-plano:
Se usa el director de la recta y el normal del plano. El angulo recta-plano es el
complementario del angulo entre u y n.

10. Consejos de examen

Antes de calcular, pregunta:
- ¿Estoy con puntos, recta, plano o variedad general?
- Si es recta: ¿cual es su punto y su vector director?
- Si es plano cartesiano: ¿cual es su normal?
- Si es plano parametrico: ¿cuales son sus dos directores?
- Si me piden posicion relativa: ¿conviene montar sistema y comparar rangos?
- Si me piden distancia: ¿la perpendicular va en direccion de un director o de un normal?
""",

    "formulas": [
        {
            "nombre": "Vector entre dos puntos",
            "formula": "AB = B - A",
            "uso": "Convertir dos puntos en un vector desplazamiento.",
            "cuando_usarla": ["Distancia entre puntos", "Recta por dos puntos", "Alineacion"],
            "detalles": ["Si A=(a1,a2,a3), B=(b1,b2,b3), entonces AB=(b1-a1,b2-a2,b3-a3)."]
        },
        {
            "nombre": "Distancia entre puntos",
            "formula": "d(A,B)=||AB||",
            "uso": "Medir la distancia entre dos puntos.",
            "cuando_usarla": ["Distancia punto-punto", "Problemas de lugares geometricos"],
            "detalles": ["En R3 usual se usa la raiz de la suma de cuadrados."]
        },
        {
            "nombre": "Recta vectorial",
            "formula": "r: P = P0 + lambda*u",
            "uso": "Representar una recta por punto y vector director.",
            "cuando_usarla": ["Ecuaciones parametricas", "Angulos entre rectas", "Distancias a rectas"],
            "detalles": ["u es vector director; lambda es parametro libre."]
        },
        {
            "nombre": "Recta por dos puntos",
            "formula": "r: P = A + lambda*(B-A)",
            "uso": "Construir una recta que pasa por A y B.",
            "cuando_usarla": ["Puntos alineados", "Recta determinada por dos puntos"],
            "detalles": ["El vector director es AB=B-A."]
        },
        {
            "nombre": "Plano parametrico",
            "formula": "pi: P = P0 + lambda*u + mu*v",
            "uso": "Representar un plano por un punto y dos direcciones.",
            "cuando_usarla": ["Plano por punto y dos directores", "Plano que contiene dos rectas"],
            "detalles": ["u y v deben ser linealmente independientes."]
        },
        {
            "nombre": "Plano cartesiano",
            "formula": "ax + by + cz = d",
            "uso": "Representar un plano usando un vector normal.",
            "cuando_usarla": ["Distancia punto-plano", "Angulo entre planos", "Posicion relativa de planos"],
            "detalles": ["El normal es n=(a,b,c)."]
        },
        {
            "nombre": "Normal de un plano por dos directores",
            "formula": "n = u x v",
            "uso": "Obtener un normal a un plano en R3.",
            "cuando_usarla": ["Pasar de plano parametrico a cartesiano", "Plano por dos rectas"],
            "detalles": ["n es perpendicular a u y a v."]
        },
        {
            "nombre": "Plano con punto y normal",
            "formula": "n · (X - P0) = 0",
            "uso": "Construir la ecuacion cartesiana de un plano.",
            "cuando_usarla": ["Tienes un punto y un normal", "Plano perpendicular a una recta"],
            "detalles": ["Si n=(a,b,c), queda a(x-x0)+b(y-y0)+c(z-z0)=0."]
        },
        {
            "nombre": "Distancia punto-plano",
            "formula": "d(P,pi)=|a*x0+b*y0+c*z0-d|/sqrt(a^2+b^2+c^2)",
            "uso": "Medir la distancia minima de un punto a un plano.",
            "cuando_usarla": ["Plano ax+by+cz=d", "Proyeccion sobre plano"],
            "detalles": ["Se usa el normal porque la distancia minima es perpendicular al plano."]
        },
        {
            "nombre": "Proyeccion sobre un vector",
            "formula": "proy_u(v) = (v·u / ||u||^2) u",
            "uso": "Separar componente paralela y perpendicular.",
            "cuando_usarla": ["Distancia punto-recta", "Proyeccion punto-recta"],
            "detalles": ["La componente perpendicular es v - proy_u(v)."]
        },
        {
            "nombre": "Distancia punto-recta",
            "formula": "d(P,r)=||P0P - proy_u(P0P)||",
            "uso": "Medir la distancia minima de un punto a una recta.",
            "cuando_usarla": ["Recta con punto P0 y director u"],
            "detalles": ["Se usa el director porque la recta avanza en esa direccion."]
        },
        {
            "nombre": "Distancia punto-recta con producto vectorial",
            "formula": "d(P,r)=||P0P x u||/||u||",
            "uso": "Formula rapida en R3.",
            "cuando_usarla": ["Distancia punto-recta en R3 usual"],
            "detalles": ["Es area del paralelogramo dividida por la base."]
        },
        {
            "nombre": "Distancia entre rectas cruzadas",
            "formula": "d(r,s)=|P_rP_s · (u_r x u_s)|/||u_r x u_s||",
            "uso": "Medir distancia minima entre rectas que se cruzan.",
            "cuando_usarla": ["Rectas no paralelas y sin corte en R3"],
            "detalles": ["u_r x u_s es perpendicular a ambas rectas."]
        },
        {
            "nombre": "Angulo entre rectas",
            "formula": "cos(alpha)=|u_r·u_s|/(||u_r|| ||u_s||)",
            "uso": "Calcular angulo de corte o cruce.",
            "cuando_usarla": ["Dos rectas con directores conocidos"],
            "detalles": ["Se suele tomar valor absoluto para el angulo agudo."]
        },
        {
            "nombre": "Angulo entre planos",
            "formula": "cos(alpha)=|n_1·n_2|/(||n_1|| ||n_2||)",
            "uso": "Calcular angulo entre planos.",
            "cuando_usarla": ["Planos en forma cartesiana"],
            "detalles": ["Se usan normales, no directores."]
        },
        {
            "nombre": "Angulo entre recta y plano",
            "formula": "sin(alpha)=|u·n|/(||u|| ||n||)",
            "uso": "Calcular angulo entre recta y plano.",
            "cuando_usarla": ["Recta con director u y plano con normal n"],
            "detalles": ["Equivale a alpha=90°-beta, donde beta es el angulo entre u y n."]
        },
        {
            "nombre": "Criterio de rangos",
            "formula": "rg(A), rg(A|b), dim solucion = n-rg(A)",
            "uso": "Estudiar intersecciones y posiciones relativas.",
            "cuando_usarla": ["Sistemas de planos", "Recta-plano", "Recta-recta en cartesianas"],
            "detalles": ["Si rg(A)!=rg(A|b), no hay solucion."]
        },
        {
            "nombre": "Cambio de referencia afin",
            "formula": "coords_nuevas = M^{-1}(coords_antiguas(P)-coords_antiguas(O'))",
            "uso": "Cambiar coordenadas de un punto a otra referencia.",
            "cuando_usarla": ["Cambio de sistema de referencia afin"],
            "detalles": ["M tiene como columnas los vectores de la nueva base expresados en la base antigua."]
        }
    ],

    "metodos": [
        {
            "nombre": "Identificar una recta en parametricas",
            "objetivo": "Sacar punto de paso y vector director.",
            "pasos": [
                "Busca los terminos independientes: forman el punto P0.",
                "Busca los coeficientes del parametro: forman el vector director u.",
                "Escribe P=P0+lambda*u.",
                "Usa u para paralelismo, angulos y distancias."
            ],
            "errores_comunes": ["Confundir punto con vector director."]
        },
        {
            "nombre": "Identificar un plano en parametricas",
            "objetivo": "Sacar punto y dos vectores directores.",
            "pasos": [
                "Los terminos independientes forman P0.",
                "Los coeficientes de lambda forman u.",
                "Los coeficientes de mu forman v.",
                "Comprueba que u y v sean independientes.",
                "Si necesitas normal, calcula n=u x v."
            ],
            "errores_comunes": ["Usar solo un vector director para el plano."]
        },
        {
            "nombre": "Pasar plano de parametricas a cartesianas",
            "objetivo": "Obtener ax+by+cz=d.",
            "pasos": [
                "Lee P0, u y v.",
                "Calcula n=u x v.",
                "Escribe n·(X-P0)=0.",
                "Desarrolla la ecuacion.",
                "Comprueba sustituyendo P0."
            ],
            "errores_comunes": ["Usar un director como si fuera normal."]
        },
        {
            "nombre": "Pasar plano cartesiano a parametricas",
            "objetivo": "Obtener punto y dos directores.",
            "pasos": [
                "De ax+by+cz=d identifica n=(a,b,c).",
                "Encuentra un punto P0 que satisfaga la ecuacion.",
                "Resuelve ax+by+cz=0 para obtener W.",
                "Extrae dos vectores independientes u,v de W.",
                "Escribe P=P0+lambda*u+mu*v."
            ],
            "errores_comunes": ["Elegir un punto que no esta en el plano."]
        },
        {
            "nombre": "Posicion relativa con rangos",
            "objetivo": "Decidir corte, vacio y dimension de la interseccion.",
            "pasos": [
                "Monta el sistema conjunto Ax=b.",
                "Reduce A y la ampliada (A|b).",
                "Compara rg(A) y rg(A|b).",
                "Si son distintos, no hay interseccion.",
                "Si son iguales, dimension del corte = n-rg(A).",
                "Interpreta: 0 punto, 1 recta, 2 plano."
            ],
            "errores_comunes": ["No interpretar la dimension final."]
        },
        {
            "nombre": "Posicion relativa de dos rectas en R3",
            "objetivo": "Clasificar dos rectas.",
            "pasos": [
                "Obtén punto y vector director de cada recta.",
                "Si los directores son proporcionales, son paralelas o coincidentes.",
                "Comprueba si un punto de una recta pertenece a la otra.",
                "Si no son proporcionales, resuelve el sistema conjunto.",
                "Si hay solucion, se cortan; si no, se cruzan."
            ],
            "errores_comunes": ["Creer que dos rectas no paralelas en R3 siempre se cortan."]
        },
        {
            "nombre": "Posicion relativa de dos planos",
            "objetivo": "Clasificar dos planos en R3.",
            "pasos": [
                "Obtén normales n1 y n2.",
                "Si son proporcionales, los planos son paralelos o coincidentes.",
                "Comprueba un punto para distinguir.",
                "Si no son proporcionales, se cortan en una recta.",
                "El director de la recta de corte es n1 x n2."
            ],
            "errores_comunes": ["Decir que dos planos se cortan en un punto."]
        },
        {
            "nombre": "Posicion relativa recta-plano",
            "objetivo": "Clasificar recta y plano.",
            "pasos": [
                "Obtén director u de la recta y normal n del plano.",
                "Calcula u·n.",
                "Si u·n != 0, corta en un punto.",
                "Si u·n = 0, es paralela o contenida.",
                "Sustituye un punto de la recta en el plano para distinguir."
            ],
            "errores_comunes": ["Pensar que u·n=0 significa perpendicular al plano."]
        },
        {
            "nombre": "Distancia punto-recta",
            "objetivo": "Calcular distancia minima y proyeccion.",
            "pasos": [
                "Lee P0 de la recta y director u.",
                "Forma v=P0P.",
                "Calcula proy_u(v).",
                "Componente perpendicular: v_perp=v-proy_u(v).",
                "Distancia: ||v_perp||.",
                "Punto proyectado: P0+proy_u(v)."
            ],
            "errores_comunes": ["Olvidar que la distancia es perpendicular a la recta."]
        },
        {
            "nombre": "Distancia punto-plano",
            "objetivo": "Calcular distancia minima a un plano.",
            "pasos": [
                "Pon el plano como ax+by+cz=d.",
                "Identifica n=(a,b,c).",
                "Sustituye P en ax+by+cz-d.",
                "Toma valor absoluto.",
                "Divide por ||n||."
            ],
            "errores_comunes": ["Olvidar el valor absoluto."]
        },
        {
            "nombre": "Distancia entre rectas que se cruzan",
            "objetivo": "Calcular distancia minima entre rectas no coplanarias.",
            "pasos": [
                "Obtén P_r, u_r y P_s, u_s.",
                "Calcula n=u_r x u_s.",
                "Forma P_rP_s.",
                "Calcula |P_rP_s·n|/||n||."
            ],
            "errores_comunes": ["Usar esta formula para rectas paralelas."]
        },
        {
            "nombre": "Cambio de referencia afin",
            "objetivo": "Cambiar coordenadas de un punto.",
            "pasos": [
                "Escribe P y O' en la referencia antigua.",
                "Calcula P-O'.",
                "Construye M con la nueva base como columnas.",
                "Resuelve M*c=P-O'.",
                "c son las coordenadas de P en la nueva referencia."
            ],
            "errores_comunes": [
                "Olvidar restar el nuevo origen.",
                "Poner la base nueva como filas."
            ]
        },
        {
            "nombre": "Puntos alineados",
            "objetivo": "Decidir si tres puntos estan en una misma recta.",
            "pasos": [
                "Calcula AB y AC.",
                "Comprueba si AB y AC son proporcionales.",
                "Si hay parametro, iguala proporciones.",
                "Con el valor valido, la recta es A+lambda*AB."
            ],
            "errores_comunes": ["Usar puntos directamente sin restar."]
        },
        {
            "nombre": "Plano que contiene una recta y un punto",
            "objetivo": "Construir un plano.",
            "pasos": [
                "Toma P0 y u de la recta.",
                "Forma P0P hacia el punto exterior.",
                "Si P0P no es proporcional a u, ambos generan el plano.",
                "Calcula n=u x P0P.",
                "Escribe n·(X-P0)=0."
            ],
            "errores_comunes": ["Si el punto esta en la recta, no hay plano unico."]
        }
    ],

    "flashcards": [
        {"id": "alg3_fc_01", "frente": "¿Que diferencia hay entre punto y vector?", "reverso": "Un punto es posicion; un vector es desplazamiento entre puntos.", "categoria": "Espacio afin"},
        {"id": "alg3_fc_02", "frente": "¿Como se obtiene AB?", "reverso": "AB=B-A.", "categoria": "Vectores"},
        {"id": "alg3_fc_03", "frente": "¿Que es una variedad afin?", "reverso": "L=P0+W, con P0 punto y W subespacio direccion.", "categoria": "Variedades afines"},
        {"id": "alg3_fc_04", "frente": "¿Dimension de L=P0+W?", "reverso": "dim(L)=dim(W).", "categoria": "Variedades afines"},
        {"id": "alg3_fc_05", "frente": "¿Que necesitas para una recta?", "reverso": "Un punto y un vector director.", "categoria": "Rectas"},
        {"id": "alg3_fc_06", "frente": "¿Que necesitas para un plano parametrico?", "reverso": "Un punto y dos vectores directores independientes.", "categoria": "Planos"},
        {"id": "alg3_fc_07", "frente": "Si pi: ax+by+cz=d, ¿cual es el normal?", "reverso": "n=(a,b,c).", "categoria": "Planos"},
        {"id": "alg3_fc_08", "frente": "¿Por que se usa el normal para distancia punto-plano?", "reverso": "Porque la distancia minima es perpendicular al plano.", "categoria": "Distancias"},
        {"id": "alg3_fc_09", "frente": "¿Por que se usa el director para distancia punto-recta?", "reverso": "Porque se proyecta sobre la direccion de la recta.", "categoria": "Distancias"},
        {"id": "alg3_fc_10", "frente": "¿Que significa rg(A)!=rg(A|b)?", "reverso": "Sistema incompatible: no hay interseccion.", "categoria": "Rangos"},
        {"id": "alg3_fc_11", "frente": "¿Que son rectas cruzadas?", "reverso": "Rectas no paralelas que no se cortan en R3.", "categoria": "Posicion relativa"},
        {"id": "alg3_fc_12", "frente": "¿Angulo entre planos?", "reverso": "Se calcula con sus normales.", "categoria": "Angulos"},
        {"id": "alg3_fc_13", "frente": "¿Angulo entre rectas?", "reverso": "Se calcula con sus directores.", "categoria": "Angulos"},
        {"id": "alg3_fc_14", "frente": "¿Que cambia en un cambio de referencia afin?", "reverso": "Cambia el origen y puede cambiar la base.", "categoria": "Cambio de referencia"}
    ],

    "preguntas_vf": [
        {"id": "alg3_vf_01", "pregunta": "En un espacio afin, la resta de dos puntos da un vector.", "respuesta": True, "explicacion": "AB representa el desplazamiento desde A hasta B.", "categoria": "Espacio afin", "dificultad": "facil"},
        {"id": "alg3_vf_02", "pregunta": "Una recta en R3 queda determinada por un punto y un vector normal.", "respuesta": False, "explicacion": "Una recta se determina por un punto y un vector director.", "categoria": "Rectas", "dificultad": "facil"},
        {"id": "alg3_vf_03", "pregunta": "Un plano ax+by+cz=d tiene normal n=(a,b,c).", "respuesta": True, "explicacion": "Los coeficientes de x,y,z dan el normal.", "categoria": "Planos", "dificultad": "facil"},
        {"id": "alg3_vf_04", "pregunta": "Si dos rectas en R3 no son paralelas, necesariamente se cortan.", "respuesta": False, "explicacion": "Pueden cruzarse.", "categoria": "Posicion relativa", "dificultad": "media"},
        {"id": "alg3_vf_05", "pregunta": "Si rg(A)!=rg(A|b), el sistema no tiene solucion.", "respuesta": True, "explicacion": "Es sistema incompatible.", "categoria": "Rangos", "dificultad": "facil"},
        {"id": "alg3_vf_06", "pregunta": "La dimension de L=P0+W es dim(W).", "respuesta": True, "explicacion": "La direccion determina la dimension.", "categoria": "Variedades afines", "dificultad": "facil"},
        {"id": "alg3_vf_07", "pregunta": "Para distancia punto-plano se usa el vector director del plano.", "respuesta": False, "explicacion": "Se usa el vector normal.", "categoria": "Distancias", "dificultad": "media"},
        {"id": "alg3_vf_08", "pregunta": "Dos planos no paralelos en R3 se cortan en una recta.", "respuesta": True, "explicacion": "La interseccion de dos planos secantes es una recta.", "categoria": "Planos", "dificultad": "facil"},
        {"id": "alg3_vf_09", "pregunta": "En cambio de referencia afin solo cambia la base, nunca el origen.", "respuesta": False, "explicacion": "Puede cambiar el origen y la base.", "categoria": "Cambio de referencia", "dificultad": "media"},
        {"id": "alg3_vf_10", "pregunta": "En R4, un hiperplano tiene dimension 3.", "respuesta": True, "explicacion": "Un hiperplano tiene dimension n-1.", "categoria": "Hiperplanos", "dificultad": "facil"}
    ],

    "preguntas_mc": [
        {"id": "alg3_mc_01", "pregunta": "¿Que necesitas para escribir r: P=P0+lambda*u?", "opciones": ["Dos normales", "Un punto y un vector director", "Un punto y dos directores", "Solo un punto"], "respuesta": 2, "explicacion": "Una recta se determina por punto y direccion.", "categoria": "Rectas", "dificultad": "facil"},
        {"id": "alg3_mc_02", "pregunta": "Si pi: 2x-3y+z=1, ¿cual es un normal?", "opciones": ["(2,-3,1)", "(1,1,1)", "(-3,1,2)", "(2,3,1)"], "respuesta": 1, "explicacion": "El normal usa los coeficientes.", "categoria": "Planos", "dificultad": "facil"},
        {"id": "alg3_mc_03", "pregunta": "Si r tiene director u y pi normal n, ¿cuando r es paralela a pi?", "opciones": ["u·n=0", "u=n", "u·n=1", "n=0"], "respuesta": 1, "explicacion": "La direccion de la recta esta dentro/paralela al plano.", "categoria": "Recta-plano", "dificultad": "media"},
        {"id": "alg3_mc_04", "pregunta": "Para distancia punto-plano se usa:", "opciones": ["Vector normal", "Cualquier vector", "Parametros", "Vector entre puntos"], "respuesta": 1, "explicacion": "La distancia minima va perpendicular al plano.", "categoria": "Distancias", "dificultad": "facil"},
        {"id": "alg3_mc_05", "pregunta": "Si rg(A)=rg(A|b)=2 en R3, la solucion tiene dimension:", "opciones": ["0", "1", "2", "3"], "respuesta": 2, "explicacion": "Dimension=3-2=1.", "categoria": "Rangos", "dificultad": "media"},
        {"id": "alg3_mc_06", "pregunta": "Dos rectas con directores proporcionales pueden ser:", "opciones": ["Secantes o cruzadas", "Paralelas o coincidentes", "Siempre cruzadas", "Siempre secantes"], "respuesta": 2, "explicacion": "Comparten direccion.", "categoria": "Posicion relativa", "dificultad": "facil"},
        {"id": "alg3_mc_07", "pregunta": "El angulo entre dos rectas se calcula con:", "opciones": ["Directores", "Puntos", "Normales", "Terminos independientes"], "respuesta": 1, "explicacion": "Las rectas tienen direcciones.", "categoria": "Angulos", "dificultad": "facil"},
        {"id": "alg3_mc_08", "pregunta": "El angulo entre dos planos se calcula con:", "opciones": ["Puntos", "Normales", "Parametros", "Distancias"], "respuesta": 2, "explicacion": "Los normales dan la inclinacion.", "categoria": "Angulos", "dificultad": "facil"},
        {"id": "alg3_mc_09", "pregunta": "En cambio de referencia afin:", "opciones": ["Corriges origen y cambias base", "Solo cambias base", "Solo sumas el origen", "Usas P^tAP"], "respuesta": 1, "explicacion": "Es afin, por eso el origen importa.", "categoria": "Cambio de referencia", "dificultad": "dificil"},
        {"id": "alg3_mc_10", "pregunta": "Para pasar plano parametrico a cartesiano en R3 conviene calcular:", "opciones": ["n=u x v", "u+v", "P0+u+v", "det(P0)"], "respuesta": 1, "explicacion": "El producto vectorial da el normal.", "categoria": "Planos", "dificultad": "media"}
    ],

    "ejercicios_guiados": [
        {
            "id": "alg3_ej_01",
            "enunciado": "Dada r: x=2-lambda, y=1, z=-1+2lambda, identifica punto y vector director.",
            "categoria": "Rectas",
            "dificultad": "facil",
            "solucion": ["Punto P0=(2,1,-1).", "Vector director u=(-1,0,2).", "Forma vectorial: P=P0+lambda*u."]
        },
        {
            "id": "alg3_ej_02",
            "enunciado": "Dado pi: x=1+lambda+mu, y=-2+lambda-mu, z=2+2mu, halla normal y cartesiana.",
            "categoria": "Planos",
            "dificultad": "media",
            "solucion": ["P0=(1,-2,2).", "u=(1,1,0), v=(1,-1,2).", "n=u x v=(2,-2,-2), proporcional a (1,-1,-1).", "n·(X-P0)=0.", "x-y-z=1."]
        },
        {
            "id": "alg3_ej_03",
            "enunciado": "Estudia pi1: 2x-3y+z=1 y pi2: 2x-3y+z=-2.",
            "categoria": "Posicion relativa",
            "dificultad": "facil",
            "solucion": ["Los normales son iguales.", "Son paralelos o coincidentes.", "Los terminos independientes son distintos.", "Conclusion: paralelos distintos."]
        },
        {
            "id": "alg3_ej_04",
            "enunciado": "Calcula distancia de P=(1,1,1) al plano x+y+z=0.",
            "categoria": "Distancia punto-plano",
            "dificultad": "facil",
            "solucion": ["n=(1,1,1).", "d=|1+1+1|/sqrt(3)=3/sqrt(3)=sqrt(3)."]
        },
        {
            "id": "alg3_ej_05",
            "enunciado": "Proyecta P=(1,1,1) sobre r con P0=(1,-1,-2), u=(1,2,2).",
            "categoria": "Proyeccion punto-recta",
            "dificultad": "media",
            "solucion": ["v=P-P0=(0,2,3).", "v·u=10.", "||u||^2=9.", "proy_u(v)=(10/9)u.", "P proyectado=P0+(10/9)u=(19/9,11/9,2/9)."]
        },
        {
            "id": "alg3_ej_06",
            "enunciado": "Dos rectas tienen directores u=(1,0,2) y v=(2,0,4). ¿Que puedes decir?",
            "categoria": "Posicion relativa",
            "dificultad": "facil",
            "solucion": ["v=2u.", "Los directores son proporcionales.", "Las rectas son paralelas o coincidentes.", "Comprueba un punto para distinguir."]
        },
        {
            "id": "alg3_ej_07",
            "enunciado": "Si u=(1,2,1) y n=(2,-1,0), decide si la recta es paralela al plano.",
            "categoria": "Recta-plano",
            "dificultad": "media",
            "solucion": ["u·n=1*2+2*(-1)+1*0=0.", "La recta es paralela al plano o contenida.", "Sustituye un punto de la recta para distinguir."]
        },
        {
            "id": "alg3_ej_08",
            "enunciado": "A=(1,2,-3), B=(4,a,1), C=(7,0,5). Halla a para que esten alineados.",
            "categoria": "Puntos alineados",
            "dificultad": "media",
            "solucion": ["AB=(3,a-2,4).", "AC=(6,-2,8).", "AC=2*AB exige -2=2(a-2).", "a=1.", "Director para la recta: (3,-1,4)."]
        },
        {
            "id": "alg3_ej_09",
            "enunciado": "Si tres planos en R3 dan rg(A)=rg(A|b)=2, ¿que es la interseccion?",
            "categoria": "Rangos",
            "dificultad": "media",
            "solucion": ["Sistema compatible.", "Dimension=3-2=1.", "La interseccion es una recta."]
        },
        {
            "id": "alg3_ej_10",
            "enunciado": "Construye el plano que pasa por P=(1,0,2) y es paralelo a u=(1,1,0), v=(0,1,1).",
            "categoria": "Planos",
            "dificultad": "media",
            "solucion": ["P0=(1,0,2).", "n=u x v=(1,-1,1).", "n·(X-P0)=0.", "x-y+z=3."]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "puntos alineados",
            "que_significa": "Varios puntos deben pertenecer a una misma recta.",
            "que_suele_pedir": ["Valores de parametros", "Recta que contiene los puntos"],
            "operaciones_recomendadas": ["Calcula AB y AC.", "Impone que sean proporcionales.", "Construye la recta con punto y director."],
            "pista_examen": "Alineacion se comprueba con vectores entre puntos, no con puntos sueltos."
        },
        {
            "palabra_clave": "recta",
            "que_significa": "Variedad afin de dimension 1.",
            "que_suele_pedir": ["Punto de paso", "Vector director", "Distancia", "Angulo", "Posicion relativa"],
            "operaciones_recomendadas": ["Busca P0.", "Busca u.", "Si viene como interseccion de planos, usa u=n1 x n2."],
            "pista_examen": "Con rectas, casi todo gira alrededor del vector director."
        },
        {
            "palabra_clave": "plano",
            "que_significa": "Variedad afin de dimension 2 en R3.",
            "que_suele_pedir": ["Normal", "Directores", "Cartesiana", "Distancia", "Angulo"],
            "operaciones_recomendadas": ["Si es ax+by+cz=d, normal=(a,b,c).", "Si es parametrico, normal=u x v."],
            "pista_examen": "Con planos cartesianos, lo principal es el normal."
        },
        {
            "palabra_clave": "posicion relativa",
            "que_significa": "Clasificar como se colocan rectas/planos/variedades.",
            "que_suele_pedir": ["Paralelismo", "Corte", "Coincidencia", "Cruce"],
            "operaciones_recomendadas": ["Identifica objetos.", "Usa directores para rectas y normales para planos.", "Monta sistemas y compara rangos."],
            "pista_examen": "Si ves muchos rangos, el problema quiere posicion relativa."
        },
        {
            "palabra_clave": "distancia a una recta",
            "que_significa": "Menor distancia hasta una recta.",
            "que_suele_pedir": ["Distancia", "Proyeccion", "Punto mas cercano"],
            "operaciones_recomendadas": ["Usa el vector director.", "Proyecta P0P sobre u.", "Toma la componente perpendicular."],
            "pista_examen": "Recta = vector director."
        },
        {
            "palabra_clave": "distancia a un plano",
            "que_significa": "Menor distancia hasta un plano.",
            "que_suele_pedir": ["Distancia", "Proyeccion", "Plano paralelo a distancia dada"],
            "operaciones_recomendadas": ["Pon el plano en cartesiana.", "Identifica el normal.", "Usa la formula con valor absoluto."],
            "pista_examen": "Plano = vector normal."
        },
        {
            "palabra_clave": "angulo entre rectas",
            "que_significa": "Angulo entre sus direcciones.",
            "que_suele_pedir": ["Angulo de corte", "Angulo de cruce", "Perpendicularidad"],
            "operaciones_recomendadas": ["Obtén directores u y v.", "Usa cos(alpha)=|u·v|/(||u||||v||)."],
            "pista_examen": "Para rectas, usa directores."
        },
        {
            "palabra_clave": "angulo entre planos",
            "que_significa": "Angulo entre sus inclinaciones.",
            "que_suele_pedir": ["Angulo de corte", "Paralelismo", "Perpendicularidad"],
            "operaciones_recomendadas": ["Obtén normales n1,n2.", "Usa cos(alpha)=|n1·n2|/(||n1||||n2||)."],
            "pista_examen": "Para planos, usa normales."
        },
        {
            "palabra_clave": "recta perpendicular a un plano",
            "que_significa": "La direccion de la recta es el normal del plano.",
            "que_suele_pedir": ["Recta por un punto perpendicular a plano", "Proyeccion punto-plano"],
            "operaciones_recomendadas": ["Obtén n.", "Usa r: X=P+lambda*n."],
            "pista_examen": "Perpendicular a plano = paralelo al normal."
        },
        {
            "palabra_clave": "recta paralela a un plano",
            "que_significa": "La direccion de la recta esta dentro/paralela al plano.",
            "que_suele_pedir": ["Distinguir contenida o paralela exterior"],
            "operaciones_recomendadas": ["Calcula u·n.", "Si u·n=0, sustituye un punto en el plano."],
            "pista_examen": "u·n=0 significa paralela al plano, no perpendicular."
        },
        {
            "palabra_clave": "cambio de referencia afin",
            "que_significa": "Coordenadas del mismo punto en otro sistema.",
            "que_suele_pedir": ["Coordenadas de P en S'", "Cambio de origen y base"],
            "operaciones_recomendadas": ["Calcula P-O'.", "Construye M con la nueva base.", "Resuelve M*c=P-O'."],
            "pista_examen": "En afin, no olvides el origen."
        },
        {
            "palabra_clave": "lugar geometrico",
            "que_significa": "Todos los puntos que cumplen una condicion.",
            "que_suele_pedir": ["Ecuacion F(x,y,z)=0", "Decidir si es plano o superficie"],
            "operaciones_recomendadas": ["Pon P=(x,y,z).", "Traduce distancias o condiciones a ecuaciones.", "Simplifica."],
            "pista_examen": "Lineal suele ser plano; cuadratica suele ser superficie."
        }
    ]
}
