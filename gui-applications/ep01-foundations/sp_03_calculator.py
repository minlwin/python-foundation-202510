import flet as ft

def InputControl(name : str, control : ft.TextField):
    control.hint_text = f"Enter {name}"
    return ft.Column(
        controls=[
            ft.Text(value=name),
            control
        ]
    )

def main(page : ft.Page):
    page.title = "Simple Calculator"
    page.window.width = 580
    page.window.height = 420

    output = ft.Text(
        value="0", 
        size=36
    )

    input1 = ft.TextField(
        label="Input 1",
        expand=True
    )
    input2 = ft.TextField(
        label="Input 2",
        expand=True
    )

    def calculate(operator : str):

        if input1.value == "":
            output.value = "Please enter input 1"
            return
        
        if input2.value == "":
            output.value = "Please enter input 2"
            return

        value1 = int(input1.value)
        value2 = int(input2.value)

        result = 0

        if operator == "+":
            result = value1 + value2
        elif operator == "-" :      
            result = value1 - value2
        elif operator == "*" :      
            result = value1 * value2
        elif operator == "/" :       
            result = value1 / value2
        elif operator == "%" :       
            result = value1 % value2
        
        output.value = f"Result is {result}"

    page.padding = ft.Padding(left=48, right=48)

    page.add(ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        spacing=24,
        controls=[
            ft.Text(
                value="Simple Calculator", 
                size=36, 
                weight=ft.FontWeight.W_600
            ),
            ft.Row(
                controls=[
                    input1,
                    input2
                ],
                col=2
            ),
            ft.Row(
                controls=[
                    ft.Button(content="+", height=48, on_click=lambda e : calculate("+"), expand=True),
                    ft.Button(content="-", height=48, on_click=lambda e : calculate("-"), expand=True),
                    ft.Button(content="*", height=48, on_click=lambda e : calculate("*"), expand=True),
                    ft.Button(content="/", height=48, on_click=lambda e : calculate("/"), expand=True),
                    ft.Button(content="%", height=48, on_click=lambda e : calculate("%"), expand=True),
                ]
            ),
            output
        ]
    ))



ft.run(main=main)