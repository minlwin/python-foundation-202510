import flet as ft

def main(page : ft.Page) :
    page.title = "Counter"
    page.window.width = 480
    page.window.height = 360

    output = ft.Text(value="0", size=60)

    def update_count(up:bool):
        value = int(output.value)
        if up :
            value += 1
        else:
            value -= 1
        output.value = str(value)
    
    plus_btn = ft.FloatingActionButton(
        icon=ft.Icons.EXPOSURE_PLUS_1_OUTLINED,
        on_click=lambda x : update_count(True)
    )

    minus_btn = ft.FloatingActionButton(
        icon=ft.Icons.EXPOSURE_MINUS_1_ROUNDED,
        on_click=lambda x : update_count(False)
    )

    page.add(ft.Column(
        expand=True,
        spacing=16,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="Counter App",
                size=36
            ),
            ft.Row(
                controls=[
                    minus_btn,
                    output,
                    plus_btn
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=36
            )
        ]
    ))

ft.run(main=main)