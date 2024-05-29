from dataclasses import dataclass

@dataclass
class Retailer:
    Type : str
    Retailer_name : str
    Retailer_code : int
    Country : str


    def __hash__(self):
        return hash(self.Retailer_code)

    def __str__(self):
        return f"Il retailer {self.Retailer_name} ha il seguente codice {self.Retailer_code}"