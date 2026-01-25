import flet as ft

def main(page : ft.Page):
    page.title = "Hello Flet"
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    page.window.width = 360
    page.window.height = 280

    page.add(ft.Text(
        value="Hello World",
        size=24,
        color=ft.Colors.RED
    ))

ft.run(main=main)