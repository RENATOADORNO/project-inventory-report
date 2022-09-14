from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_page = 0

    def __next__(self):
        try:
            data_inventory = self.data[self.current_page]
        except IndexError:
            raise StopIteration()
        else:
            self.current_page += 1
            return data_inventory
