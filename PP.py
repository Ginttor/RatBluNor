from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyApp(App):
    def build(self):
        # Layout principal horizontal
        layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        # Sección izquierda: mensaje
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.label = Label(
            text="Hello World",
            font_size=48,
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))  # Ajustar texto al tamaño
        left_layout.add_widget(self.label)
        left_layout.add_widget(Widget())  # Espaciador flexible
        layout.add_widget(left_layout)

        # Sección derecha: botones
        right_layout = BoxLayout(orientation='vertical', size_hint=(0.3, 1), spacing=10)
        btn1 = Button(text="Cambiar a Español", font_size=20)
        btn2 = Button(text="Cambiar a Kivy", font_size=20)

        # Vincular acciones a los botones
        btn1.bind(on_press=self.cambiar_a_espanol)
        btn2.bind(on_press=self.cambiar_a_kivy)

        right_layout.add_widget(btn1)
        right_layout.add_widget(btn2)
        layout.add_widget(right_layout)

        return layout

    def cambiar_a_espanol(self, instance):
        self.label.text = "¡Hola Mundo!"

    def cambiar_a_kivy(self, instance):
        self.label.text = "Hello Kivy!"

# Ejecutar la aplicación
MyApp().run()   