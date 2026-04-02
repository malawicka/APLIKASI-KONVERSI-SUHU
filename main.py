from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout

class KonversiSuhuApp(App):
    def build(self):
        self.title = 'KONVERSI SUHU'
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # GridLayout untuk menyusun elemen-elemen
        grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=250)  # Increased height

        # Dropdown untuk satuan suhu masukan
        self.input_unit_label = Label(text='Pilih suhu masukan:', size_hint_y=None, height=44, color=(1, 1, 1, 1))  # White text color
        self.input_unit_dropdown = DropDown()

        input_units = ['Celcius', 'Fahrenheit', 'Kelvin', 'Reamur']
        for unit in input_units:
            btn = Button(text=unit, size_hint_y=None, height=44, background_color=(0.8, 0.2, 0.8, 1))  # Lighter purple button color
            btn.bind(on_release=lambda btn: self.input_unit_dropdown.select(btn.text))
            self.input_unit_dropdown.add_widget(btn)

        self.input_unit_button = Button(text='Pilih', size_hint_y=None, height=44, background_color=(0.6, 0.1, 0.6, 1))  # Darker purple button color
        self.input_unit_button.bind(on_release=self.input_unit_dropdown.open)
        self.input_unit_dropdown.bind(on_select=lambda instance, x: setattr(self.input_unit_button, 'text', x))

        # Dropdown untuk satuan suhu keluaran
        self.output_unit_label = Label(text='Pilih suhu keluaran:', size_hint_y=None, height=44, color=(1, 1, 1, 1))  # White text color
        self.output_unit_dropdown = DropDown()

        output_units = ['Celcius', 'Fahrenheit', 'Kelvin', 'Reamur']
        for unit in output_units:
            btn = Button(text=unit, size_hint_y=None, height=44, background_color=(0.8, 0.2, 0.8, 1))  # Lighter purple button color
            btn.bind(on_release=lambda btn: self.output_unit_dropdown.select(btn.text))
            self.output_unit_dropdown.add_widget(btn)

        self.output_unit_button = Button(text='Pilih', size_hint_y=None, height=44, background_color=(0.6, 0.1, 0.6, 1))  # Darker purple button color
        self.output_unit_button.bind(on_release=self.output_unit_dropdown.open)
        self.output_unit_dropdown.bind(on_select=lambda instance, x: setattr(self.output_unit_button, 'text', x))

        # Input suhu
        self.input_text = TextInput(multiline=False, hint_text='Masukkan Angka', size_hint_y=None, height=44, background_color=(0.9, 0.9, 0.9, 1))  # Light gray input background

        # Label untuk menampilkan hasil konversi
        self.result_label = Label(text='Hasil:', size_hint_y=None, height=44, color=(1, 1, 1, 1))  # White text color

        # Tombol konversi
        btn_convert = Button(text='Konversi', on_press=self.convert_temperature, size_hint_y=None, height=44, background_color=(0.6, 0.1, 0.6, 1))  # Darker purple button color

        # Menambahkan elemen-elemen ke dalam GridLayout
        grid_layout.add_widget(self.input_unit_label)
        grid_layout.add_widget(self.input_unit_button)
        grid_layout.add_widget(self.output_unit_label)
        grid_layout.add_widget(self.output_unit_button)
        grid_layout.add_widget(self.input_text)
        grid_layout.add_widget(btn_convert)
        grid_layout.add_widget(self.result_label)

        # Menambahkan GridLayout ke dalam layout utama
        layout.add_widget(grid_layout)

        # Memastikan tidak ada space kosong di atas GridLayout
        layout.add_widget(BoxLayout(size_hint_y=None, height=1))

        return layout

    def convert_temperature(self, instance):
        try:
            input_temperature = float(self.input_text.text)
            input_unit = self.input_unit_button.text
            output_unit = self.output_unit_button.text

            if input_unit == output_unit:
                result_text = f'Hasil konversi: {input_temperature:.2f} {output_unit}'
            else:
                if input_unit == 'Celcius':
                    celcius = input_temperature
                elif input_unit == 'Fahrenheit':
                    celcius = (input_temperature - 32) * 5/9
                elif input_unit == 'Kelvin':
                    celcius = input_temperature - 273.15
                elif input_unit == 'Reamur':
                    celcius = input_temperature * 5/4

                if output_unit == 'Celcius':
                    result_text = f'Hasil konversi: {celcius:.2f} {output_unit}'
                elif output_unit == 'Fahrenheit':
                    result_text = f'Hasil konversi: {(celcius * 9/5) + 32:.2f} {output_unit}'
                elif output_unit == 'Kelvin':
                    result_text = f'Hasil konversi: {celcius + 273.15:.2f} {output_unit}'
                elif output_unit == 'Reamur':
                    result_text = f'Hasil konversi: {celcius * 4/5:.2f} {output_unit}'

            self.result_label.text = result_text
        except ValueError:
            self.result_label.text = 'Masukkan suhu dengan benar'

if __name__ == '__main__':
    KonversiSuhuApp().run()
