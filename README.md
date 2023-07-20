# Полезное
## Структуры данных
### 1. [Односвязный список](https://github.com/VyacheslavRoev/useful/blob/main/Структуры%20данных/1_Односвязанный_список.py)
Структура данных, состоящая из узлов, в каждом из которых есть ссылка на следующий.


Описан при помощи создания класса LinkedList, свойствами которого являются голова списка(head) и хвост(tail), по умолчанию отсутствуют.
А также длинна списка(lenght), по умолчанию = 0.


Также внутри класса LinkedList описан класс Node, для создания узла списка. Его свойствами являются значение элемента(element) и ссылка на следующий узел(next_node).

Для работы со списком необходимо создать экземпляр класса LinkedList:
```
a = LinkedList()
```

Методы LinkedList:
- a.push_front(element) - добавление элемента в начало списка
- a.push_back(element) - добавление элемента в конец списка
- a.push_index(element, index) - добавление элемента по индексу
- a.len_list() - вывод длинны списка
- a.output() - вывод списка
- a[index] - поиск элемента по индексу
- a.delete_front() - удаление первого элемента списка
- del a[index] - удаление элемента по индексу


### 2. [Двусвязный список](https://github.com/VyacheslavRoev/useful/blob/main/Структуры%20данных/2_Двусвязный_список.py)
Структура данных, состоящая из узлов, в каждом из которых есть ссылка на следующий и предыдущий.


Описан при помощи создания класса DolbyLinkedList, свойствами которого являются голова списка(head) и хвост(tail), по умолчанию отсутствуют.
А также длинна списка(lenght), по умолчанию = 0.


Также внутри класса DolbyLinkedList описан класс Node, для создания узла списка. Его свойствами являются значение элемента(element), ссылка на предыдущий узел(prev_node) и ссылка на следующий(next_node)

Для работы со списком необходимо создать экземпляр класса DolbyLinkedList:
```
a = DolbyLinkedList()
```


Методы DolbyLinkedList:
- a.push_front(element) - добавление элемента в начало списка
- a.push_back(element) - добавление элемента в конец списка
- a.push_index(element, index) - добавление элемента по индексу
- a.len_list() - вывод длинны списка
- a.out_front() - вывод списка начиная с первого элемента
- a.out_back() - вывод списка в обратном порядке
- a[index] - поиск элемента по индексу
- a.delete_front() - удаление первого элемента списка
- a.delete_back() - удаление последнего элемента списка
- del a[index] - удаление элемента по индексу


## Сортировка

### 1. [Сортировка выбором](https://github.com/VyacheslavRoev/useful/blob/main/Сортировка/1_Сортировка_выбором.py)

 Алгоритм без дополнительного выделения памяти
 
```
Шаги алгоритма:

1. Находим номер минимального значения в текущем списке.
2. Производим обмен этого значения со значением первой неотсортированной позиции (обмен не нужен, если минимальный элемент уже находится на данной позиции).
3. Теперь сортируем хвост списка, исключив из рассмотрения уже отсортированные элементы.
```

### 2. [Пузырьковая сортировка](https://github.com/VyacheslavRoev/useful/blob/main/Сортировка/2_Пузырьковая_сортировка.py)

Алгоритм:


Сначала сравниваются первые два элемента списка. Если первый элемент больше, они меняются местами.
Если они уже в нужном порядке, оставляем их как есть. Затем переходим к следующей паре элементов,
сравниваем их значения и меняем местами при необходимости. Этот процесс продолжается до последней пары элементов в списке.


Чтобы остановить алгоритм по окончании сортировки, нужно ввести переменную-флаг.
Когда значения меняются местами, устанавливаем флаг в значение True, чтобы повторить процесс сортировки.
Если перестановок не произошло, флаг остаётся False и алгоритм останавливается.


### 3. [Сортировка слиянием](https://github.com/VyacheslavRoev/useful/blob/main/Сортировка/3_Сортировка_слиянием.py)

Алгоритм:

```
1. Массив разбивается на две части примерно одинакового размера.
2. Если в каком-то из получившихся подмассивов больше одного элемента,
то для него рекурсивно запускается сортировка по этому же алгоритму, начиная с пункта 1.
3. Два упорядоченных массива соединяются в один.
Условие остановки рекурсии — массив из одного элемента. Он не нуждается в сортировке, поэтому это базовый случай.
```


### 3. [Быстрая сортировка](https://github.com/VyacheslavRoev/useful/blob/main/Сортировка/4_Быстрая_сортировка.py)

Алгоритм:

```
1. Выбрать опорный элемент из массива. Обычно опорным элементом является средний элемент.
2. Разделить массив на два подмассива: элементы меньше опорного и элементы больше опорного.
3. Рекурсивно применить сортировку к двум подмассивам.
```