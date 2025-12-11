import flet as ft

def main(page: ft.Page):
    page.title = "Conversor de Monedas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Tasas de conversión (ejemplo)
    tasas = {
        "USD a MXN": 17.50,
        "MXN a USD": 0.057,
        "USD a EUR": 0.92,
        "EUR a USD": 1.09,
        "MXN a EUR": 0.053,
        "EUR a MXN": 18.90
    }
    
    # Campo de entrada
    cantidad_input = ft.TextField(
        label="Cantidad",
        value="0",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300
    )
    
    # Menú desplegable para seleccionar conversión
    conversion_dropdown = ft.Dropdown(
        label="Tipo de conversión",
        width=300,
        options=[
            ft.dropdown.Option("USD a MXN"),
            ft.dropdown.Option("MXN a USD"),
            ft.dropdown.Option("USD a EUR"),
            ft.dropdown.Option("EUR a USD"),
            ft.dropdown.Option("MXN a EUR"),
            ft.dropdown.Option("EUR a MXN")
        ],
        value="USD a MXN"
    )
    
    # Texto para mostrar resultado
    resultado = ft.Text("0.00", size=40, weight=ft.FontWeight.BOLD)
    
    def convertir_click(e):
        try:
            cantidad = float(cantidad_input.value)
            tipo = conversion_dropdown.value
            tasa = tasas[tipo]
            convertido = cantidad * tasa
            resultado.value = f"{convertido:.2f}"
            resultado.update()
        except ValueError:
            resultado.value = "Error: ingresa un número válido"
            resultado.update()
    
    # Botón de conversión
    boton_convertir = ft.ElevatedButton(
        text="Convertir",
        icon=ft.Icons.CURRENCY_EXCHANGE,
        on_click=convertir_click
    )
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column(
                    [
                        ft.Text("💱 Conversor de Monedas", size=30, weight=ft.FontWeight.BOLD),
                        cantidad_input,
                        conversion_dropdown,
                        boton_convertir,
                        ft.Divider(height=20, color="transparent"),
                        ft.Text("Resultado:", size=20),
                        resultado
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
                padding=20,
                alignment=ft.alignment.center
            ),
            expand=True
        )
    )

ft.app(main)