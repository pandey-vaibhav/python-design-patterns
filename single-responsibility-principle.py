"""
Single responsibility principle: A class should have 1 reason to change
"""


# region Badcode
# class Marker:
#     def __init__(self, name: str, color: str, year: int, price: int) -> None:
#         self.name = name
#         self.color = color
#         self.year = year
#         self.price = price


# class Invoice:
#     def __init__(self, marker: Marker, quantity: int) -> None:
#         self.marker = marker
#         self.quantity = quantity

#     def calculate_total(self) -> int:
#         price = self.marker.price * self.quantity
#         return price

#     def print_invoice(self) -> None:
#         # print the invoice
#         pass

#     def save_to_database(self) -> None:
#         # save the data into database
#         pass
# endregion

# region Goodcode
class Marker:
    def __init__(self, name: str, color: str, year: int, price: int) -> None:
        self.name = name
        self.color = color
        self.year = year
        self.price = price


# Invoice only (1) holds the responsibility to generate invoice, it will
# neither print not save invoice to databse.
class Invoice:
    def __init__(self, marker: Marker, quantity: int) -> None:
        self.marker = marker
        self.quantity = quantity

    def calculate_total(self) -> int:
        price = self.marker.price * self.quantity
        return price


# InvoiceDao only (1) holds the responsiblity to save the invoice to database
class InvoiceDao:
    def __init__(self, invoice: Invoice) -> None:
        self.invoice = invoice

    def save_to_database(self) -> None:
        # save the data into database
        pass


# InvoicePrinter only (1) holds the responsibility to print the invoice
class InvoicePrinter:
    def __init__(self, invoice: Invoice) -> None:
        self.invoice = invoice

    def print_invoice(self) -> None:
        # print the invoice
        pass
# endregion
