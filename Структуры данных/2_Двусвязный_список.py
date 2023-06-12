"""Описание двусвязного списка."""


class DolbyLinkedList():
    """Создание класса списка."""

    def __init__(self, head=None, tail=None, lenght=0):
        """Объявление атрибутов класса."""
        self.head = head
        self.tail = tail
        self.lenght = lenght

    class Node():
        """Создание класса узла списка."""

        def __init__(self, element, prev_node=None, next_node=None):
            """Объявление атрибутов класса."""
            self.element = element
            self.prev_node = prev_node
            self.next_node = next_node

    def len_list(self):
        print(self.lenght)

    def out_front(self):
        """Вывод списка с первого элемента."""
        if self.lenght == 0:
            print('Список пуст!')
        elif self.lenght == 1:
            print(self.head.element)
        else:
            node = self.head
            while node.next_node:
                print(node.element, end=', ')
                node = node.next_node
            print(node.element)

    def out_back(self):
        """Вывод списка с последнего элемента."""
        if self.lenght == 0:
            print('Список пуст!')
        elif self.lenght == 1:
            print(self.head.element)
        else:
            node = self.tail
            while node.prev_node:
                print(node.element, end=', ')
                node = node.prev_node
            print(node.element)

    def push_back(self, element):
        """Добавление элемента в конец списка."""
        if self.lenght == 0:
            node = self.Node(element)
            self.head = node
            self.tail = node
            self.lenght += 1
            return element
        if self.lenght == 1:
            node = self.Node(element, self.head)
            self.head.next_node = node
            self.tail = node
            self.lenght += 1
            return element
        node = self.Node(element, self.tail)
        self.tail.next_node = node
        self.tail = node
        self.lenght += 1
        return element

    def push_front(self, element):
        """Добавление элемента в начало списка."""
        if self.lenght == 0:
            node = self.Node(element)
            self.head = node
            self.tail = node
            self.lenght += 1
            return element
        if self.lenght == 1:
            node = self.Node(element, None, self.tail)
            self.tail.prev_node = node
            self.head = node
            self.lenght += 1
            return element
        node = self.Node(element, None, self.head)
        self.head.prev_node = node
        self.head = node
        self.lenght += 1
        return element

    def push_index(self, element, index):
        """Добавление элемента по индексу."""
        if index < 0 or index > self.lenght - 1:
            print('Индекс не существует!')
            exit()
        if index == 0:
            self.push_front(element)
        elif 0 < index <= self.lenght // 2:
            i = 0
            node = self.head
            while i < index:
                node = node.next_node
                i += 1
            node_index = self.Node(element, node.prev_node, node)
            node.prev_node.next_node = node_index
            node.prev_node = node_index
            self.lenght += 1
        else:
            i = self.lenght - 1
            node = self.tail
            while i > index:
                node = node.prev_node
                i -= 1
            node_index = self.Node(element, node.prev_node, node)
            node.prev_node.next_node = node_index
            node.prev_node = node_index
            self.lenght += 1

    def delete_front(self):
        """Удаление первого элемента."""
        node = self.head
        self.head.next_node.prev_node = None
        self.head = self.head.next_node
        del node
        self.lenght -= 1

    def delete_back(self):
        """Удаление последнего элемента."""
        node = self.tail
        self.tail.prev_node.next_node = None
        self.tail = self.tail.prev_node
        del node
        self.lenght -= 1

    def __delitem__(self, index):
        """Удаление элемента по индексу."""
        if index < 0 or index > self.lenght - 1:
            print('Индекс не существует!')
            exit()
        if index == 0:
            self.delete_front()
        elif index == self.lenght - 1:
            self.delete_back()
        elif 0 < index <= self.lenght // 2:
            i = 0
            node = self.head
            while i < index:
                node = node.next_node
                i += 1
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
            del node
            self.lenght -= 1
        else:
            i = self.lenght - 1
            node = self.tail
            while i > index:
                node = node.prev_node
                i -= 1
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
            del node
            self.lenght -= 1

    def __getitem__(self, index):
        """Вывод элемента по индексу."""
        if index < 0 or index > self.lenght - 1:
            return 'Индекс не существует!'
        if index == 0:
            return self.head.element
        if index == self.lenght - 1:
            return self.tail.element
        if 0 < index <= self.lenght // 2:
            i = 0
            node = self.head
            while i < index:
                node = node.next_node
                i += 1
            return node.element
        i = self.lenght - 1
        node = self.tail
        while i > index:
            node = node.prev_node
            i -= 1
        return node.element


def main():
    """Функция для проверки списка."""
    a = DolbyLinkedList()
    a.out_front()
    a.out_back()
    print('\n')
    a.push_back(12)
    a.push_back(332)
    a.push_back(254)
    a.push_back(1111)
    a.push_front(765)
    a.len_list()
    print('\n')
    a.push_front(876)
    a.len_list()
    a.push_front(444)
    a.push_front(9372)
    a.len_list()
    a.out_front()
    a.out_back()
    a.push_index(32134, 7)
    a.push_index(923, 4)
    a.push_index(1000, 9)
    a.push_back(999)
    a.out_front()
    a.out_back()
    a.len_list()
    print('\n')
    a.delete_front()
    a.out_front()
    a.out_back()
    a.len_list()
    print('\n')
    a.delete_front()
    a.out_front()
    a.out_back()
    a.len_list()
    print('\n')
    a.delete_front()
    a.out_front()
    a.out_back()
    a.len_list()
    a.delete_back()
    a.out_front()
    a.out_back()
    a.len_list()
    a.delete_back()
    a.out_front()
    a.out_back()
    a.len_list()
    a.delete_back()
    a.out_front()
    a.out_back()
    a.len_list()
    del a[4]
    a.out_front()
    a.out_back()
    a.len_list()
    print(a[3])


if __name__ == '__main__':
    main()
