import flet as ft
import math

def main(page: ft.page):
    page.title = "calculadora simple"
    page.bgcolor = ft.colors.BLUE_800

   # TITULO
    titulo = ft.text(
            "🧮 calculadora basica",
            size=28,
            color=ft.colors.YELLOW_100,
            text_align="center",
            weight="bold"
    )

    # entradas
    num1 = ft.TextField(
        label="numero 1",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors.BLUE_GREY_200)
    )
    num2 = ft.TextField(
        label="numero 2",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors.INVERSE_PRIMARY)
    )
    resultado = ft.Text(
        value="resultado",
        size=20,
        color=ft.Colors.DEEP_ORANGE_ACCENT_700,
        text_align="center"
    )

    # label informativo mejorado
    info = ft.Container(
        content=ft.text(
            "📊 para el boton de porcentaje: el campo de arriba es el numero base y el de abajo es el porcentaje (%) que quieres calcular"
        )
    )