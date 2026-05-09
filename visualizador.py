# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# UTILIDADES BASICAS
# ============================================================

def convertir_vector(texto):
    """
    Convierte texto tipo '1,2,3' en np.array([1,2,3]).
    """
    partes = texto.replace(";", ",").split(",")

    if len(partes) != 3:
        raise ValueError("Debes escribir 3 coordenadas separadas por comas. Ejemplo: 1,2,3")

    try:
        return np.array([float(p.strip()) for p in partes], dtype=float)
    except ValueError:
        raise ValueError("Las coordenadas deben ser numeros. Ejemplo: 1,2,3")


def convertir_numero(texto):
    try:
        return float(texto.strip())
    except ValueError:
        raise ValueError("Debes escribir un numero. Ejemplo: 3 o -2.5")


def norma(v):
    return np.linalg.norm(v)


def vector_unitario(v):
    if norma(v) == 0:
        raise ValueError("No se puede normalizar el vector cero.")
    return v / norma(v)


def son_proporcionales(u, v, tol=1e-9):
    """
    Comprueba si dos vectores son proporcionales usando rango.
    """
    if norma(u) == 0 or norma(v) == 0:
        return False

    matriz = np.vstack([u, v])
    return np.linalg.matrix_rank(matriz, tol=tol) == 1


def configurar_ejes(ax):
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.grid(True)

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_zlim(-6, 6)

    try:
        ax.set_box_aspect([1, 1, 1])
    except Exception:
        pass

    # Ejes principales
    ax.quiver(0, 0, 0, 5, 0, 0, arrow_length_ratio=0.05, linewidth=0.8)
    ax.quiver(0, 0, 0, 0, 5, 0, arrow_length_ratio=0.05, linewidth=0.8)
    ax.quiver(0, 0, 0, 0, 0, 5, arrow_length_ratio=0.05, linewidth=0.8)

    ax.text(5.2, 0, 0, "x")
    ax.text(0, 5.2, 0, "y")
    ax.text(0, 0, 5.2, "z")


def crear_figura(titulo):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_title(titulo)
    configurar_ejes(ax)
    return fig, ax


# ============================================================
# DIBUJO DE OBJETOS
# ============================================================

def dibujar_punto(ax, p, nombre="P", tamano=60):
    ax.scatter(p[0], p[1], p[2], s=tamano)
    ax.text(p[0], p[1], p[2], f" {nombre}")


def dibujar_vector(ax, origen, v, nombre="v", grosor=2):
    ax.quiver(
        origen[0], origen[1], origen[2],
        v[0], v[1], v[2],
        arrow_length_ratio=0.1,
        linewidth=grosor
    )
    extremo = origen + v
    ax.text(extremo[0], extremo[1], extremo[2], f" {nombre}")


def dibujar_segmento(ax, a, b, nombre=None, estilo="--", grosor=2):
    ax.plot(
        [a[0], b[0]],
        [a[1], b[1]],
        [a[2], b[2]],
        linestyle=estilo,
        linewidth=grosor
    )

    if nombre:
        medio = (a + b) / 2
        ax.text(medio[0], medio[1], medio[2], f" {nombre}")


def dibujar_recta(ax, p0, u, nombre="r"):
    if norma(u) == 0:
        raise ValueError("El vector director de la recta no puede ser cero.")

    lambdas = np.linspace(-5, 5, 100)
    puntos = np.array([p0 + lmb * u for lmb in lambdas])

    ax.plot(puntos[:, 0], puntos[:, 1], puntos[:, 2], linewidth=2)
    dibujar_punto(ax, p0, "P0")
    dibujar_vector(ax, p0, vector_unitario(u), "u")
    ax.text(puntos[-1, 0], puntos[-1, 1], puntos[-1, 2], f" {nombre}")


def punto_en_plano(normal, d):
    """
    Encuentra un punto cualquiera que cumple n·x = d.
    """
    a, b, c = normal

    if abs(a) > 1e-9:
        return np.array([d / a, 0, 0], dtype=float)
    if abs(b) > 1e-9:
        return np.array([0, d / b, 0], dtype=float)
    if abs(c) > 1e-9:
        return np.array([0, 0, d / c], dtype=float)

    raise ValueError("El normal no puede ser cero.")


