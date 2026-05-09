# -*- coding: utf-8 -*-

import json
import os
import random

PROGRESO_ARCHIVO = "progreso_algebra.json"


def cargar_progreso():
    if not os.path.exists(PROGRESO_ARCHIVO):
        return {
            "tests_realizados": 0,
            "preguntas_totales": 0,
            "preguntas_correctas": 0,
            "fallos_por_categoria": {},
            "preguntas_falladas": [],
            "flashcards_vistas": 0,
            "ejercicios_guiados_vistos": 0
        }

    with open(PROGRESO_ARCHIVO, "r", encoding="utf-8") as archivo:
        progreso = json.load(archivo)

    claves = {
        "tests_realizados": 0,
        "preguntas_totales": 0,
        "preguntas_correctas": 0,
        "fallos_por_categoria": {},
        "preguntas_falladas": [],
        "flashcards_vistas": 0,
        "ejercicios_guiados_vistos": 0
    }

    for clave, valor in claves.items():
        if clave not in progreso:
            progreso[clave] = valor

    return progreso


def guardar_progreso(progreso):
    with open(PROGRESO_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(progreso, archivo, indent=4, ensure_ascii=False)


def pedir_numero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))

            if minimo <= numero <= maximo:
                return numero

            print(f"Introduce un numero entre {minimo} y {maximo}.")

        except ValueError:
            print("Entrada no valida. Introduce un numero.")


def elegir_dificultad():
    print("\nDificultad:")
    print("1. Facil")
    print("2. Media")
    print("3. Dificil")
    print("4. Mixto")

    opcion = pedir_numero("Elige dificultad: ", 1, 4)

    if opcion == 1:
        return "facil"
    elif opcion == 2:
        return "media"
    elif opcion == 3:
        return "dificil"
    else:
        return "mixto"


def filtrar_por_dificultad(preguntas, dificultad):
    if dificultad == "mixto":
        return preguntas

    return [pregunta for pregunta in preguntas if pregunta["dificultad"] == dificultad]


def mostrar_resumen(tema):
    print("\n" + "=" * 80)
    print(tema["nombre"].center(80))
    print("=" * 80)
    print(tema["resumen"])


def mostrar_formulas(tema):
    print("\n" + "=" * 80)
    print("FORMULAS Y REGLAS IMPORTANTES".center(80))
    print("=" * 80)

    for i, formula in enumerate(tema["formulas"], start=1):
        print(f"\n{i}. {formula['nombre']}")
        print("-" * 80)
        print("Formula/regla:", formula["formula"])
        print("Uso:", formula["uso"])

        if "cuando_usarla" in formula:
            print("Cuando usarla:")
            for caso in formula["cuando_usarla"]:
                print(" -", caso)

        if "detalles" in formula:
            print("Detalles:")
            for detalle in formula["detalles"]:
                print(" -", detalle)


def mostrar_metodos(tema):
    print("\n" + "=" * 80)
    print("METODOS PASO A PASO".center(80))
    print("=" * 80)

    for i, metodo in enumerate(tema["metodos"], start=1):
        print(f"\n{i}. {metodo['nombre']}")
        print("-" * 80)
        print("Objetivo:", metodo["objetivo"])
        print("Pasos:")

        for j, paso in enumerate(metodo["pasos"], start=1):
            print(f"  {j}. {paso}")

        if "errores_comunes" in metodo:
            print("Errores comunes:")
            for error in metodo["errores_comunes"]:
                print(" -", error)


def mostrar_conexiones(conexiones):
    print("\n" + "=" * 80)
    print("CONEXIONES ENTRE TEMAS".center(80))
    print("=" * 80)

    for i, conexion in enumerate(conexiones, start=1):
        print(f"\n{i}. {conexion['titulo']}")
        print("-" * 80)
        print(conexion["explicacion"])
        print("Ejemplo:", conexion["ejemplo"])


def modo_flashcards(tema, progreso):
    flashcards = tema["flashcards"].copy()
    random.shuffle(flashcards)

    cantidad = pedir_numero(
        f"Cuantas flashcards quieres estudiar? Maximo {len(flashcards)}: ",
        1,
        len(flashcards)
    )

    seleccionadas = flashcards[:cantidad]

    for i, card in enumerate(seleccionadas, start=1):
        print("\n" + "=" * 80)
        print(f"FLASHCARD {i}/{cantidad}")
        print("Categoria:", card["categoria"])
        print("-" * 80)
        print("Pregunta:")
        print(card["frente"])

        input("\nPulsa ENTER para ver la respuesta...")

        print("\nRespuesta:")
        print(card["reverso"])

        progreso["flashcards_vistas"] += 1
        input("\nPulsa ENTER para continuar...")

    guardar_progreso(progreso)


