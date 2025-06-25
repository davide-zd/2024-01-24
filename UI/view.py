import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esame 24-01-2024"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.bgcolor = "#ebf4f4"
        self._page.window_height = 800
        page.window_center()
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txt_name = None
        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 24-01-2024", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddyear = ft.Dropdown(label="Anno")
        self._ddmetodo = ft.Dropdown(label="Metodo")
        self._txtS = ft.TextField(label="Valore numerico S")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo)

        cont = ft.Container(self._ddyear, width=250, alignment=ft.alignment.top_left)
        cont2 = ft.Container(self._ddmetodo, width=250, alignment=ft.alignment.top_left)
        row1 = ft.Row([cont, cont2, self._txtS, self._btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)

        self._btnProdotti = ft.ElevatedButton(text="Calcola Prodotti Redditizzi", on_click=self._controller.handleProdotti)
        row2 = ft.Row([ft.Container(self._btnProdotti, width=250)
        ], alignment=ft.MainAxisAlignment.CENTER)

        # lancio i metodi del controller
        self._controller.fill_DD_metodo()
        self._controller.fill_DD_anno()

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()