def dibujar_plano(ax, normal, d, nombre="π"):
    if norma(normal) == 0:
        raise ValueError("El vector normal del plano no puede ser cero.")

    a, b, c = normal

    x_vals = np.linspace(-5, 5, 15)
    y_vals = np.linspace(-5, 5, 15)
    X, Y = np.meshgrid(x_vals, y_vals)

    if abs(c) > 1e-9:
        Z = (d - a * X - b * Y) / c
    elif abs(b) > 1e-9:
        z_vals = np.linspace(-5, 5, 15)
        X, Z = np.meshgrid(x_vals, z_vals)
        Y = (d - a * X - c * Z) / b
    elif abs(a) > 1e-9:
        y_vals = np.linspace(-5, 5, 15)
        z_vals = np.linspace(-5, 5, 15)
        Y, Z = np.meshgrid(y_vals, z_vals)
        X = (d - b * Y - c * Z) / a
    else:
        raise ValueError("Plano no valido.")

    ax.plot_surface(X, Y, Z, alpha=0.35)

    p0 = punto_en_plano(normal, d)
    dibujar_punto(ax, p0, "P0")
    dibujar_vector(ax, p0, vector_unitario(normal), "n")
    ax.text(p0[0], p0[1], p0[2], f" {nombre}")


def dibujar_plano_parametrico(ax, p0, u, v, nombre="π"):
    if norma(u) == 0 or norma(v) == 0:
        raise ValueError("Los vectores directores del plano no pueden ser cero.")

    normal = np.cross(u, v)

    if norma(normal) == 0:
        raise ValueError("Los dos vectores directores del plano deben ser independientes.")

    s_vals = np.linspace(-4, 4, 12)
    t_vals = np.linspace(-4, 4, 12)
    S, T = np.meshgrid(s_vals, t_vals)

    X = p0[0] + S * u[0] + T * v[0]
    Y = p0[1] + S * u[1] + T * v[1]
    Z = p0[2] + S * u[2] + T * v[2]

    ax.plot_surface(X, Y, Z, alpha=0.35)
    dibujar_punto(ax, p0, "P0")
    dibujar_vector(ax, p0, vector_unitario(u), "u")
    dibujar_vector(ax, p0, vector_unitario(v), "v")
    dibujar_vector(ax, p0, vector_unitario(normal), "n")
    ax.text(p0[0], p0[1], p0[2], f" {nombre}")


# ============================================================
# CALCULOS GEOMETRICOS
# ============================================================

def proyeccion_punto_recta(p, p0, u):
    if norma(u) == 0:
        raise ValueError("El vector director de la recta no puede ser cero.")

    v = p - p0
    proy = (np.dot(v, u) / np.dot(u, u)) * u
    pie = p0 + proy
    distancia = norma(p - pie)

    return pie, distancia


def proyeccion_punto_plano(p, normal, d):
    if norma(normal) == 0:
        raise ValueError("El vector normal del plano no puede ser cero.")

    factor = (np.dot(normal, p) - d) / np.dot(normal, normal)
    pie = p - factor * normal
    distancia = norma(p - pie)

    return pie, distancia


def punto_interseccion_recta_plano(p0, u, normal, d):
    denominador = np.dot(normal, u)

    if abs(denominador) < 1e-9:
        return None

    lmb = (d - np.dot(normal, p0)) / denominador
    return p0 + lmb * u


def puntos_cercanos_rectas(p1, u1, p2, u2):
    """
    Para dos rectas r=p1+s*u1 y s=p2+t*u2, calcula puntos cercanos
    por minimos cuadrados.
    """
    if norma(np.cross(u1, u2)) < 1e-9:
        raise ValueError("Las rectas son paralelas o casi paralelas. Esta formula es para rectas que se cruzan.")

    A = np.column_stack((u1, -u2))
    b = p2 - p1

    solucion, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    s, t = solucion

    q1 = p1 + s * u1
    q2 = p2 + t * u2
    distancia = norma(q1 - q2)

    return q1, q2, distancia


# ============================================================
# ESCENAS MANUALES
# ============================================================

def escena_punto_vector(p, v):
    fig, ax = crear_figura("Punto y vector")
    dibujar_punto(ax, p, "P")
    dibujar_vector(ax, p, v, "v")

    explicacion = (
        "PUNTO + VECTOR\n\n"
        "Se dibuja el punto P y el vector v aplicado desde P.\n\n"
        "Recuerda:\n"
        "- Un punto indica posicion.\n"
        "- Un vector indica desplazamiento.\n"
        "- P + v produce otro punto.\n\n"
        "Esto es la base de los espacios afines: no sumamos puntos con puntos, "
        "pero si podemos sumar un vector a un punto."
    )

    return fig, explicacion


