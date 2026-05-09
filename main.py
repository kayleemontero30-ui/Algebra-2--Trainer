
from datos_tema1 import TEMA1
from funciones_estudio import (
    cargar_progreso,
    mostrar_resumen,
    mostrar_formulas,
    mostrar_metodos,
    modo_flashcards,
    mini_test_vf,
    mini_test_mc,
    ejercicios_guiados,
    practicar_falladas,
    mostrar_progreso
)


def mostrar_menu():
    print("\n" + "=" * 80)
    print("ASISTENTE DE ESTUDIO - ALGEBRA II".center(80))
    print("=" * 80)
    print("Tema actual:", TEMA1["nombre"])
    print()
    print("1. Ver resumen del tema")
    print("2. Ver formulas y reglas importantes")
    print("3. Ver metodos paso a paso")
    print("4. Modo flashcards")
    print("5. Mini test verdadero/falso")
    print("6. Mini test multiple choice")
    print("7. Ejercicios guiados")
    print("8. Practicar preguntas falladas")
    print("9. Ver progreso")
    print("10. Salir")


def main():
    progreso = cargar_progreso()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mostrar_resumen(TEMA1)

        elif opcion == "2":
            mostrar_formulas(TEMA1)

        elif opcion == "3":
            mostrar_metodos(TEMA1)

        elif opcion == "4":
            modo_flashcards(TEMA1, progreso)

        elif opcion == "5":
            mini_test_vf(TEMA1, progreso)

        elif opcion == "6":
            mini_test_mc(TEMA1, progreso)

        elif opcion == "7":
            ejercicios_guiados(TEMA1, progreso)

        elif opcion == "8":
            practicar_falladas(TEMA1, progreso)

        elif opcion == "9":
            mostrar_progreso(progreso)

        elif opcion == "10":
            print("Saliendo del asistente de Algebra II...")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()