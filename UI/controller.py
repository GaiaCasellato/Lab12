import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        pass

    def fillDDCountries(self):
        countries = self._model.getCountries()
        for country in countries:
            self._view.ddcountry.options.append(ft.dropdown.Option(country))
        self._view.update_page()







    def handle_graph(self, e):
        print("Sono entrato qui")
        self._view.txt_result.controls.clear()
        self._model.creaGrafo(self._view.ddcountry.value, self._view.ddyear.value)
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di vertici :{self._model.getNumNodes()} Numero di archi:{self._model.getNumEdges()}"))

        self._view.update_page()

    def handle_volume(self, e):
        volumi_sortati = self._model.calculate_sales_volume()
        for retailer, volume in volumi_sortati:
            self._view.txt_result.controls.append(ft.Text(f"{retailer} --> {volume}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