def escena_recta(p0, u):
    fig, ax = crear_figura("Recta: P = P0 + λu")
    dibujar_recta(ax, p0, u)

    explicacion = (
        "RECTA\n\n"
        "Una recta se representa como:\n"
        "r: P = P0 + λu\n\n"
        "P0 es un punto de la recta.\n"
        "u es el vector director.\n\n"
        "¿Por que usamos el vector director?\n"
        "Porque indica hacia donde avanza la recta.\n\n"
        "Con el vector director puedes:\n"
        "- calcular angulos entre rectas;\n"
        "- saber si dos rectas son paralelas;\n"
        "- calcular distancia punto-recta;\n"
        "- proyectar puntos sobre la recta."
    )

    return fig, explicacion


def escena_plano(normal, d):
    fig, ax = crear_figura("Plano: ax + by + cz = d")
    dibujar_plano(ax, normal, d)

    explicacion = (
        "PLANO EN CARTESIANAS\n\n"
        "Un plano en forma cartesiana se escribe como:\n"
        "ax + by + cz = d\n\n"
        "El vector normal es:\n"
        "n = (a,b,c)\n\n"
        "¿Por que usamos el normal?\n"
        "Porque es perpendicular al plano.\n\n"
        "Con el vector normal puedes:\n"
        "- calcular distancia punto-plano;\n"
        "- calcular angulo entre planos;\n"
        "- saber si planos son paralelos;\n"
        "- construir rectas perpendiculares al plano."
    )

    return fig, explicacion


def escena_plano_parametrico(p0, u, v):
    fig, ax = crear_figura("Plano parametrico: P = P0 + λu + μv")
    dibujar_plano_parametrico(ax, p0, u, v)

    normal = np.cross(u, v)

    explicacion = (
        "PLANO EN PARAMETRICAS\n\n"
        "Un plano parametrico se escribe como:\n"
        "P = P0 + λu + μv\n\n"
        "P0 es un punto del plano.\n"
        "u y v son vectores directores del plano.\n\n"
        "Para pasar a cartesianas necesitamos un vector normal.\n"
        "Ese normal se calcula con:\n"
        "n = u × v\n\n"
        f"En este ejemplo:\n"
        f"u = {np.round(u, 4)}\n"
        f"v = {np.round(v, 4)}\n"
        f"n = u × v = {np.round(normal, 4)}\n\n"
        "Luego escribes:\n"
        "n · (X - P0) = 0"
    )

    return fig, explicacion


def escena_punto_recta(p, p0, u):
    fig, ax = crear_figura("Proyeccion de punto sobre recta")

    dibujar_recta(ax, p0, u)
    dibujar_punto(ax, p, "P")

    pie, distancia = proyeccion_punto_recta(p, p0, u)

    dibujar_punto(ax, pie, "H")
    dibujar_segmento(ax, p, pie, "distancia")

    explicacion = (
        "DISTANCIA PUNTO-RECTA\n\n"
        "Tenemos un punto P y una recta r.\n\n"
        "La recta tiene:\n"
        "- punto P0;\n"
        "- vector director u.\n\n"
        "Procedimiento:\n"
        "1. Formas el vector P0P.\n"
        "2. Proyectas P0P sobre u.\n"
        "3. Obtienes el punto H sobre la recta.\n"
        "4. La distancia es ||PH||.\n\n"
        f"Pie de perpendicular H = {np.round(pie, 4)}\n"
        f"Distancia aproximada = {distancia:.4f}\n\n"
        "¿Por que usamos el vector director?\n"
        "Porque la recta solo tiene una direccion: u. La distancia minima debe ser "
        "perpendicular a esa direccion."
    )

    return fig, explicacion


