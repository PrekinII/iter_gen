class FlatIterator:

    def __init__(self, some_list):
        self.list_of_lists = some_list

    def __iter__(self):
        self.position = 0
        self.elem_position = 0
        return self

    def __next__(self):

        if self.elem_position == len(self.list_of_lists[self.position]):
            self.position += 1
            self.elem_position = 0

        if self.position == len(self.list_of_lists):
            raise StopIteration
        item = self.list_of_lists[self.position][self.elem_position]
        self.elem_position += 1

        return item
#======= Возвращает список (т.к. я не понял изначально задание)))
    # def __next__(self):
    #     if len(self.list_of_lists) == 0:
    #         raise StopIteration
    #     while len(self.list_of_lists) != 0:
    #         self.result = self.list_of_lists.pop(0)
    #         while len(self.result) != 0:
    #             self.item.append(self.result.pop(0))
    #     return self.item
#=========


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