def preparar_vf(tema):
    preguntas = []

    for pregunta in tema["preguntas_vf"]:
        copia = pregunta.copy()
        copia["tipo"] = "vf"
        preguntas.append(copia)

    return preguntas


def preparar_mc(tema):
    preguntas = []

    for pregunta in tema["preguntas_mc"]:
        copia = pregunta.copy()
        copia["tipo"] = "mc"
        preguntas.append(copia)

    return preguntas


def preparar_banco_completo(tema):
    banco = []
    banco.extend(preparar_vf(tema))
    banco.extend(preparar_mc(tema))
    return banco


def obtener_id_pregunta(pregunta):
    tema_nombre = pregunta.get("tema_nombre", "")
    return tema_nombre + ":" + pregunta["tipo"] + ":" + pregunta["id"]


def registrar_resultado(progreso, pregunta, correcto):
    progreso["preguntas_totales"] += 1

    pregunta_id = obtener_id_pregunta(pregunta)

    if correcto:
        progreso["preguntas_correctas"] += 1

        if pregunta_id in progreso["preguntas_falladas"]:
            progreso["preguntas_falladas"].remove(pregunta_id)

    else:
        categoria = pregunta.get("categoria", "Sin categoria")

        if categoria not in progreso["fallos_por_categoria"]:
            progreso["fallos_por_categoria"][categoria] = 0

        progreso["fallos_por_categoria"][categoria] += 1

        if pregunta_id not in progreso["preguntas_falladas"]:
            progreso["preguntas_falladas"].append(pregunta_id)


def preguntar_vf(pregunta):
    print("\n" + "-" * 80)
    print("VERDADERO O FALSO")
    print("Categoria:", pregunta["categoria"])
    print("Dificultad:", pregunta["dificultad"])
    print("-" * 80)
    print(pregunta["pregunta"])

    while True:
        respuesta = input("Respuesta (v/f): ").strip().lower()

        if respuesta in ["v", "verdadero"]:
            respuesta_usuario = True
            break

        elif respuesta in ["f", "falso"]:
            respuesta_usuario = False
            break

        else:
            print("Respuesta no valida. Escribe v o f.")

    correcto = respuesta_usuario == pregunta["respuesta"]

    if correcto:
        print("Correcto.")
    else:
        print("Incorrecto.")

    print("Explicacion:", pregunta["explicacion"])

    return correcto


def preguntar_mc(pregunta):
    print("\n" + "-" * 80)
    print("MULTIPLE CHOICE")
    print("Categoria:", pregunta["categoria"])
    print("Dificultad:", pregunta["dificultad"])
    print("-" * 80)
    print(pregunta["pregunta"])

    for i, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{i}. {opcion}")

    respuesta_usuario = pedir_numero(
        "Elige una opcion: ",
        1,
        len(pregunta["opciones"])
    )

    correcto = respuesta_usuario == pregunta["respuesta"]

    if correcto:
        print("Correcto.")
    else:
        print("Incorrecto.")
        print("Respuesta correcta:", pregunta["respuesta"])

    print("Explicacion:", pregunta["explicacion"])

    return correcto


def hacer_preguntas(preguntas, progreso, titulo, tema_nombre):
    if len(preguntas) == 0:
        print("No hay preguntas disponibles para esta opcion.")
        return

    for pregunta in preguntas:
        pregunta["tema_nombre"] = tema_nombre

    cantidad = pedir_numero(
        f"Cuantas preguntas quieres? Maximo {len(preguntas)}: ",
        1,
        len(preguntas)
    )

    seleccionadas = random.sample(preguntas, cantidad)
    correctas = 0

    for pregunta in seleccionadas:
        if pregunta["tipo"] == "vf":
            correcto = preguntar_vf(pregunta)
        elif pregunta["tipo"] == "mc":
            correcto = preguntar_mc(pregunta)
        else:
            correcto = False

        registrar_resultado(progreso, pregunta, correcto)

        if correcto:
            correctas += 1

    progreso["tests_realizados"] += 1
    guardar_progreso(progreso)

    print("\n" + "=" * 80)
    print(titulo.center(80))
    print("=" * 80)
    print(f"Puntuacion: {correctas}/{cantidad}")


def mini_test_vf(tema, progreso):
    dificultad = elegir_dificultad()
    preguntas = filtrar_por_dificultad(preparar_vf(tema), dificultad)
    hacer_preguntas(preguntas, progreso, "RESULTADO TEST VERDADERO/FALSO", tema["nombre"])