def escena_punto_plano(p, normal, d):
    fig, ax = crear_figura("Proyeccion de punto sobre plano")

    dibujar_plano(ax, normal, d)
    dibujar_punto(ax, p, "P")

    pie, distancia = proyeccion_punto_plano(p, normal, d)

    dibujar_punto(ax, pie, "H")
    dibujar_segmento(ax, p, pie, "distancia")

    explicacion = (
        "DISTANCIA PUNTO-PLANO\n\n"
        "Tenemos un punto P y un plano π.\n\n"
        "Si el plano es:\n"
        "ax + by + cz = d\n\n"
        "entonces su normal es:\n"
        "n = (a,b,c)\n\n"
        "Procedimiento:\n"
        "1. Identificas el normal n.\n"
        "2. Bajas desde P en direccion perpendicular al plano.\n"
        "3. Esa direccion perpendicular es la direccion del normal.\n"
        "4. H es el pie de perpendicular.\n\n"
        f"Pie de perpendicular H = {np.round(pie, 4)}\n"
        f"Distancia aproximada = {distancia:.4f}\n\n"
        "Formula directa:\n"
        "d(P,π)=|a*x0+b*y0+c*z0-d|/sqrt(a²+b²+c²)"
    )

    return fig, explicacion


def escena_recta_plano(p0, u, normal, d):
    fig, ax = crear_figura("Recta y plano")

    dibujar_plano(ax, normal, d)
    dibujar_recta(ax, p0, u)

    producto = np.dot(u, normal)
    punto_corte = punto_interseccion_recta_plano(p0, u, normal, d)

    if punto_corte is not None:
        dibujar_punto(ax, punto_corte, "Corte")
        resultado = (
            "Como u·n ≠ 0, la recta corta al plano en un punto.\n"
            f"Punto de corte aproximado = {np.round(punto_corte, 4)}"
        )
    else:
        pertenece = abs(np.dot(normal, p0) - d) < 1e-9

        if pertenece:
            resultado = (
                "Como u·n = 0, la recta es paralela al plano.\n"
                "Ademas, P0 satisface la ecuacion del plano.\n"
                "Entonces la recta esta contenida en el plano."
            )
        else:
            resultado = (
                "Como u·n = 0, la recta es paralela al plano.\n"
                "Pero P0 no satisface la ecuacion del plano.\n"
                "Entonces la recta es paralela exterior al plano."
            )

    explicacion = (
        "POSICION RELATIVA RECTA-PLANO\n\n"
        "Para una recta usamos su vector director u.\n"
        "Para un plano usamos su vector normal n.\n\n"
        "La clave es calcular u·n.\n\n"
        "- Si u·n ≠ 0: la recta corta al plano.\n"
        "- Si u·n = 0: la recta es paralela al plano o esta contenida.\n\n"
        f"En este ejemplo:\n"
        f"u·n = {producto:.4f}\n\n"
        f"{resultado}\n\n"
        "Ojo:\n"
        "u·n = 0 NO significa que la recta sea perpendicular al plano.\n"
        "Significa que la direccion de la recta es paralela al plano."
    )

    return fig, explicacion


def escena_rectas_cruzadas(p1, u1, p2, u2):
    fig, ax = crear_figura("Rectas que se cruzan")

    dibujar_recta(ax, p1, u1, "r")
    dibujar_recta(ax, p2, u2, "s")

    n = np.cross(u1, u2)

    if norma(n) < 1e-9:
        explicacion = (
            "RECTAS PARALELAS\n\n"
            "Los vectores directores son proporcionales.\n"
            "Por tanto las rectas son paralelas o coincidentes.\n\n"
            "Para distinguirlas, comprueba si un punto de una recta pertenece a la otra."
        )
        return fig, explicacion

    q1, q2, distancia = puntos_cercanos_rectas(p1, u1, p2, u2)

    dibujar_punto(ax, q1, "H1")
    dibujar_punto(ax, q2, "H2")
    dibujar_segmento(ax, q1, q2, "distancia")

    explicacion = (
        "RECTAS QUE SE CRUZAN\n\n"
        "En R3, dos rectas pueden no ser paralelas y aun asi no cortarse.\n"
        "A eso le llamamos rectas que se cruzan.\n\n"
        "Para la distancia entre rectas cruzadas usamos:\n"
        "n = u_r × u_s\n\n"
        "¿Por que?\n"
        "Porque u_r × u_s es perpendicular a ambas direcciones.\n\n"
        f"En este ejemplo:\n"
        f"u_r × u_s = {np.round(n, 4)}\n"
        f"Distancia aproximada = {distancia:.4f}\n\n"
        "La distancia minima esta sobre un segmento perpendicular a las dos rectas."
    )

    return fig, explicacion


