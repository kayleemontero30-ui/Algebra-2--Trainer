# -*- coding: utf-8 -*-

CONEXIONES = [
    {
        "titulo": "Tema 1 -> Tema 2: forma bilineal simetrica definida positiva",
        "explicacion": """
En el Tema 1 estudiaste formas bilineales y formas cuadraticas. En el Tema 2 aparece
un caso especial muy importante: el producto escalar.

Un producto escalar es una forma bilineal simetrica definida positiva. Por eso muchas
ideas del Tema 1 vuelven aqui:
- matriz asociada,
- cambio de base por congruencia,
- matriz simetrica,
- definida positiva,
- criterio de Sylvester.
""",
        "ejemplo": "Si G es simetrica y definida positiva, entonces <x,y>=x^tGy define un producto escalar."
    },
    {
        "titulo": "Congruencia vs semejanza",
        "explicacion": """
Esta es una de las confusiones mas importantes:

- Para formas bilineales, formas cuadraticas y matrices de Gram:
  G_nueva = P^t G_antigua P

- Para endomorfismos y matrices de aplicaciones lineales:
  D = P^{-1} A P

En Tema 2 se usan ambas cosas:
- La matriz de Gram cambia por congruencia.
- Una matriz real simetrica puede diagonalizarse ortogonalmente por semejanza.
""",
        "ejemplo": "Si Q es ortogonal, entonces Q^{-1}=Q^t, y la semejanza ortogonal se escribe D=Q^tAQ."
    },
    {
        "titulo": "Forma cuadratica y norma",
        "explicacion": """
En Tema 1 una forma cuadratica era phi(x)=x^tMx. En Tema 2, si M=G es una matriz
de Gram de un producto escalar, entonces:

phi(x)=<x,x>=x^tGx

y la norma inducida es:

||x||=sqrt(phi(x))

Por eso el producto escalar genera una forma cuadratica definida positiva.
""",
        "ejemplo": "Si G=I, entonces ||x||=sqrt(x1^2+...+xn^2)."
    },
    {
        "titulo": "Nucleo, imagen y rango dentro del complemento ortogonal",
        "explicacion": """
Cuando calculas U_perp, acabas resolviendo un sistema lineal homogeneo.
Eso es exactamente la idea de nucleo de Algebra I.

Si U=lin{u1,...,ur}, entonces y pertenece a U_perp si:

<u1,y>=0, ..., <ur,y>=0

Eso se convierte en Ay=0. Por tanto U_perp es el nucleo de una matriz construida
con las ecuaciones de ortogonalidad.
""",
        "ejemplo": "En R3 usual, si U=lin{(1,2,-3)}, entonces U_perp se obtiene de x+2y-3z=0."
    },
    {
        "titulo": "Gram-Schmidt y proyeccion ortogonal",
        "explicacion": """
Gram-Schmidt funciona restando proyecciones. Para construir un vector nuevo ortogonal,
le quitas al vector original sus componentes paralelas a los vectores anteriores.

Por eso la formula:

o2 = b2 - proy_o1(b2)

es la misma idea que:

componente_perpendicular = x - p_U(x)
""",
        "ejemplo": "o2=b2-(<b2,o1>/||o1||^2)o1."
    },
    {
        "titulo": "Bases ortogonales y coeficientes de Fourier",
        "explicacion": """
En una base cualquiera, calcular coordenadas puede requerir resolver un sistema.
Pero en una base ortogonal las coordenadas salen directamente con productos escalares:

coord_i = <x,e_i>/||e_i||^2

Si la base es ortonormal:

coord_i = <x,e_i>

Eso se parece mucho a proyectar x sobre cada direccion de la base.
""",
        "ejemplo": "x=sum((<x,e_i>/||e_i||^2)e_i)."
    }
]