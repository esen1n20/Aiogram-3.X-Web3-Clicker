import os
import flet as ft

def main(page: ft.Page):  # Removed async keyword
    page.title = "MAKCOH CLICKER"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#663300"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Added CrossAxisAlignment.CENTER
    page.fonts = {"HefferCyr": "fonts/HefferCyr.otf"}
    page.theme = ft.Theme(font_family="HefferCyr")

    score = ft.Text(value="0", size=150, data=0)
    score_counter = ft.Text(
        size=50,
        animate_opacity=ft.Animation(duration=500, curve=ft.AnimationCurve.BOUNCE_IN),
    )

    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets", "mandarin.png"))

    image = ft.Image(
        src=image_path,
        fit=ft.ImageFit.CONTAIN
    )

    def score_up(e): # Removed async keyword
        score.data += 1
        score.value = str(score.data)
        page.update() # Use page.update() instead of await page.update_async


    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[image, score_counter, score] # Added score to the stack
            ),
            on_click=score_up,
            margin=ft.margin.only(bottom=30), # use flet.margin
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=None, port=8080)