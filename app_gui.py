# -*- coding: utf-8 -*-

import customtkinter as ctk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from datos_tema1 import TEMA1
from datos_tema2 import TEMA2
from datos_tema3 import TEMA3
from datos_conexiones import CONEXIONES

from visualizador import generar_escena


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


TEMAS = {
    "Tema 1 - Formas cuadraticas": TEMA1,
    "Tema 2 - Espacios euclideos": TEMA2,
    "Tema 3 - Espacios afines": TEMA3
}


class AlgebraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Asistente Visual - Algebra II")
        self.geometry("1200x800")

        self.tema_actual_nombre = "Tema 3 - Espacios afines"
        self.tema_actual = TEMAS[self.tema_actual_nombre]

        self.canvas_actual = None

        self.crear_layout()

    def crear_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Asistente Visual de Algebra II",
            font=("Arial", 26, "bold")
        )
        titulo.grid(row=0, column=0, pady=10)

        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)

        self.tab_inicio = self.tabs.add("Inicio")
        self.tab_resumen = self.tabs.add("Resumen")
        self.tab_formulas = self.tabs.add("Formulas")
        self.tab_interpretar = self.tabs.add("Interpretar")
        self.tab_visual = self.tabs.add("Visualizador T3")

        self.crear_tab_inicio()
        self.crear_tab_resumen()
        self.crear_tab_formulas()
        self.crear_tab_interpretar()
        self.crear_tab_visualizador()

    def selector_tema(self, parent, row=0, column=0):
        frame = ctk.CTkFrame(parent)
        frame.grid(row=row, column=column, sticky="ew", padx=10, pady=10)
        frame.grid_columnconfigure(1, weight=1)

        label = ctk.CTkLabel(frame, text="Tema:")
        label.grid(row=0, column=0, padx=10, pady=10)

        combo = ctk.CTkComboBox(
            frame,
            values=list(TEMAS.keys()),
            command=self.cambiar_tema
        )
        combo.set(self.tema_actual_nombre)
        combo.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        return combo

    def cambiar_tema(self, nombre):
        self.tema_actual_nombre = nombre
        self.tema_actual = TEMAS[nombre]

        self.actualizar_resumen()
        self.actualizar_formulas()
        self.actualizar_interpretacion()

    def crear_tab_inicio(self):
        self.tab_inicio.grid_columnconfigure(0, weight=1)

        texto = """
Bienvenida al asistente visual de Algebra II.

Esta version añade una interfaz con pestañas para estudiar:

- Tema 1: formas bilineales y formas cuadraticas.
- Tema 2: espacios vectoriales euclideos.
- Tema 3: espacios afines y geometria afin.

La parte mas importante nueva es el visualizador del Tema 3, donde puedes ver:

- puntos,
- vectores,
- rectas,
- planos,
- proyecciones,
- distancia punto-recta,
- distancia punto-plano.

Idea clave del Tema 3:

Recta  -> usa vector director.
Plano  -> usa vector normal.
Distancia -> busca siempre la direccion perpendicular.
"""

        label = ctk.CTkLabel(
            self.tab_inicio,
            text=texto,
            justify="left",
            font=("Arial", 16)
        )
        label.grid(row=0, column=0, sticky="n", padx=30, pady=30)

    def crear_tab_resumen(self):
        self.tab_resumen.grid_columnconfigure(0, weight=1)
        self.tab_resumen.grid_rowconfigure(1, weight=1)

        self.selector_tema(self.tab_resumen)

        self.resumen_textbox = ctk.CTkTextbox(
            self.tab_resumen,
            wrap="word",
            font=("Consolas", 14)
        )
        self.resumen_textbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.actualizar_resumen()

    def actualizar_resumen(self):
        if not hasattr(self, "resumen_textbox"):
            return

        self.resumen_textbox.delete("1.0", "end")
        self.resumen_textbox.insert("1.0", self.tema_actual.get("resumen", "Sin resumen."))

    def crear_tab_formulas(self):
        self.tab_formulas.grid_columnconfigure(0, weight=1)
        self.tab_formulas.grid_columnconfigure(1, weight=2)
        self.tab_formulas.grid_rowconfigure(1, weight=1)

        self.selector_tema(self.tab_formulas)

        self.lista_formulas = ctk.CTkScrollableFrame(self.tab_formulas)
        self.lista_formulas.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.formula_textbox = ctk.CTkTextbox(
            self.tab_formulas,
            wrap="word",
            font=("Consolas", 14)
        )
        self.formula_textbox.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.actualizar_formulas()

    def actualizar_formulas(self):
        if not hasattr(self, "lista_formulas"):
            return

        for widget in self.lista_formulas.winfo_children():
            widget.destroy()

        formulas = self.tema_actual.get("formulas", [])

        if not formulas:
            self.formula_textbox.delete("1.0", "end")
            self.formula_textbox.insert("1.0", "Este tema no tiene formulas.")
            return

        for i, formula in enumerate(formulas):
            boton = ctk.CTkButton(
                self.lista_formulas,
                text=formula["nombre"],
                command=lambda f=formula: self.mostrar_formula(f),
                anchor="w"
            )
            boton.pack(fill="x", padx=5, pady=4)

        self.mostrar_formula(formulas[0])

    def mostrar_formula(self, formula):
        texto = f"{formula['nombre']}\n"
        texto += "=" * 80 + "\n\n"
        texto += f"Formula/regla:\n{formula.get('formula', '')}\n\n"
        texto += f"Uso:\n{formula.get('uso', '')}\n\n"

        if "cuando_usarla" in formula:
            texto += "Cuando usarla:\n"
            for item in formula["cuando_usarla"]:
                texto += f"- {item}\n"
            texto += "\n"

        if "detalles" in formula:
            texto += "Detalles:\n"
            for item in formula["detalles"]:
                texto += f"- {item}\n"

        self.formula_textbox.delete("1.0", "end")
        self.formula_textbox.insert("1.0", texto)

    def crear_tab_interpretar(self):
        self.tab_interpretar.grid_columnconfigure(0, weight=1)
        self.tab_interpretar.grid_columnconfigure(1, weight=2)
        self.tab_interpretar.grid_rowconfigure(1, weight=1)

        self.selector_tema(self.tab_interpretar)

        self.lista_interpretacion = ctk.CTkScrollableFrame(self.tab_interpretar)
        self.lista_interpretacion.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.interpretacion_textbox = ctk.CTkTextbox(
            self.tab_interpretar,
            wrap="word",
            font=("Consolas", 14)
        )
        self.interpretacion_textbox.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.actualizar_interpretacion()

    def actualizar_interpretacion(self):
        if not hasattr(self, "lista_interpretacion"):
            return

        for widget in self.lista_interpretacion.winfo_children():
            widget.destroy()

        guias = self.tema_actual.get("interpretacion_enunciados", [])

        if not guias:
            self.interpretacion_textbox.delete("1.0", "end")
            self.interpretacion_textbox.insert(
                "1.0",
                "Este tema no tiene guia de interpretacion de enunciados."
            )
            return

        for guia in guias:
            boton = ctk.CTkButton(
                self.lista_interpretacion,
                text=guia["palabra_clave"],
                command=lambda g=guia: self.mostrar_guia(g),
                anchor="w"
            )
            boton.pack(fill="x", padx=5, pady=4)

        self.mostrar_guia(guias[0])

    def mostrar_guia(self, guia):
        texto = f"{guia['palabra_clave'].upper()}\n"
        texto += "=" * 80 + "\n\n"

        texto += "Que significa:\n"
        texto += guia["que_significa"] + "\n\n"

        texto += "Que suele pedir:\n"
        for item in guia["que_suele_pedir"]:
            texto += f"- {item}\n"

        texto += "\nOperaciones recomendadas:\n"
        for item in guia["operaciones_recomendadas"]:
            texto += f"- {item}\n"

        texto += "\nPista de examen:\n"
        texto += guia["pista_examen"]

        self.interpretacion_textbox.delete("1.0", "end")
        self.interpretacion_textbox.insert("1.0", texto)

    def crear_tab_visualizador(self):
        self.tab_visual.grid_columnconfigure(0, weight=0)
        self.tab_visual.grid_columnconfigure(1, weight=1)
        self.tab_visual.grid_rowconfigure(0, weight=1)

        panel = ctk.CTkFrame(self.tab_visual)
        panel.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        grafico_frame = ctk.CTkFrame(self.tab_visual)
        grafico_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        grafico_frame.grid_rowconfigure(0, weight=3)
        grafico_frame.grid_rowconfigure(1, weight=1)
        grafico_frame.grid_columnconfigure(0, weight=1)

        self.grafico_frame = grafico_frame

        ctk.CTkLabel(
            panel,
            text="Visualizador Tema 3",
            font=("Arial", 18, "bold")
        ).pack(padx=10, pady=10)

        self.tipo_visual = ctk.CTkComboBox(
            panel,
            values=[
                "Punto + vector",
                "Recta",
                "Plano",
                "Punto + recta",
                "Punto + plano"
            ]
        )
        self.tipo_visual.set("Punto + recta")
        self.tipo_visual.pack(fill="x", padx=10, pady=10)

        self.entrada_punto = self.crear_entrada(panel, "Punto P", "1,1,1")
        self.entrada_vector = self.crear_entrada(panel, "Vector v", "2,0,1")
        self.entrada_punto_recta = self.crear_entrada(panel, "Punto recta P0", "1,-1,-2")
        self.entrada_director = self.crear_entrada(panel, "Vector director u", "1,2,2")
        self.entrada_normal = self.crear_entrada(panel, "Normal plano n", "1,1,1")
        self.entrada_d = self.crear_entrada(panel, "Plano d: n·X=d", "0")

        boton = ctk.CTkButton(panel, text="Dibujar", command=self.dibujar_visualizacion)
        boton.pack(fill="x", padx=10, pady=15)

        ayuda = """
Formato:
- Escribe vectores como: 1,2,3
- Plano: n=(a,b,c), d
- Recta: P0 y u

Ejemplos:
P = 1,1,1
P0 = 1,-1,-2
u = 1,2,2
n = 1,1,1
d = 0
"""
        ctk.CTkLabel(panel, text=ayuda, justify="left").pack(padx=10, pady=10)

        self.plot_area = ctk.CTkFrame(grafico_frame)
        self.plot_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.explicacion_visual = ctk.CTkTextbox(
            grafico_frame,
            wrap="word",
            font=("Consolas", 13),
            height=160
        )
        self.explicacion_visual.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.dibujar_visualizacion()

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
            "d": self.entrada_d.get()
        }

    def dibujar_visualizacion(self):
        try:
            tipo = self.tipo_visual.get()
            datos = self.obtener_datos_visualizador()

            fig, explicacion = generar_escena(tipo, datos)

            for widget in self.plot_area.winfo_children():
                widget.destroy()

            self.canvas_actual = FigureCanvasTkAgg(fig, master=self.plot_area)
            self.canvas_actual.draw()
            self.canvas_actual.get_tk_widget().pack(fill="both", expand=True)

            self.explicacion_visual.delete("1.0", "end")
            self.explicacion_visual.insert("1.0", explicacion)

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = AlgebraApp()
    app.mainloop()