# ============================================================
# EJEMPLOS GUIADOS
# ============================================================

EJEMPLOS_GUIADOS_VISUALES = {
    "Recta: ver punto y vector director": {
        "tipo": "Recta",
        "datos": {
            "punto_recta": "1,-1,-2",
            "director": "1,2,2"
        }
    },
    "Plano cartesiano: ver vector normal": {
        "tipo": "Plano",
        "datos": {
            "normal": "1,1,1",
            "d": "0"
        }
    },
    "Plano parametrico: directores y normal": {
        "tipo": "Plano parametrico",
        "datos": {
            "punto_recta": "1,0,2",
            "director": "1,1,0",
            "vector": "0,1,1"
        }
    },
    "Distancia punto-recta: usa vector director": {
        "tipo": "Punto + recta",
        "datos": {
            "punto": "1,1,1",
            "punto_recta": "1,-1,-2",
            "director": "1,2,2"
        }
    },
    "Distancia punto-plano: usa vector normal": {
        "tipo": "Punto + plano",
        "datos": {
            "punto": "1,1,1",
            "normal": "1,1,1",
            "d": "0"
        }
    },
    "Recta-plano: cortar, paralela o contenida": {
        "tipo": "Recta + plano",
        "datos": {
            "punto_recta": "1,0,0",
            "director": "1,1,1",
            "normal": "1,1,1",
            "d": "3"
        }
    },
    "Rectas que se cruzan en 3D": {
        "tipo": "Dos rectas",
        "datos": {
            "punto_recta": "0,0,0",
            "director": "1,0,1",
            "punto_recta_2": "0,2,1",
            "director_2": "0,1,1"
        }
    }
}


def listar_ejemplos():
    return list(EJEMPLOS_GUIADOS_VISUALES.keys())


def generar_ejemplo(nombre):
    if nombre not in EJEMPLOS_GUIADOS_VISUALES:
        raise ValueError("Ejemplo no encontrado.")

    ejemplo = EJEMPLOS_GUIADOS_VISUALES[nombre]
    fig, explicacion = generar_escena(ejemplo["tipo"], ejemplo["datos"])

    explicacion = (
        f"EJEMPLO GUIADO: {nombre}\n"
        + "=" * 60
        + "\n\n"
        + explicacion
    )

    return fig, explicacion


# ============================================================
# GENERADOR PRINCIPAL
# ============================================================

def generar_escena(tipo, datos):
    """
    tipo: string seleccionado en la GUI.
    datos: diccionario con textos.
    """

    if tipo == "Punto + vector":
        p = convertir_vector(datos["punto"])
        v = convertir_vector(datos["vector"])
        return escena_punto_vector(p, v)

    if tipo == "Recta":
        p0 = convertir_vector(datos["punto_recta"])
        u = convertir_vector(datos["director"])
        return escena_recta(p0, u)

    if tipo == "Plano":
        normal = convertir_vector(datos["normal"])
        d = convertir_numero(datos["d"])
        return escena_plano(normal, d)

    if tipo == "Plano parametrico":
        p0 = convertir_vector(datos["punto_recta"])
        u = convertir_vector(datos["director"])
        v = convertir_vector(datos["vector"])
        return escena_plano_parametrico(p0, u, v)

    if tipo == "Punto + recta":
        p = convertir_vector(datos["punto"])
        p0 = convertir_vector(datos["punto_recta"])
        u = convertir_vector(datos["director"])
        return escena_punto_recta(p, p0, u)

    if tipo == "Punto + plano":
        p = convertir_vector(datos["punto"])
        normal = convertir_vector(datos["normal"])
        d = convertir_numero(datos["d"])
        return escena_punto_plano(p, normal, d)

    if tipo == "Recta + plano":
        p0 = convertir_vector(datos["punto_recta"])
        u = convertir_vector(datos["director"])
        normal = convertir_vector(datos["normal"])
        d = convertir_numero(datos["d"])
        return escena_recta_plano(p0, u, normal, d)

    if tipo == "Dos rectas":
        p1 = convertir_vector(datos["punto_recta"])
        u1 = convertir_vector(datos["director"])
        p2 = convertir_vector(datos["punto_recta_2"])
        u2 = convertir_vector(datos["director_2"])
        return escena_rectas_cruzadas(p1, u1, p2, u2)

    raise ValueError("Tipo de visualizacion no reconocido.")