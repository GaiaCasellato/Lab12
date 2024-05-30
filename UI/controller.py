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
        self._view.txt_result.controls.clear()
        self._model.creaGrafo(self._view.ddcountry.value, self._view.ddyear.value)
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di vertici :{self._model.getNumNodes()} Numero di archi:{self._model.getNumEdges()}"))

        self._view.update_page()

    def handle_volume(self, e):
        self._view.txtOut2.controls.clear()
        volumi = self._model.calculate_sales_volume()
        volumi_sortati = sorted(volumi.items(), key=lambda x: x[1], reverse=True)
        for retailer, volume in volumi_sortati:
            if volume != 0:
                self._view.txtOut2.controls.append(ft.Text(f"{retailer.Retailer_name} --> {volume}"))
        self._view.update_page()

    def handle_path(self, e):
        self._view.txtOut3.controls.clear()
        numero = int(self._view.txtN.value)
        if numero <= 1:
            self._view.create_alert("Il numero inserito è troppo piccolo coglione.")
            return
        ottimo, peso= self._model.getPercorsoPesoMax(numero)
        self._view.txtOut3.controls.append(ft.Text(f"Peso cammino massimo : {peso}."))
        for i in range(len(ottimo)-1):
            self._view.txtOut3.controls.append(ft.Text(f"{ottimo[i].Retailer_name} --->{ottimo[i+1].Retailer_name} "))
        self._view.update_page()

