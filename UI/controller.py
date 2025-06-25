import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_DD_metodo(self):
        lista_metodi = self._model.fillDDmetodo()
        self._view._ddmetodo.options.clear()

        for a in lista_metodi:
            self._view._ddmetodo.options.append(ft.dropdown.Option(
                text=a))
        self._view.update_page()

    def fill_DD_anno(self):
        lista_anni = self._model.fillDDanno()
        self._view._ddyear.options.clear()

        for a in lista_anni:
            self._view._ddyear.options.append(ft.dropdown.Option(
                text=a))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view._ddyear.value
        metodo = self._view._ddmetodo.value
        numeroS = self._view._txtS.value

        # se è un dropdown --> is None, altrimenti ""
        if (anno is None):
            self._view.txt_result.controls.append(ft.Text("Devi selezionare un anno dal menù."))
            self._view.update_page()
            return
        if (metodo is None):
            self._view.txt_result.controls.append(ft.Text("Devi selezionare un metodo di ordinazione dal menù."))
            self._view.update_page()
            return
        if (numeroS == ""):
            self._view.txt_result.controls.append(ft.Text("Devi scrivere un numero nella casella di testo."))
            self._view.update_page()
            return
        try:
            numeroS = float(numeroS)
        except:
            self._view.txt_result.controls.append(ft.Text("Deve essere un numero."))
            self._view.update_page()
            return
        if (numeroS < 0):
            self._view.txt_result.controls.append(ft.Text("Deve essere un numero positivo."))
            self._view.update_page()
            return

        # creo il grafo e i dettagli
        self._model.creaGrafo(anno, metodo, numeroS)
        n, e = self._model.graphDetails()

        # stampo i nodi e gli archi
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato."))
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {n} vertici"))
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {e} archi"))
        self._view.update_page()

    def handleProdotti(self, e):
        lista5P_redditizzi = self._model.getProdRedditizzi()
        self._view.txt_result.controls.append(ft.Text(f"I prodotti più redditizzi sono:"))
        for p in lista5P_redditizzi:
            self._view.txt_result.controls.append(ft.Text(f"Prodotto {p[0].id:<20} Archi Entranti = {p[1]:<20} Ricavo = {p[0].p_vendita_tot:<20}"))
        self._view.update_page()