class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            if new_floor > self.numbers_of_floors:
                print("Такого этажа не существует")
                break
            print(int(i))







h_1 = House('ЖК Горьский', 18)
h_2 = House('Домик в деревне', 2)
h_1.go_to(5)
h_2.go_to(10)
