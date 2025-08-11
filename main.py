from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window
from bubblesort import BubbleSort

Window.size = (700, 500)
Window.clearcolor = (0.94, 0.94, 0.96, 1) 


class SortingApp(App):
    def build(self):
        layout = FloatLayout()

        # Colors
        label_color = (0.15, 0.15, 0.15, 1)
        input_bg = (1, 1, 1, 1)
        input_fg = (0.1, 0.1, 0.1, 1)
        button_color = (0.0, 0.6, 0.55, 1)

        # Title
        layout.add_widget(Label(
            text="[b]SORTING ALGORITHM[/b]",
            markup=True,
            font_size=28,
            color=label_color,
            size_hint=(1, 0.1),
            pos_hint={"x": 0, "top": 0.98}
        ))

        # Enter the Data Label
        layout.add_widget(Label(
            text="Enter the Data",
            size_hint=(0.3, 0.08),
            pos_hint={"x": 0.05, "top": 0.88},
            color=label_color,
            font_size=18
        ))

        # Data Input
        self.data_input = TextInput(
            multiline=False,
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.81},
            background_color=input_bg,
            foreground_color=input_fg
        )
        layout.add_widget(self.data_input)

        # Input Type Spinner
        self.input_type = Spinner(
            text="Input Type",
            values=("List", "Tuple", "Dictionary", "String"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.05, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        layout.add_widget(self.input_type)

        # Sorting Order Spinner
        self.sorting_order = Spinner(
            text="Sorting Order",
            values=("Ascending", "Descending"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.375, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        layout.add_widget(self.sorting_order)

        # Algorithm Spinner
        self.algorithm = Spinner(
            text="Algorithm",
            values=("Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.70, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        layout.add_widget(self.algorithm)

        # Sort Button with direct on_press
        self.sort_button = Button(
            text="Sort",
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.58},
            background_color=button_color,
            color=(1, 1, 1, 1),
            bold=True,
            on_press=self.input_conversion  # ✅ linked function
        )
        layout.add_widget(self.sort_button)

        # Iterations Label
        layout.add_widget(Label(
            text="Iterations -",
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.48},
            color=label_color,
            font_size=16
        ))

        # Iterations Result
        self.iter_result = TextInput(
            multiline=False,
            readonly=True,
            size_hint=(0.65, 0.06),
            pos_hint={"x": 0.25, "top": 0.48},
            background_color=input_bg,
            foreground_color=input_fg
        )
        layout.add_widget(self.iter_result)

        # Output Label
        layout.add_widget(Label(
            text="Output",
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.35},
            color=label_color,
            font_size=18
        ))

        # Output Box
        self.output_box = TextInput(
            multiline=True,
            readonly=True,
            size_hint=(0.65, 0.20),
            pos_hint={"x": 0.25, "top": 0.35},
            background_color=input_bg,
            foreground_color=input_fg
        )
        layout.add_widget(self.output_box)

        return layout

    def input_conversion(self, instance):
        raw_input = self.data_input.text.strip()
        input_type = self.input_type.text  

        try:
            match input_type:
                case "List":
                    sep = raw_input.split(",")
                    data = []
                    for i in sep:
                        data.append(i.strip())

                case "Tuple":
                    sep = raw_input.split(",")
                    temp = []
                    for p in sep:
                        temp.append(p.strip())
                    data = tuple(temp)

                case "Dictionary":
                    sep = raw_input.split(",")
                    data = {}
                    for item in sep:
                        kv = item.split(":")
                        key = kv[0].strip()
                        value_str = kv[1].strip()
                        try:
                            if '.' in value_str:
                                value = float(value_str)
                            else:
                                value = int(value_str)
                        except ValueError:
                            value = value_str  # fallback to string if conversion fails
                        data[key] = value


                case "String":
                    sep = raw_input.split(",")
                    data = []
                    for i in sep:
                        data.append(i.strip())  

                    
                case _:
                    self.output_box.text = "Invalid Input Type Selected"
                    return
            order = self.sorting_order.text
            if self.algorithm.text == "Bubble Sort":
                sorter = BubbleSort(data)
                sorted_data, iterations = sorter.Bubble(order)

                self.output_box.text = str(sorted_data)
                self.iter_result.text = str(iterations)
            else:
                self.output_box.text = "Selected algorithm not implemented yet."
                self.iter_result.text = ""

        except Exception:
            self.output_box.text = "Invalid Input"
            self.iter_result.text = ""
                

if __name__ == "__main__":
    SortingApp().run()

