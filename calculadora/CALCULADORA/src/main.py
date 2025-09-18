import flet as ft
import math

def main(page: ft.Page):
    page.title = "calculadora Simple"
    page.bgcolor = ft.Colors.BLUE_400

    #Titulo
    titulo=ft.Text(
        "🧮 Calculadora basica",
        size= 28,
        color=ft.Colors.YELLOW_200,
        text_align="center",
        weight="bold"
    )
    #ENTRADAS
    num1 = ft.TextField(
        label = "Numero1",
        width= 200,
        text_style=ft.TextStyle(color=ft.Colors.YELLOW_200)

    )
    num2 = ft.TextField(
        label="Numero2",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors.YELLOW_200)
    )
    resultado = ft.Text(
        value="resultado: ",
        size = 20,
        color = ft.Colors.YELLOW_200,
        text_align="center"
    )

    #Label informativo mejorado
    info = ft.Container(
        content=ft.Text(
            "📊 Para el boton porcentaje: el campo de arriba es el numero base y el de abajo es el porcentaje (%) que quieres calcular",
            size = 13,
            color = ft.Colors.YELLOW_100,
            text_align="center",
            italic=True,
            max_lines=2,
            overflow="clip",
        ),
        alignment=ft.alignment.center,
        width=400,
        padding=5
    )

    #funcion para mostrar el resultado
    def mostrar_resultado(valor):
        resultado.value = f"resultado: {valor}"
        page.update()

    #funcionesde operaciones
    def suma(e):
        try:
            res = float(num1.value) + float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
    def resta(e):
        try:
            res = float(num1.value) - float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
    def multiplicacion(e):
        try:
            res = float(num1.value) * float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
    def division(e):
        try:
            if float(num2.value) == 0:
                mostrar_resultado("Divison por cero")
            else:
                res = float(num1.value) / float(num2.value)
                mostrar_resultado(res)
        except:
            mostrar_resultado(res)
    def porcentaje(e):
        try:
            res = (float(num1.value) * float(num2.value)) / 100
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
    def  raiz_cuadrada(e):
        try:
            res1= math.sqrt(float(num1.value))
            res2 = math.sqrt(float(num2.value))
            mostrar_resultado(f"✔{num1.value} = {res1:.2f} ✔{num2.value}= {res2:.2f}")
        except:
            mostrar_resultado("Error")
    
    #Layout general, todo centrado
    page.add(
        ft.Column(
            [
                ft.Row([titulo], alignment="center"),
                ft.Row([num1], alignment="center"),
                ft.Row([num2], alignment="center"),
                ft.Row(
                 [
                     ft.ElevatedButton("➕ sumar", on_click=suma, width=120),
                     ft.ElevatedButton("➖ Restar", on_click=resta, width=120),
                     ft.ElevatedButton("✖ Multiplicar", on_click=multiplicacion, width=120),
                 ],
                 spacing=10,
                 alignment="center"
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("➗ Division", on_click=division, width=120),
                        ft.ElevatedButton("📊 Porcentaje", on_click= porcentaje, width=120),
                        ft.ElevatedButton("√ Raiz Cuadrada", on_click=raiz_cuadrada, width=120),
                    ],
                    spacing=10,
                    alignment="center"
                ),
                ft.Row([resultado], alignment="center"),
                ft.Row([info], alignment="center"), #label informativo al final y centrado
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True,
            spacing=15
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)
