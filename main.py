from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from watchdog_core import check_url

Window.clearcolor = (0.08, 0.1, 0.12, 1)

class WatchDogUI(BoxLayout):
    def _init_(self, **kwargs):
        super()._init_(orientation="vertical", padding=15, spacing=10, **kwargs)

        self.title_label = Label(
            text="[b]WatchDog — Phishing URL Detector[/b]",
            markup=True,
            font_size=18
        )
        self.add_widget(self.title_label)

        self.input = TextInput(
            hint_text="Enter URL here…",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.input)

        self.btn = Button(
            text="Scan URL",
            size_hint=(1, 0.2)
        )
        self.btn.bind(on_press=self.scan)
        self.add_widget(self.btn)

        self.result = Label(text="", markup=True)
        self.add_widget(self.result)

    def scan(self, *_):
        url = self.input.text.strip()
        if not url:
            self.result.text = "[color=orange]Enter a URL first[/color]"
            return

        verdict, reasons = check_url(url)

        colors = {
            "Probably Safe": "00ff00",
            "Suspicious": "ffff00",
            "Likely Phishing": "ff4444"
        }

        color = colors.get(verdict, "ffffff")

        text = f"[color={color}][b]{verdict}[/b][/color]\n"
        for r in reasons:
            text += f"• {r}\n"

        self.result.text = text

class WatchDog(App):
    def build(self):
        self.title = "WatchDog"
        return WatchDogUI()

if _name_ == "_main_":
    WatchDog().run()