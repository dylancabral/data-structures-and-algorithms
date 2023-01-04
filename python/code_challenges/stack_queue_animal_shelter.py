# from data_structures.queue import Queue


class AnimalShelter:
    # initializes empty node
    def __init__(self):
        self.front = None
        self.rear = None

    # enqueues new animal into the animal shelters queue
    def enqueue(self, animal):
        new_animal = animal
        if self.front is None:
            self.front = new_animal

        if self.rear:
            self.rear.next = new_animal
        self.rear = new_animal

    def dequeue(self, pref):

        if pref is not 'cat' and pref is not 'dog':
            return None

        # If they have no preference, return the first animal
        if pref is None:
            temp = self.front
            self.front = temp.next
            temp.next = None
            adopted_animal = temp
            return adopted_animal

        # While the animal is not the species of preference move to the holding pen
        holding_pen = []
        adopted_animal = None
        while self.front.animal != pref:
            temp = self.front
            self.front = temp.next
            temp.next = None
            holding_pen.append(temp)

        # Hold animal that going to be adopted and return to person
        temp = self.front
        self.front = temp.next
        temp.next = None
        adopted_animal = temp

        # Move holding pen animals back into the queue in reverse to return queue
        num_held = len(holding_pen)
        while holding_pen:
            return_animal = holding_pen[num_held - 1]
            return_animal.next = self.front
            self.front = return_animal
            holding_pen.pop()

        # Return the chosen species animal to the adoptee
        return adopted_animal


class Dog:
    def __init__(self, animal="dog", next=None):
        self.species = animal
        self.next = next

    def __str__(self):
        return self.species


class Cat:
    def __init__(self, animal="cat", next=None):
        self.species = animal
        self.next = next

    def __str__(self):
        return self.animal

