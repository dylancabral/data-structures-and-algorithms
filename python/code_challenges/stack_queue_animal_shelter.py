from data_structures.queue import Queue
from data_structures.stack import Stack

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):
        new_animal = animal
        if self.front is None:
            self.front =new_animal

        if self.rear:
            self.rear.next = new_animal
        self.rear = new_animal

    def dequeue(self,pref):

        if pref is not 'cat' and pref is not 'dog':
            return None

        if pref is None:
            temp = self.front
            self.front = temp.next
            temp.next = None
            adopted_animal = temp
            return adopted_animal

        holding_pen = []
        adopted_animal = None
        while self.front.species != pref:
            temp= self.front
            self.front = temp.next
            temp.next = None
            holding_pen.append(temp)

        temp = self.front
        self.front =temp.next
        temp.next = None
        adopted_animal = temp

        num_held = len(holding_pen)
        while holding_pen:
            return_animal = holding_pen[num_held - 1]
            return_animal.next = self.front
            self.front = return_animal
            holding_pen.pop()

        return adopted_animal

class Dog:
    def __init__(self, species="dog", next=None):
        self.species = species
        self.next = next



class Cat:
    def __init__(self, species="cat", next= None):
        self.species = species
        self.next = next
        def __str__(self):

