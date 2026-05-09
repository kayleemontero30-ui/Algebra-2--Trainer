# -*- coding: utf-8 -*-

import json
import os
import random
import customtkinter as ctk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from datos_tema1 import TEMA1
from datos_tema2 import TEMA2
from datos_tema3 import TEMA3
from datos_conexiones import CONEXIONES

from visualizador import generar_escena, generar_ejemplo, listar_ejemplos


# ============================================================
# CONFIGURACION GENERAL
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

PROGRESO_ARCHIVO = "progreso_algebra_gui.json"

TEMAS = {
    "Tema 1 - Formas cuadraticas": TEMA1,
    "Tema 2 - Espacios euclideos": TEMA2,
    "Tema 3 - Espacios afines": TEMA3
}


# ============================================================
# PROGRESO
# ============================================================

def cargar_progreso():
    if not os.path.exists(PROGRESO_ARCHIVO):
        return {
            "tests_realizados": 0,
            "preguntas_totales": 0,
            "preguntas_correctas": 0,
            "fallos_por_categoria": {},
            "preguntas_falladas": [],
            "flashcards_vistas": 0
        }

    with open(PROGRESO_ARCHIVO, "r", encoding="utf-8") as archivo:
        progreso = json.load(archivo)

    claves = {
        "tests_realizados": 0,
        "preguntas_totales": 0,
        "preguntas_correctas": 0,
        "fallos_por_categoria": {},
        "preguntas_falladas": [],
        "flashcards_vistas": 0
    }

    for clave, valor in claves.items():
        if clave not in progreso:
            progreso[clave] = valor

    return progreso


