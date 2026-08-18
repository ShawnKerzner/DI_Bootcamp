import math


class Pagination():
    def __init__(self, items=None, page_size=10):
        self.items = items
        self.page_size = page_size
        if items == None:
            self.items = []
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        starting_point = self.current_idx * self.page_size
        return self.items[starting_point: starting_point + self.page_size]

    def go_to_page(self, page_num):
        if page_num > self.total_pages:
            raise ValueError(
                "Requested page_number exceeds the amount of pages")
        elif page_num <= 0:
            raise ValueError(
                "Requested page number must be greater than 0")
        else:
            self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx + 1 > self.total_pages - 1:
            raise ValueError("You are currently on the last page")
        else:
            self.current_idx += 1
            return self

    def previous_page(self):
        if self.current_idx == 0:
            raise ValueError("You are currently on the first page")
        else:
            self.current_idx -= 1
            return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: ValueError

p.go_to_page(0)
# Raises ValueError
