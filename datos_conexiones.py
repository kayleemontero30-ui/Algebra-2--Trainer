# -*- coding: utf-8 -*-

CONEXIONES = [
    {
        "titulo": "Tema 1 -> Tema 2: producto escalar como forma bilineal",
        "explicacion": """
Un producto escalar es una forma bilineal simetrica definida positiva.
Por eso aparecen matriz asociada, cambio de base por congruencia y criterio de Sylvester.
""",
        "ejemplo": "Si G es simetrica y definida positiva, entonces <x,y>=x^tGy define un producto escalar."
    },
    {
        "titulo": "Tema 2 -> Tema 3: espacio afin euclideo",
        "explicacion": """
Tema 3 usa el producto escalar para medir en espacios afines:
distancia, angulo, ortogonalidad y proyeccion.
""",
        "ejemplo": "d(A,B)=||AB|| usa la norma del Tema 2 aplicada al vector AB."
    },
    {
        "titulo": "Puntos vs vectores",
        "explicacion": """
En Tema 3 aparecen puntos. Regla mental:
- Punto: posicion.
- Vector: desplazamiento.
- B-A = vector AB.
- A + vector = otro punto.
""",
        "ejemplo": "La recta por A y B usa punto A y director AB=B-A."
    },
    {
        "titulo": "Rectas y planos: directores vs normales",
        "explicacion": """
Recta: lo importante suele ser el vector director.
Plano cartesiano: lo importante suele ser el vector normal.

Por eso:
- Punto-recta: proyectas sobre el director.
- Punto-plano: usas el normal.
""",
        "ejemplo": "Si pi: ax+by+cz=d, el normal es n=(a,b,c)."
    },
    {
        "titulo": "Rangos y posiciones relativas",
        "explicacion": """
Las intersecciones se estudian con Ax=b:
- rg(A)!=rg(A|b): no hay solucion.
- rg(A)=rg(A|b): hay solucion.
- dimension = n-rg(A).
""",
        "ejemplo": "En R3, rg(A)=rg(A|b)=2 implica interseccion recta."
    },
    {
        "titulo": "Congruencia vs semejanza vs referencia afin",
        "explicacion": """
- Formas bilineales/cuadraticas/Gram: P^tAP.
- Endomorfismos: P^{-1}AP.
- Puntos en referencia afin: corriges origen y cambias base.
""",
        "ejemplo": "coords nuevas = M^{-1}(P - O')."
    },
    {
        "titulo": "Gram-Schmidt y proyecciones en geometria afin",
        "explicacion": """
Las proyecciones del Tema 2 se vuelven geometricas en Tema 3:
proyectar puntos sobre rectas/planos y hallar distancias minimas.
""",
        "ejemplo": "Para proyectar P sobre una recta r, proyectas P0P sobre el director de r."
    }
]
