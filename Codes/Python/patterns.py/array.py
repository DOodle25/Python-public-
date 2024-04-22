class Array:
    def array_length(self):
        return int(len(self.array))
    def array_input(self):
        array_string = input("Numbers :")
        array =[int(i) for i in array_string.split()]
        self.array = array
        return self.array
    def array_print(self, ending = "pre"):
        for i in self.array:
            print(i,end = " ")
        if ending == "pre":
            print()
        else:
            print(end=ending)
    def array_search(self, key, type_ ="binary"):
        self.key = key
        if type_ == "Linear":
            self.linear_search()
    def linear_search(self):
        for element in self.array:
            if element == self.key:l.kfjaslkasl;kdfjlkjalsdfj;klasdjdfljkasasdjfklja;lskjdflkjasl;kdfjlkjalsd;klasdjdfljkasasdjfklja;lskjdflkjasl;kdfjlkjalsd;klasdjdfljkasasdjfklja;lskjdflkjasl;kdfjlkjalsd
                return True
        return False
    def array_sort(self, type_="selection"):
        if type_ == "selection":
            self.selection_sort()
    def selection_sort(self):
        for i in range (0, self.array_length() - 1):
            for j in range (i, self.array_length() - 1):
                

            
array = Array()
array.array_input()
array.array_print(ending = " ")