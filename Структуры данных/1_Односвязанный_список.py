"""Описание односвязанного списка."""


class linkedList:
    """Создание класса списка."""

    def __init__(self, head=None, tail=None, lenght=0):
        """Объявление атрибутов класса."""
        self.head = head
        self.tail = tail
        self.lenght = lenght

    class Node:
        """Класс узла списка."""

        def __init__(self, element, next_node=None):
            """Объявление атрибутов класса."""
            self.element = element
            self.next_node = next_node

    def len_list(self):
        """Метод для вывода длинны списка."""
        print(self.lenght)

    def output(self):
        """Метод для вывода элементов списка через запятую."""
        if self.lenght == 0:
            print('Список отсутствует!')
        else:
            node = self.head
            while node.next_node:
                print(node.element, end=', ')
                node = node.next_node
            print(node.element)

    def push_back(self, element):
        """Добавление элемента в конец списка."""
        node = self.Node(element)
        if self.lenght == 0:
            self.head = node
            self.tail = node
            self.lenght += 1
            return element
        if self.lenght == 1:
            self.head.next_node = node
            self.tail = node
            self.lenght += 1
            return element
        self.tail.next_node = node
        self.tail = node
        self.lenght += 1
        return element

    def push_front(self, element):
        """Добавление элемента в начало списка."""
        node = self.Node(element)
        if self.lenght == 0:
            self.head = node
            self.tail = node
            self.lenght += 1
            return element
        if self.lenght == 1:
            node.next_node = self.tail
            self.head = node
            self.lenght += 1
            return element
        node.next_node = self.head
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
        else:
            i = 0
            node = self.head
            prev_node = None
            while i < index:
                prev_node = node
                node = node.next_node
                i += 1
            prev_node.next_node = self.Node(element, next_node=node)
            self.lenght += 1

    def __getitem__(self, index):
        """Поиск элемента по индексу."""
        if index < 0 or index > self.lenght - 1:
            print('Индекс не существует.')
            exit()
        if index == 0:
            return self.head.element
        if index == self.lenght - 1:
            return self.tail.element
        i = 0
        node = self.head
        prev_node = None
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        return prev_node.next_node.element

    def delete_front(self):
        """Удаление элемента из начала списка."""
        node = self.head
        self.head = self.head.next_node
        del node
        self.lenght -= 1

    def __delitem__(self, index):
        """Удаление элемента по индексу."""
        if index < 0 or index > self.lenght - 1:
            print('Индекс не существует!')
            exit()
        if index == 0:
            self.delete_front()
        else:
            i = 0
            node = self.head
            prev_node = None
            while i < index:
                prev_node = node
                node = node.next_node
                i += 1
            prev_node.next_node = node.next_node
            if index == self.lenght - 1:
                self.tail = prev_node
            del node
            self.lenght -= 1


def main():
    """Функция для проверки односвязанного списка."""
    a = linkedList()
    a.output()
    a.len_list()
    print('\n')
    a.push_back(432)
    a.output()
    a.len_list()
    print('\n')
    a.push_back(555)
    a.push_back(41232)
    a.push_back(4343)
    a.output()
    a.len_list()
    print('\n')
    a.push_front(999)
    a.output()
    a.len_list()
    print('\n')
    a.push_front(123)
    a.output()
    a.len_list()
    print('\n')
    a.push_front(654)
    a.push_front(345)
    a.push_front(6256)
    a.output()
    a.len_list()
    print('\n')
    a.push_index(3214, 5)
    a.push_index(95432, 0)
    a.push_index(43, 10)
    a.output()
    a.len_list()
    print('\n')
    print(a[0])
    print(a[11])
    print(a[5])
    print('\n')
    a.delete_front()
    a.delete_front()
    a.delete_front()
    a.output()
    a.len_list()
    print('\n')
    del (a[0])
    a.output()
    a.len_list()
    del (a[5])
    a.output()
    a.len_list()
    del (a[6])
    a.output()
    a.len_list()
    a.push_back(32)
    a.output()
    a.len_list()


if __name__ == '__main__':
    main()
