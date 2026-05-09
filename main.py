# -*- coding: utf-8 -*-

from datos_tema1 import TEMA1
from datos_tema2 import TEMA2
from datos_conexiones import CONEXIONES

from funciones_estudio import (
    cargar_progreso,
    mostrar_resumen,
    mostrar_formulas,
    mostrar_metodos,
    mostrar_conexiones,
    interpretar_enunciados,
    modo_flashcards,
    mini_test_vf,
    mini_test_mc,
    ejercicios_guiados,
    practicar_falladas,
    mostrar_progreso,
    pedir_numero
)


TEMAS = {
    "1": TEMA1,
    "2": TEMA2
}


def elegir_tema():
    while True:
        print("\n" + "=" * 80)
        print("ELEGIR TEMA".center(80))
        print("=" * 80)
        print("1. Tema 1 - Formas bilineales y formas cuadraticas")
        print("2. Tema 2 - Espacios vectoriales euclideos")

        opcion = input("Elige tema: ").strip()

        if opcion in TEMAS:
            return TEMAS[opcion]

        print("Opcion no valida.")


def mostrar_menu(tema):
    print("\n" + "=" * 80)
    print("ASISTENTE DE ESTUDIO - ALGEBRA II".center(80))
    print("=" * 80)
    print("Tema actual:", tema["nombre"])
    print()
    print("1. Ver resumen del tema")
    print("2. Ver formulas y reglas importantes")
    print("3. Ver metodos paso a paso")
    print("4. Como interpretar enunciados")
    print("5. Modo flashcards")
    print("6. Mini test verdadero/falso")
    print("7. Mini test multiple choice")
    print("8. Ejercicios guiados")
    print("9. Practicar preguntas falladas de este tema")
    print("10. Ver progreso")
    print("11. Ver conexiones entre temas")
    print("12. Cambiar tema")
    print("13. Salir")


def main():
    progreso = cargar_progreso()
    tema_actual = elegir_tema()

    while True:
        mostrar_menu(tema_actual)
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mostrar_resumen(tema_actual)

        elif opcion == "2":
            mostrar_formulas(tema_actual)

        elif opcion == "3":
            mostrar_metodos(tema_actual)

        elif opcion == "4":
            interpretar_enunciados(tema_actual)

        elif opcion == "5":
            modo_flashcards(tema_actual, progreso)

        elif opcion == "6":
            mini_test_vf(tema_actual, progreso)

        elif opcion == "7":
            mini_test_mc(tema_actual, progreso)

        elif opcion == "8":
            ejercicios_guiados(tema_actual, progreso)

        elif opcion == "9":
            practicar_falladas(tema_actual, progreso)

        elif opcion == "10":
            mostrar_progreso(progreso)

        elif opcion == "11":
            mostrar_conexiones(CONEXIONES)

        elif opcion == "12":
            tema_actual = elegir_tema()

        elif opcion == "13":
            print("Saliendo del asistente de Algebra II...")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()