import flet as ft
from dataclasses import field
from decimal import Decimal

def Display(output : ft.Text):
    output.size = 48
    output.color = ft.Colors.WHITE
    return ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=output,
                bgcolor=ft.Colors.BLACK,
                padding=ft.Padding.all(12),
                alignment=ft.Alignment.CENTER_RIGHT,
                border_radius=8
            )
        ],
        expand=True
    )

@ft.control
class BaseButton(ft.Button):
    expand : int = field(default_factory=lambda : 1)
    col: int = field(default_factory=lambda : 3)
    height: int = field(default_factory=lambda : 80)
    style: ft.ButtonStyle = field(default_factory=lambda : ft.ButtonStyle(
        text_style=ft.TextStyle(size=18)
    ))

@ft.control
class DigitButton(BaseButton):
    bgcolor : ft.Colors = ft.Colors.WHITE_10
    color : ft.Colors = ft.Colors.BLACK

@ft.control
class ActionButton(BaseButton):
    bgcolor : ft.Colors  = ft.Colors.ORANGE
    color : ft.Colors  = ft.Colors.WHITE

@ft.control
class SpecialActionButton(BaseButton):
    bgcolor : ft.Colors  = ft.Colors.BLUE_GREY
    color : ft.Colors  = ft.Colors.WHITE

def application(page : ft.Page):
    page.title = "Calculator"
    page.window.width = 400
    page.window.height = 600

    output = ft.Text(value="0")

    state = {
        "prev_value" : None,
        "last_ope" : None,
        "replace_output" : True
    }

    def press_number(event : ft.Event[ft.Button]):
        if state["replace_output"] :
            output.value = event.control.content
            state["replace_output"] = False
        else :
            output.value = f"{output.value}{event.control.content}"
    
    def clear(event : ft.Event[ft.Button]):
        output.value = "0"
        state["last_ope"] = None
        state["prev_value"] = None
        state["replace_output"] = True

    def plus_minus(event : ft.Event[ft.Button]):
        value = output.value
        if value != "0":
            if value.startswith("-"):
                output.value = value[1:]
            else :
                output.value = "-" + value 
        state["replace_output"] = False

    def do_decimal(event : ft.Event[ft.Button]):
        if "." not in output.value:
            output.value = f"{output.value}."
        state["replace_output"] = False

    def press_operator(event : ft.Event[ft.Button]):
        if state["prev_value"] != None and state["last_ope"] != None:
            calculate()
        state["prev_value"] = output.value
        state["last_ope"] = event.control.content
        state["replace_output"] = True

    def press_equal(event : ft.Event[ft.Button]):
        if state["prev_value"] != None and state["last_ope"] != None:
            calculate()
        state["prev_value"] = None
        state["last_ope"] = None
        state["replace_output"] = True

    def calculate():
        digit1 = Decimal(state["prev_value"])
        digit2 = Decimal(output.value)
        result = Decimal(0)
        match state["last_ope"]:
            case "+" : result = digit1 + digit2
            case "-" : result = digit1 - digit2
            case "*" : result = digit1 * digit2
            case "/" : result = digit1 / digit2
            case "%" : result = digit1 % digit2
        output.value = str(result)

    page.add(ft.Column(
        expand=True,
        spacing=8,
        controls=[
            Display(output),
            ft.ResponsiveRow(
                controls=[
                    SpecialActionButton(content="AC", on_click=clear),
                    SpecialActionButton(content="+/-", on_click=plus_minus),
                    SpecialActionButton(content="%", on_click=press_operator),
                    ActionButton(content="/", on_click=press_operator),
                    DigitButton(content="7", on_click=press_number),
                    DigitButton(content="8", on_click=press_number),
                    DigitButton(content="9", on_click=press_number),
                    ActionButton(content="*", on_click=press_operator),
                    DigitButton(content="4", on_click=press_number),
                    DigitButton(content="5", on_click=press_number),
                    DigitButton(content="6", on_click=press_number),
                    ActionButton(content="-", on_click=press_operator),
                    DigitButton(content="1", on_click=press_number),
                    DigitButton(content="2", on_click=press_number),
                    DigitButton(content="3", on_click=press_number),
                    ActionButton(content="+", on_click=press_operator),
                    DigitButton(content="0", col=6, on_click=press_number),
                    DigitButton(content=".", on_click=do_decimal),
                    ActionButton(content="=", on_click=press_equal)
                ],
            )
        ]
    ))

ft.run(application)