def mini_test_mc(tema, progreso):
    dificultad = elegir_dificultad()
    preguntas = filtrar_por_dificultad(preparar_mc(tema), dificultad)
    hacer_preguntas(preguntas, progreso, "RESULTADO TEST MULTIPLE CHOICE", tema["nombre"])


def practicar_falladas(tema, progreso):
    banco = preparar_banco_completo(tema)

    for pregunta in banco:
        pregunta["tema_nombre"] = tema["nombre"]

    falladas = []

    for pregunta in banco:
        pregunta_id = obtener_id_pregunta(pregunta)

        if pregunta_id in progreso["preguntas_falladas"]:
            falladas.append(pregunta)

    if len(falladas) == 0:
        print("\nNo tienes preguntas falladas pendientes para este tema.")
        return

    hacer_preguntas(falladas, progreso, "RESULTADO PREGUNTAS FALLADAS", tema["nombre"])


def ejercicios_guiados(tema, progreso):
    ejercicios = tema["ejercicios_guiados"].copy()
    random.shuffle(ejercicios)

    cantidad = pedir_numero(
        f"Cuantos ejercicios guiados quieres ver? Maximo {len(ejercicios)}: ",
        1,
        len(ejercicios)
    )

    seleccionados = ejercicios[:cantidad]

    for i, ejercicio in enumerate(seleccionados, start=1):
        print("\n" + "=" * 80)
        print(f"EJERCICIO GUIADO {i}/{cantidad}")
        print("Categoria:", ejercicio["categoria"])
        print("Dificultad:", ejercicio["dificultad"])
        print("=" * 80)

        print("\nEnunciado:")
        print(ejercicio["enunciado"])

        input("\nPulsa ENTER para ver la solucion paso a paso...")

        print("\nSolucion:")
        for j, paso in enumerate(ejercicio["solucion"], start=1):
            print(f"{j}. {paso}")

        progreso["ejercicios_guiados_vistos"] += 1
        input("\nPulsa ENTER para continuar...")

    guardar_progreso(progreso)


def mostrar_progreso(progreso):
    print("\n" + "=" * 80)
    print("PROGRESO".center(80))
    print("=" * 80)

    print("Tests realizados:", progreso["tests_realizados"])
    print("Flashcards vistas:", progreso["flashcards_vistas"])
    print("Ejercicios guiados vistos:", progreso["ejercicios_guiados_vistos"])
    print("Preguntas totales:", progreso["preguntas_totales"])
    print("Preguntas correctas:", progreso["preguntas_correctas"])

    if progreso["preguntas_totales"] > 0:
        porcentaje = progreso["preguntas_correctas"] / progreso["preguntas_totales"] * 100
        print(f"Porcentaje de acierto: {porcentaje:.2f}%")
    else:
        print("Porcentaje de acierto: 0%")

    print("\nPreguntas falladas pendientes:", len(progreso["preguntas_falladas"]))

    print("\nFallos por categoria:")
    if len(progreso["fallos_por_categoria"]) == 0:
        print("Todavia no hay fallos registrados.")
    else:
        for categoria, fallos in progreso["fallos_por_categoria"].items():
            print(f"- {categoria}: {fallos}")


def interpretar_enunciados(tema):
    if "interpretacion_enunciados" not in tema:
        print("\nEste tema no tiene seccion de interpretacion de enunciados.")
        return

    guias = tema["interpretacion_enunciados"]

    while True:
        print("\n" + "=" * 80)
        print("COMO INTERPRETAR ENUNCIADOS".center(80))
        print("=" * 80)

        for i, guia in enumerate(guias, start=1):
            print(f"{i}. {guia['palabra_clave']}")

        print(f"{len(guias) + 1}. Volver")

        opcion = pedir_numero("Elige una palabra clave: ", 1, len(guias) + 1)

        if opcion == len(guias) + 1:
            break

        guia = guias[opcion - 1]

        print("\n" + "-" * 80)
        print(guia["palabra_clave"].upper())
        print("-" * 80)

        print("\nQue significa:")
        print(guia["que_significa"])

        print("\nQue suele pedir:")
        for item in guia["que_suele_pedir"]:
            print(" -", item)

        print("\nOperaciones recomendadas:")
        for item in guia["operaciones_recomendadas"]:
            print(" -", item)

        print("\nPista de examen:")
        print(guia["pista_examen"])

        input("\nPulsa ENTER para continuar...")