# Задание 10: Написать связный список 
# 1.Расширить связный список Создайте и опишите метод remove. 
# Создайте и опишите метод append. Подумайте: какова временна́я 
# сложность метода append? Скорее всего, вы создали метод append 
# со сложностью O(n).  Если вы добавите в класс LinkedList 
# некую переменную, то сможете сделать его со сложностью O(1). 
# Будьте внимательны! Чтобы сделать это по-настоящему правильно, 
# вам нужно рассмотреть несколько специальных случаев, 
# которые могут потребовать модификации метода add. 
# Подумайте: какова временна́я сложность метода size? Как 
# можно его оптимизировать? Создайте и опишите метод pop.   
# Протестируйте свой связный список.

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.size = 0     

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  
            self.tail = new_node  
        self.size += 1  

    def remove(self, data):
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous is None:  
                    self.head = current.next
                else:
                    previous.next = current.next  
                if current == self.tail:  
                    self.tail = previous
                self.size -= 1 
                return True
            previous = current
            current = current.next
        return False  

    def pop(self):
        if self.size == 0:
            return None
        if self.size == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return data
        current = self.head
        while current.next != self.tail: 
            current = current.next
        data = self.tail.data
        current.next = None
        self.tail = current
        self.size -= 1 
        return data

    def get_size(self):
        return self.size

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(map(str, elements))


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print(linked_list)  

print("Размер списка:", linked_list.get_size()) 

linked_list.remove(2)
print(linked_list)  

popped_value = linked_list.pop()
print("Удаленный элемент:", popped_value)
print(linked_list)
print("Размер списка:", linked_list.get_size())