def guardar_progreso(progreso):
    with open(PROGRESO_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(progreso, archivo, indent=4, ensure_ascii=False)


# ============================================================
# APP PRINCIPAL
# ============================================================

class AlgebraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Asistente Visual - Algebra II")
        self.geometry("1350x850")
        self.minsize(1100, 720)

        self.tema_actual_nombre = "Tema 3 - Espacios afines"
        self.tema_actual = TEMAS[self.tema_actual_nombre]

        self.progreso = cargar_progreso()

        self.pagina_actual = None
        self.canvas_actual = None

        self.flashcards_actuales = []
        self.flashcard_indice = 0
        self.flashcard_mostrando_respuesta = False

        self.test_preguntas = []
        self.test_indice = 0
        self.test_correctas = 0
        self.test_respondido = False

        self.crear_layout()
        self.mostrar_pagina("Inicio")

    # ========================================================
    # LAYOUT BASE
    # ========================================================

    def crear_layout(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure(12, weight=1)

        self.main_frame = ctk.CTkFrame(self, corner_radius=18)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=16, pady=16)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.crear_sidebar()
        self.crear_header()

        self.contenido = ctk.CTkFrame(self.main_frame, corner_radius=14)
        self.contenido.grid(row=1, column=0, sticky="nsew", padx=12, pady=12)
        self.contenido.grid_rowconfigure(0, weight=1)
        self.contenido.grid_columnconfigure(0, weight=1)

    def crear_sidebar(self):
        titulo = ctk.CTkLabel(
            self.sidebar,
            text="Álgebra II",
            font=("Arial", 28, "bold")
        )
        titulo.grid(row=0, column=0, padx=20, pady=(28, 6))

        subtitulo = ctk.CTkLabel(
            self.sidebar,
            text="Asistente visual",
            font=("Arial", 14)
        )
        subtitulo.grid(row=1, column=0, padx=20, pady=(0, 24))

        botones = [
            ("🏠  Inicio", "Inicio"),
            ("📘  Resumen", "Resumen"),
            ("🧮  Fórmulas", "Formulas"),
            ("🧠  Interpretar", "Interpretar"),
            ("🃏  Flashcards", "Flashcards"),
            ("✅  Mini test", "Mini Test"),
            ("📊  Progreso", "Progreso"),
            ("📐  Visualizador T3", "Visualizador")
        ]

        for i, (texto, pagina) in enumerate(botones, start=2):
            boton = ctk.CTkButton(
                self.sidebar,
                text=texto,
                height=42,
                corner_radius=12,
                anchor="w",
                command=lambda p=pagina: self.mostrar_pagina(p)
            )
            boton.grid(row=i, column=0, sticky="ew", padx=18, pady=5)

        salir = ctk.CTkButton(
            self.sidebar,
            text="Salir",
            fg_color="#7a1f1f",
            hover_color="#9b2c2c",
            height=40,
            corner_radius=12,
            command=self.destroy
        )
        salir.grid(row=13, column=0, sticky="ew", padx=18, pady=18)

    def crear_header(self):
        self.header = ctk.CTkFrame(self.main_frame, height=80, corner_radius=14)
        self.header.grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 0))
        self.header.grid_columnconfigure(0, weight=1)
        self.header.grid_columnconfigure(1, weight=0)

        self.titulo_pagina = ctk.CTkLabel(
            self.header,
            text="Inicio",
            font=("Arial", 24, "bold")
        )
        self.titulo_pagina.grid(row=0, column=0, sticky="w", padx=20, pady=18)

        self.selector_tema = ctk.CTkComboBox(
            self.header,
            values=list(TEMAS.keys()),
            width=310,
            command=self.cambiar_tema
        )
        self.selector_tema.set(self.tema_actual_nombre)
        self.selector_tema.grid(row=0, column=1, sticky="e", padx=20, pady=18)

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

        for i in range(10):
            self.contenido.grid_rowconfigure(i, weight=0)
            self.contenido.grid_columnconfigure(i, weight=0)

        self.contenido.grid_rowconfigure(0, weight=1)
        self.contenido.grid_columnconfigure(0, weight=1)

    def cambiar_tema(self, nombre):
        self.tema_actual_nombre = nombre
        self.tema_actual = TEMAS[nombre]

        if self.pagina_actual:
            self.mostrar_pagina(self.pagina_actual)

    def mostrar_pagina(self, pagina):
        self.pagina_actual = pagina
        self.titulo_pagina.configure(text=pagina)
        self.limpiar_contenido()

        if pagina == "Inicio":
            self.pagina_inicio()
        elif pagina == "Resumen":
            self.pagina_resumen()
        elif pagina == "Formulas":
            self.pagina_formulas()
        elif pagina == "Interpretar":
            self.pagina_interpretar()
        elif pagina == "Flashcards":
            self.pagina_flashcards()
        elif pagina == "Mini Test":
            self.pagina_mini_test()
        elif pagina == "Progreso":
            self.pagina_progreso()
        elif pagina == "Visualizador":
            self.pagina_visualizador()

    # ========================================================
    # HELPERS VISUALES
    # ========================================================

    def crear_card(self, parent, titulo, texto, row, column, padx=10, pady=10):
        card = ctk.CTkFrame(parent, corner_radius=16)
        card.grid(row=row, column=column, sticky="nsew", padx=padx, pady=pady)
        card.grid_columnconfigure(0, weight=1)

        label_titulo = ctk.CTkLabel(
            card,
            text=titulo,
            font=("Arial", 18, "bold")
        )
        label_titulo.grid(row=0, column=0, sticky="w", padx=18, pady=(16, 6))

        label_texto = ctk.CTkLabel(
            card,
            text=texto,
            justify="left",
            wraplength=420,
            font=("Arial", 14)
        )
        label_texto.grid(row=1, column=0, sticky="nw", padx=18, pady=(0, 16))

        return card

    def crear_textbox(self, parent, texto=""):
        textbox = ctk.CTkTextbox(
            parent,
            wrap="word",
            font=("Consolas", 14)
        )
        textbox.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        textbox.insert("1.0", texto)
        return textbox

    # ========================================================
    # PAGINA INICIO
    # ========================================================

    def pagina_inicio(self):
        self.contenido.grid_columnconfigure((0, 1), weight=1)
        self.contenido.grid_rowconfigure((0, 1), weight=1)

        self.crear_card(
            self.contenido,
            "Estudia por temas",
            "Elige Tema 1, 2 o 3 desde arriba. Puedes ver resumen, fórmulas, métodos e interpretación de enunciados.",
            0,
            0
        )

        self.crear_card(
            self.contenido,
            "Mini tests visuales",
            "Practica verdadero/falso, multiple choice o mixto. La app guarda aciertos, fallos y categorías débiles.",
            0,
            1
        )

        self.crear_card(
            self.contenido,
            "Visualizador Tema 3",
            "Mira ejemplos guiados de rectas, planos, vectores directores, normales, proyecciones y distancias.",
            1,
            0
        )

        self.crear_card(
            self.contenido,
            "Idea clave",
            "Recta → vector director.\nPlano → vector normal.\nDistancia → dirección perpendicular.\nPosición relativa → rangos o sistemas.",
            1,
            1
        )

    # ========================================================
    # RESUMEN
    # ========================================================

    def pagina_resumen(self):
        texto = self.tema_actual.get("resumen", "Este tema no tiene resumen.")
        self.crear_textbox(self.contenido, texto)

    # ========================================================
    # FORMULAS
    # ========================================================

    def pagina_formulas(self):
        self.contenido.grid_columnconfigure(0, weight=1)
        self.contenido.grid_columnconfigure(1, weight=2)
        self.contenido.grid_rowconfigure(0, weight=1)

        lista = ctk.CTkScrollableFrame(self.contenido, corner_radius=14)
        lista.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)

        detalle = ctk.CTkTextbox(
            self.contenido,
            wrap="word",
            font=("Consolas", 14)
        )
        detalle.grid(row=0, column=1, sticky="nsew", padx=12, pady=12)

        formulas = self.tema_actual.get("formulas", [])

        if not formulas:
            detalle.insert("1.0", "Este tema no tiene fórmulas.")
            return

        def mostrar_formula(formula):
            texto = f"{formula.get('nombre', '')}\n"
            texto += "=" * 80 + "\n\n"
            texto += f"Fórmula/regla:\n{formula.get('formula', '')}\n\n"
            texto += f"Uso:\n{formula.get('uso', '')}\n\n"

            if "cuando_usarla" in formula:
                texto += "Cuándo usarla:\n"
                for item in formula["cuando_usarla"]:
                    texto += f"- {item}\n"
                texto += "\n"

            if "detalles" in formula:
                texto += "Detalles:\n"
                for item in formula["detalles"]:
                    texto += f"- {item}\n"

            detalle.delete("1.0", "end")
            detalle.insert("1.0", texto)

        for formula in formulas:
            boton = ctk.CTkButton(
                lista,
                text=formula.get("nombre", "Sin nombre"),
                height=38,
                corner_radius=10,
                anchor="w",
                command=lambda f=formula: mostrar_formula(f)
            )
            boton.pack(fill="x", padx=8, pady=5)

        mostrar_formula(formulas[0])

    # ========================================================
    # INTERPRETAR ENUNCIADOS
    # ========================================================

    def pagina_interpretar(self):
        self.contenido.grid_columnconfigure(0, weight=1)
        self.contenido.grid_columnconfigure(1, weight=2)
        self.contenido.grid_rowconfigure(0, weight=1)

        lista = ctk.CTkScrollableFrame(self.contenido, corner_radius=14)
        lista.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)

        detalle = ctk.CTkTextbox(
            self.contenido,
            wrap="word",
            font=("Consolas", 14)
        )
        detalle.grid(row=0, column=1, sticky="nsew", padx=12, pady=12)

        guias = self.tema_actual.get("interpretacion_enunciados", [])

        if not guias:
            detalle.insert("1.0", "Este tema no tiene guía de interpretación de enunciados.")
            return

        def mostrar_guia(guia):
            texto = f"{guia.get('palabra_clave', '').upper()}\n"
            texto += "=" * 80 + "\n\n"
            texto += "Qué significa:\n"
            texto += guia.get("que_significa", "") + "\n\n"

            texto += "Qué suele pedir:\n"
            for item in guia.get("que_suele_pedir", []):
                texto += f"- {item}\n"

            texto += "\nOperaciones recomendadas:\n"
            for item in guia.get("operaciones_recomendadas", []):
                texto += f"- {item}\n"

            texto += "\nPista de examen:\n"
            texto += guia.get("pista_examen", "")

            detalle.delete("1.0", "end")
            detalle.insert("1.0", texto)

        for guia in guias:
            boton = ctk.CTkButton(
                lista,
                text=guia.get("palabra_clave", "Sin título"),
                height=38,
                corner_radius=10,
                anchor="w",
                command=lambda g=guia: mostrar_guia(g)
            )
            boton.pack(fill="x", padx=8, pady=5)

        mostrar_guia(guias[0])

    # ========================================================
    # FLASHCARDS
    # ========================================================

    def pagina_flashcards(self):
        self.contenido.grid_columnconfigure(0, weight=1)
        self.contenido.grid_rowconfigure(1, weight=1)

        panel = ctk.CTkFrame(self.contenido, corner_radius=14)
        panel.grid(row=0, column=0, sticky="ew", padx=12, pady=12)
        panel.grid_columnconfigure(2, weight=1)

        ctk.CTkLabel(panel, text="Cantidad:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)

        self.flash_cantidad = ctk.CTkEntry(panel, width=70)
        self.flash_cantidad.insert(0, "5")
        self.flash_cantidad.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(
            panel,
            text="Iniciar flashcards",
            command=self.iniciar_flashcards
        ).grid(row=0, column=2, sticky="w", padx=10, pady=10)

        self.flash_card_frame = ctk.CTkFrame(self.contenido, corner_radius=18)
        self.flash_card_frame.grid(row=1, column=0, sticky="nsew", padx=12, pady=12)
        self.flash_card_frame.grid_rowconfigure(1, weight=1)
        self.flash_card_frame.grid_columnconfigure(0, weight=1)

        self.flash_titulo = ctk.CTkLabel(
            self.flash_card_frame,
            text="Pulsa iniciar para estudiar flashcards.",
            font=("Arial", 20, "bold")
        )
        self.flash_titulo.grid(row=0, column=0, pady=(24, 8))

        self.flash_texto = ctk.CTkTextbox(
            self.flash_card_frame,
            wrap="word",
            font=("Consolas", 18)
        )
        self.flash_texto.grid(row=1, column=0, sticky="nsew", padx=30, pady=20)

        botones = ctk.CTkFrame(self.flash_card_frame)
        botones.grid(row=2, column=0, pady=18)

        ctk.CTkButton(
            botones,
            text="Mostrar respuesta",
            command=self.toggle_flashcard
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            botones,
            text="Siguiente",
            command=self.siguiente_flashcard
        ).grid(row=0, column=1, padx=10)

    def iniciar_flashcards(self):
        flashcards = self.tema_actual.get("flashcards", []).copy()

        if not flashcards:
            messagebox.showwarning("Sin flashcards", "Este tema no tiene flashcards.")
            return

        try:
            cantidad = int(self.flash_cantidad.get())
        except ValueError:
            cantidad = 5

        cantidad = max(1, min(cantidad, len(flashcards)))

        random.shuffle(flashcards)
        self.flashcards_actuales = flashcards[:cantidad]
        self.flashcard_indice = 0
        self.flashcard_mostrando_respuesta = False

        self.mostrar_flashcard_actual()

    def mostrar_flashcard_actual(self):
        if not self.flashcards_actuales:
            return

        card = self.flashcards_actuales[self.flashcard_indice]

        self.flash_titulo.configure(
            text=f"Flashcard {self.flashcard_indice + 1}/{len(self.flashcards_actuales)} - {card.get('categoria', '')}"
        )

        self.flash_texto.delete("1.0", "end")

        if self.flashcard_mostrando_respuesta:
            self.flash_texto.insert("1.0", card.get("reverso", ""))
        else:
            self.flash_texto.insert("1.0", card.get("frente", ""))

    def toggle_flashcard(self):
        if not self.flashcards_actuales:
            return

        self.flashcard_mostrando_respuesta = not self.flashcard_mostrando_respuesta
        self.mostrar_flashcard_actual()

    def siguiente_flashcard(self):
        if not self.flashcards_actuales:
            return

        self.progreso["flashcards_vistas"] += 1
        guardar_progreso(self.progreso)

        self.flashcard_indice += 1

        if self.flashcard_indice >= len(self.flashcards_actuales):
            self.flash_texto.delete("1.0", "end")
            self.flash_texto.insert("1.0", "Has terminado esta ronda de flashcards.")
            self.flash_titulo.configure(text="Flashcards terminadas")
            self.flashcards_actuales = []
            return

        self.flashcard_mostrando_respuesta = False
        self.mostrar_flashcard_actual()

    # ========================================================
    # MINI TEST
    # ========================================================

    def pagina_mini_test(self):
        self.contenido.grid_columnconfigure(0, weight=1)
        self.contenido.grid_rowconfigure(0, weight=0)
        self.contenido.grid_rowconfigure(1, weight=1)

        # Panel superior
        panel = ctk.CTkFrame(self.contenido, corner_radius=14)
        panel.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        panel.grid_columnconfigure(0, weight=1)
        panel.grid_columnconfigure(1, weight=1)
        panel.grid_columnconfigure(2, weight=1)
        panel.grid_columnconfigure(3, weight=1)

        titulo = ctk.CTkLabel(
            panel,
            text="Configurar mini test",
            font=("Arial", 20, "bold")
        )
        titulo.grid(row=0, column=0, columnspan=4, sticky="w", padx=18, pady=(16, 10))

        ctk.CTkLabel(panel, text="Tipo de test:").grid(
            row=1, column=0, sticky="w", padx=18, pady=(5, 2)
        )
        self.test_tipo = ctk.CTkComboBox(
            panel,
            values=["Verdadero/Falso", "Multiple choice", "Mixto"]
        )
        self.test_tipo.set("Mixto")
        self.test_tipo.grid(row=2, column=0, sticky="ew", padx=18, pady=(0, 16))

        ctk.CTkLabel(panel, text="Dificultad:").grid(
            row=1, column=1, sticky="w", padx=18, pady=(5, 2)
        )
        self.test_dificultad = ctk.CTkComboBox(
            panel,
            values=["facil", "media", "dificil", "mixto"]
        )
        self.test_dificultad.set("mixto")
        self.test_dificultad.grid(row=2, column=1, sticky="ew", padx=18, pady=(0, 16))

        ctk.CTkLabel(panel, text="Cantidad:").grid(
            row=1, column=2, sticky="w", padx=18, pady=(5, 2)
        )
        self.test_cantidad = ctk.CTkEntry(panel)
        self.test_cantidad.insert(0, "5")
        self.test_cantidad.grid(row=2, column=2, sticky="ew", padx=18, pady=(0, 16))

        boton_iniciar = ctk.CTkButton(
            panel,
            text="Iniciar test",
            height=40,
            command=self.iniciar_test
        )
        boton_iniciar.grid(row=2, column=3, sticky="ew", padx=18, pady=(0, 16))

        # Frame principal del test
        self.test_frame = ctk.CTkFrame(self.contenido, corner_radius=18)
        self.test_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.test_frame.grid_columnconfigure(0, weight=1)
        self.test_frame.grid_rowconfigure(1, weight=0)
        self.test_frame.grid_rowconfigure(3, weight=1)

        self.test_titulo = ctk.CTkLabel(
            self.test_frame,
            text="Pulsa 'Iniciar test' para empezar.",
            font=("Arial", 22, "bold")
        )
        self.test_titulo.grid(row=0, column=0, pady=(24, 10))

        self.test_pregunta_texto = ctk.CTkTextbox(
            self.test_frame,
            wrap="word",
            font=("Consolas", 17),
            height=160
        )
        self.test_pregunta_texto.grid(row=1, column=0, sticky="ew", padx=28, pady=12)
        self.test_pregunta_texto.insert(
            "1.0",
            "Elige tipo, dificultad y cantidad arriba.\n\nLuego pulsa 'Iniciar test'."
        )

        self.test_opciones_frame = ctk.CTkFrame(self.test_frame, corner_radius=12)
        self.test_opciones_frame.grid(row=2, column=0, sticky="ew", padx=28, pady=12)

        self.test_explicacion = ctk.CTkTextbox(
            self.test_frame,
            wrap="word",
            font=("Consolas", 14),
            height=170
        )
        self.test_explicacion.grid(row=3, column=0, sticky="nsew", padx=28, pady=12)
        self.test_explicacion.insert(
            "1.0",
            "Aquí aparecerá la explicación después de responder."
        )

        boton_siguiente = ctk.CTkButton(
            self.test_frame,
            text="Siguiente pregunta",
            height=40,
            command=self.siguiente_pregunta_test
        )
        boton_siguiente.grid(row=4, column=0, pady=(8, 22))

    def preparar_preguntas_test(self):
        tipo = self.test_tipo.get()
        dificultad = self.test_dificultad.get()

        preguntas = []

        if tipo in ["Verdadero/Falso", "Mixto"]:
            for p in self.tema_actual.get("preguntas_vf", []):
                copia = p.copy()
                copia["tipo"] = "vf"
                preguntas.append(copia)

        if tipo in ["Multiple choice", "Mixto"]:
            for p in self.tema_actual.get("preguntas_mc", []):
                copia = p.copy()
                copia["tipo"] = "mc"
                preguntas.append(copia)

        if dificultad != "mixto":
            preguntas = [p for p in preguntas if p.get("dificultad") == dificultad]

        return preguntas

    def iniciar_test(self):
        preguntas = self.preparar_preguntas_test()

        if not preguntas:
            messagebox.showwarning("Sin preguntas", "No hay preguntas para esta configuración.")
            return

        try:
            cantidad = int(self.test_cantidad.get())
        except ValueError:
            cantidad = 5

        cantidad = max(1, min(cantidad, len(preguntas)))

        self.test_preguntas = random.sample(preguntas, cantidad)
        self.test_indice = 0
        self.test_correctas = 0
        self.test_respondido = False

        self.mostrar_pregunta_test()

    def mostrar_pregunta_test(self):
        for widget in self.test_opciones_frame.winfo_children():
            widget.destroy()

        self.test_explicacion.delete("1.0", "end")

        if self.test_indice >= len(self.test_preguntas):
            self.finalizar_test()
            return

        pregunta = self.test_preguntas[self.test_indice]

        self.test_titulo.configure(
            text=f"Pregunta {self.test_indice + 1}/{len(self.test_preguntas)} - {pregunta.get('categoria', '')}"
        )

        self.test_pregunta_texto.delete("1.0", "end")
        self.test_pregunta_texto.insert("1.0", pregunta.get("pregunta", ""))

        self.test_respondido = False

        if pregunta["tipo"] == "vf":
            boton_v = ctk.CTkButton(
                self.test_opciones_frame,
                text="Verdadero",
                height=42,
                command=lambda: self.responder_test(True)
            )
            boton_v.pack(side="left", padx=12, pady=14)

            boton_f = ctk.CTkButton(
                self.test_opciones_frame,
                text="Falso",
                height=42,
                command=lambda: self.responder_test(False)
            )
            boton_f.pack(side="left", padx=12, pady=14)

        else:
            opciones = pregunta.get("opciones", [])

            for i, opcion in enumerate(opciones, start=1):
                boton = ctk.CTkButton(
                    self.test_opciones_frame,
                    text=f"{i}. {opcion}",
                    height=40,
                    anchor="w",
                    command=lambda respuesta=i: self.responder_test(respuesta)
                )
                boton.pack(fill="x", padx=12, pady=6)

    def responder_test(self, respuesta_usuario):
        if self.test_respondido:
            return

        pregunta = self.test_preguntas[self.test_indice]
        correcto = respuesta_usuario == pregunta.get("respuesta")

        if correcto:
            self.test_correctas += 1
            resultado = "Correcto."
        else:
            resultado = "Incorrecto."

        self.registrar_resultado_test(pregunta, correcto)

        texto = resultado + "\n\n"
        texto += "Explicación:\n"
        texto += pregunta.get("explicacion", "")

        if pregunta["tipo"] == "mc" and not correcto:
            texto += f"\n\nRespuesta correcta: opción {pregunta.get('respuesta')}"

        self.test_explicacion.delete("1.0", "end")
        self.test_explicacion.insert("1.0", texto)

        self.test_respondido = True

    def registrar_resultado_test(self, pregunta, correcto):
        self.progreso["preguntas_totales"] += 1

        pregunta_id = f"{self.tema_actual_nombre}:{pregunta['tipo']}:{pregunta['id']}"

        if correcto:
            self.progreso["preguntas_correctas"] += 1

            if pregunta_id in self.progreso["preguntas_falladas"]:
                self.progreso["preguntas_falladas"].remove(pregunta_id)
        else:
            categoria = pregunta.get("categoria", "Sin categoria")

            if categoria not in self.progreso["fallos_por_categoria"]:
                self.progreso["fallos_por_categoria"][categoria] = 0

            self.progreso["fallos_por_categoria"][categoria] += 1

            if pregunta_id not in self.progreso["preguntas_falladas"]:
                self.progreso["preguntas_falladas"].append(pregunta_id)

        guardar_progreso(self.progreso)

    def siguiente_pregunta_test(self):
        if not self.test_preguntas:
            return

        if not self.test_respondido:
            messagebox.showinfo("Responde primero", "Primero responde la pregunta actual.")
            return

        self.test_indice += 1
        self.mostrar_pregunta_test()

    def finalizar_test(self):
        self.progreso["tests_realizados"] += 1
        guardar_progreso(self.progreso)

        for widget in self.test_opciones_frame.winfo_children():
            widget.destroy()

        self.test_titulo.configure(text="Mini test terminado")
        self.test_pregunta_texto.delete("1.0", "end")
        self.test_pregunta_texto.insert(
            "1.0",
            f"Puntuación final: {self.test_correctas}/{len(self.test_preguntas)}"
        )

        self.test_explicacion.delete("1.0", "end")
        self.test_explicacion.insert(
            "1.0",
            "Puedes cambiar tema, dificultad o tipo de test y empezar otra ronda."
        )

        self.test_preguntas = []

    # ========================================================
    # PROGRESO
    # ========================================================

    def pagina_progreso(self):
        self.contenido.grid_columnconfigure(0, weight=1)
        self.contenido.grid_rowconfigure(0, weight=1)

        total = self.progreso.get("preguntas_totales", 0)
        correctas = self.progreso.get("preguntas_correctas", 0)

        if total > 0:
            porcentaje = correctas / total * 100
        else:
            porcentaje = 0

        texto = ""
        texto += "PROGRESO GENERAL\n"
        texto += "=" * 80 + "\n\n"
        texto += f"Tests realizados: {self.progreso.get('tests_realizados', 0)}\n"
        texto += f"Flashcards vistas: {self.progreso.get('flashcards_vistas', 0)}\n"
        texto += f"Preguntas totales: {total}\n"
        texto += f"Preguntas correctas: {correctas}\n"
        texto += f"Porcentaje de acierto: {porcentaje:.2f}%\n"
        texto += f"Preguntas falladas pendientes: {len(self.progreso.get('preguntas_falladas', []))}\n\n"

        texto += "FALLOS POR CATEGORÍA\n"
        texto += "-" * 80 + "\n"

        fallos = self.progreso.get("fallos_por_categoria", {})

        if not fallos:
            texto += "Todavía no hay fallos registrados.\n"
        else:
            for categoria, cantidad in sorted(fallos.items(), key=lambda x: x[1], reverse=True):
                texto += f"- {categoria}: {cantidad}\n"

        self.crear_textbox(self.contenido, texto)

    # ========================================================
    # VISUALIZADOR
    # ========================================================

    def pagina_visualizador(self):
        self.contenido.grid_columnconfigure(0, weight=0)
        self.contenido.grid_columnconfigure(1, weight=1)
        self.contenido.grid_rowconfigure(0, weight=1)

        panel = ctk.CTkScrollableFrame(self.contenido, width=330, corner_radius=14)
        panel.grid(row=0, column=0, sticky="ns", padx=12, pady=12)

        derecha = ctk.CTkFrame(self.contenido, corner_radius=14)
        derecha.grid(row=0, column=1, sticky="nsew", padx=12, pady=12)
        derecha.grid_columnconfigure(0, weight=1)
        derecha.grid_rowconfigure(0, weight=3)
        derecha.grid_rowconfigure(1, weight=1)

        self.plot_area = ctk.CTkFrame(derecha, corner_radius=14)
        self.plot_area.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)

        self.explicacion_visual = ctk.CTkTextbox(
            derecha,
            wrap="word",
            font=("Consolas", 13)
        )
        self.explicacion_visual.grid(row=1, column=0, sticky="nsew", padx=12, pady=12)

        ctk.CTkLabel(
            panel,
            text="Visualizador Tema 3",
            font=("Arial", 20, "bold")
        ).pack(padx=10, pady=(14, 8))

        ctk.CTkLabel(
            panel,
            text="Modo:",
            anchor="w"
        ).pack(fill="x", padx=10, pady=(8, 0))

        self.visual_modo = ctk.CTkComboBox(
            panel,
            values=["Ejemplos guiados", "Manual"],
            command=lambda _: self.actualizar_modo_visual()
        )
        self.visual_modo.set("Ejemplos guiados")
        self.visual_modo.pack(fill="x", padx=10, pady=5)

        self.visual_panel_dinamico = ctk.CTkFrame(panel, corner_radius=12)
        self.visual_panel_dinamico.pack(fill="x", padx=10, pady=10)

        self.actualizar_modo_visual()

    def actualizar_modo_visual(self):
        for widget in self.visual_panel_dinamico.winfo_children():
            widget.destroy()

        modo = self.visual_modo.get()

        if modo == "Ejemplos guiados":
            self.crear_modo_ejemplos()
        else:
            self.crear_modo_manual()

    def crear_modo_ejemplos(self):
        ctk.CTkLabel(
            self.visual_panel_dinamico,
            text="Elige un ejemplo:",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 4))

        self.combo_ejemplos = ctk.CTkComboBox(
            self.visual_panel_dinamico,
            values=listar_ejemplos(),
            width=280
        )
        ejemplos = listar_ejemplos()
        self.combo_ejemplos.set(ejemplos[0])
        self.combo_ejemplos.pack(fill="x", padx=10, pady=6)

        ctk.CTkButton(
            self.visual_panel_dinamico,
            text="Mostrar ejemplo",
            command=self.dibujar_ejemplo_guiado
        ).pack(fill="x", padx=10, pady=12)

        ayuda = """
Usa este modo cuando todavía
no sepas crear tus propios datos.

Te enseña:
- vector director de rectas,
- normal de planos,
- proyecciones,
- distancias,
- posición recta-plano,
- rectas cruzadas.
"""
        ctk.CTkLabel(
            self.visual_panel_dinamico,
            text=ayuda,
            justify="left"
        ).pack(anchor="w", padx=10, pady=10)

        self.dibujar_ejemplo_guiado()

    def crear_modo_manual(self):
        ctk.CTkLabel(
            self.visual_panel_dinamico,
            text="Tipo manual:",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 4))

        self.tipo_visual = ctk.CTkComboBox(
            self.visual_panel_dinamico,
            values=[
                "Punto + vector",
                "Recta",
                "Plano",
                "Plano parametrico",
                "Punto + recta",
                "Punto + plano",
                "Recta + plano",
                "Dos rectas"
            ]
        )
        self.tipo_visual.set("Punto + recta")
        self.tipo_visual.pack(fill="x", padx=10, pady=6)

        self.entrada_punto = self.crear_entrada(self.visual_panel_dinamico, "Punto P", "1,1,1")
        self.entrada_vector = self.crear_entrada(self.visual_panel_dinamico, "Vector v / segundo director", "0,1,1")
        self.entrada_punto_recta = self.crear_entrada(self.visual_panel_dinamico, "Punto recta/plano P0", "1,-1,-2")
        self.entrada_director = self.crear_entrada(self.visual_panel_dinamico, "Vector director u", "1,2,2")
        self.entrada_normal = self.crear_entrada(self.visual_panel_dinamico, "Normal plano n", "1,1,1")
        self.entrada_d = self.crear_entrada(self.visual_panel_dinamico, "Plano d: n·X=d", "0")
        self.entrada_punto_recta_2 = self.crear_entrada(self.visual_panel_dinamico, "Punto recta 2", "0,2,1")
        self.entrada_director_2 = self.crear_entrada(self.visual_panel_dinamico, "Director recta 2", "0,1,1")

        ctk.CTkButton(
            self.visual_panel_dinamico,
            text="Dibujar manual",
            command=self.dibujar_visualizacion_manual
        ).pack(fill="x", padx=10, pady=14)

        ayuda = """
Formato:
- Vectores: 1,2,3
- Plano: n=(a,b,c), d
- Recta: P0 y u
"""
        ctk.CTkLabel(
            self.visual_panel_dinamico,
            text=ayuda,
            justify="left"
        ).pack(anchor="w", padx=10, pady=8)

        self.dibujar_visualizacion_manual()

    def crear_entrada(self, parent, label, defecto):
        ctk.CTkLabel(parent, text=label).pack(anchor="w", padx=10, pady=(8, 0))
        entrada = ctk.CTkEntry(parent)
        entrada.insert(0, defecto)
        entrada.pack(fill="x", padx=10, pady=4)
        return entrada

    def obtener_datos_visualizador(self):
        return {
            "punto": self.entrada_punto.get(),
            "vector": self.entrada_vector.get(),
            "punto_recta": self.entrada_punto_recta.get(),
            "director": self.entrada_director.get(),
            "normal": self.entrada_normal.get(),
            "d": self.entrada_d.get(),
            "punto_recta_2": self.entrada_punto_recta_2.get(),
            "director_2": self.entrada_director_2.get()
        }

    def mostrar_figura(self, fig, explicacion):
        for widget in self.plot_area.winfo_children():
            widget.destroy()

        self.canvas_actual = FigureCanvasTkAgg(fig, master=self.plot_area)
        self.canvas_actual.draw()
        self.canvas_actual.get_tk_widget().pack(fill="both", expand=True)

        plt.close(fig)

        self.explicacion_visual.delete("1.0", "end")
        self.explicacion_visual.insert("1.0", explicacion)

    def dibujar_ejemplo_guiado(self):
        try:
            nombre = self.combo_ejemplos.get()
            fig, explicacion = generar_ejemplo(nombre)
            self.mostrar_figura(fig, explicacion)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def dibujar_visualizacion_manual(self):
        try:
            tipo = self.tipo_visual.get()
            datos = self.obtener_datos_visualizador()
            fig, explicacion = generar_escena(tipo, datos)
            self.mostrar_figura(fig, explicacion)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = AlgebraApp()
    app.mainloop()
