#data type string
#when given input String() -----> return object ['','','','']
class ArrayString():
    #either takes input from user and makes it to list type of takes input in argument
    '''self.data_(list) | self.len_(int)'''
    def __init__(self, *strin_):
        if strin_:
            if (len(strin_) < 2 and type(strin_[0]) == type(list())):
                self.len_ = len(strin_[0])
                self.data_ = strin_[0]
            elif (len(strin_) < 2 and type(strin_[0]) == type(str())):
                self.len_ = len(strin_[0])
                self.data_ = list(strin_[0])
            else:
                print("more then 1 arguments provided")
                return None
        else:
            temp = input()
            self.len_ = len(temp)
            self.data_ = [0] * self.len_
            temp_ = 0
            while not temp_ == self.len_:
                self.data_[temp_] = temp[temp_]
                temp_ += 1
    #concatenation of two same type [Arraystring] + [Arraystring]
    def __add__(obj1_,obj2_):
        temp1_ = obj1_.len_
        temp2_ = temp1_ + obj2_.len_
        obj3_ = [0] * temp2_
        loop_ = 0
        while not loop_ == temp1_:
            obj3_[loop_] = obj1_.data_[loop_]
            loop_ += 1
        loop2_ = 0
        while not loop_ == temp2_:
            obj3_[loop_] = obj2_.data_[loop2_]
            loop_ += 1
            loop2_ += 1
        return ArrayString(obj3_)
    #returns string type and also sets self.str_ as string type of given array
    '''self.str_(str)'''
    def string_(self):
        temp_ = 0
        self.str_ = str()
        while not temp_ == self.len_:
            self.str_ = self.str_ + self.data_[temp_]
            temp_ += 1
        return self.str_
    #def methods_():(for slicing and stuff)
    #count_ : calculates how many times specific element occurs
    def count_(self,element_):
        element_count = 0
        for i in self.data_:
            if i == element_:
                element_count += 1
        return element_count
    #find_ : finds if substring exists in a string
    def find_(self,key_):
        key_ = ArrayString(key_)
        loop1_ = 0
        for i in range(0, self.len_ - key_.len_):
            if self.data_[i] == key_.data_[0]:
                loop2_ = i
                key_check_ = True
                for j in key_.data_:
                    if not j == self.data_[loop2_]:
                        key_check_ = False
                    loop2_ += 1
                if key_check_ == True:
                    return True
        return False
    #index_ : returns first location of found element
    def index_(self,element_):
        index_list = list()
        temp_ = self.len_
        loop_ = 0
        while not loop_ == temp_:
            if self.data_[loop_] == element_:
                return loop_
            loop_ += 1
        return None
    #index_all_ : returns all location of found element
    def index_all_(self,element_):
        index_list = list()
        temp_ = self.len_
        loop_ = 0
        while not loop_ == temp_:
            if self.data_[loop_] == element_:
                index_list.append(loop_)
            loop_ += 1
        return index_list
    #starts_with_ : returns if the given string starts with specifics or not
    def starts_with_(self,start_data_):
        start_data_ = ArrayString(start_data_)
        if start_data_.len_ > self.len_:
            return False
        else:
            len_ = start_data_.len_
            loop_ = 0
            while not loop_ == len_:
                if not start_data_.data_[loop_] == self.data_[loop_]:
                    return False
                loop_ += 1
            return True
    #ends_with_ : returns if the given string ends with specifics or not
    def ends_with_(self,end_data_):
        end_data_ = ArrayString(end_data_)
        if end_data_.len_ > self.len_:
            return False
        else:
            loop1_ = self.len_
            loop2_ = end_data_.len_
            len_ = loop1_ - loop2_
            while not loop1_ == len_:
                if not end_data_.data_[loop2_ - 1] == self.data_[loop1_ - 1]:
                    return False
                loop1_ -= 1
                loop2_ -= 1
            return True
    #isdigit_ : retruns true if all elements are only digit
    def isdigit_(self):
        for i in self.data_:
            if not(ord(i) >= 48 and ord(i) <= 57):
                return False
        return True
    #isalpha_ : returns true if all elements are alphabets
    def isalpha_(self):
        for i in self.data_:
            if not((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):
                return False
        return True
    #isalnum_ : returns true if all elements are alphabets and numbers
    def isalnum_(self):
        for i in self.data_:
            if not((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 48 and ord(i) <= 57)):
                return False
        return True
    #isidentifier_ : returns true the it follows all rules of identifiers
    def isidentifier_(self):
        if not (ord(self.data_[0]) == 95 or ((ord(self.data_[0]) >= 97 and ord(self.data_[0]) <= 122) or (ord(self.data_[0]) >= 65 and ord(self.data_[0]) <= 90))):
            return False
        for i in range(1, self.len_ - 1):
            if not((ord(self.data_[i]) >= 97 and ord(self.data_[i]) <= 122) or (ord(self.data_[i]) >= 65 and ord(self.data_[i]) <= 90) or (ord(self.data_[i]) >= 48 and ord(self.data_[i]) <= 57)):
                return False
        """reserved words and special identifiers check"""
        #print(self.string_())
        if self.string_() in globals():
                return False
        return True
    #upper_ : capializes the string
    def upper_(self):
        loop_ = 0
        for i in self.data_:
            if (ord(i) >= 97 and ord(i) <= 122):
                self.data_[loop_] = chr(ord(i) - 32)
            loop_ += 1
        return self.data_ 
    #lower_ : decapializes the string
    def lower_(self):
        loop_ = 0
        for i in self.data_:
            if (ord(i) >= 65 and ord(i) <= 90):
                self.data_[loop_] = chr(ord(i) + 32)
            loop_ += 1
        return self.data_
    #title_ : first word in every word capitalize
    def title_(self):
        loop_ = 0
        if ord(self.data_[0]) >= 97 and ord(self.data_[0]) <= 122:
                    self.data_[0] = chr(ord(self.data_[0]) - 32)
        for i in self.data_:
            if not loop_ == self.len_ - 1:
                if ord(self.data_[loop_ + 1]) >= 97 and ord(self.data_[loop_ + 1]) <= 122 and i == " ":
                    self.data_[loop_ + 1] = chr(ord(self.data_[loop_ + 1]) - 32)
            loop_ += 1
        return self.data_
    #is_upper_ : checks if string is capital
    def is_upper_(self):
        loop_ = 0
        for i in self.data_:
            if (ord(i) >= 97 and ord(i) <= 122):
                return False
            loop_ += 1
        return True
    #is_lower_ : checks if string is small
    def is_lower_(self):
        loop_ = 0
        for i in self.data_:
            if (ord(i) >= 65 and ord(i) <= 90):
                return False
            loop_ += 1
        return True
    #is_title_ : checks if first word in every word is capital
    def is_title_(self):
        loop_ = 0
        if ord(self.data_[0]) >= 97 and ord(self.data_[0]) <= 122:
                    return False
        for i in self.data_:
            if not loop_ == self.len_ - 1:
                if ord(self.data_[loop_ + 1]) >= 97 and ord(self.data_[loop_ + 1]) <= 122 and i == " ":
                    return False
            loop_ += 1
        return True
    #capitalize_ : first word in whole para capital all other small
    def capitalize_(self):
        loop_ = 0
        if ord(self.data_[0]) >= 97 and ord(self.data_[0]) <= 122:
                    self.data_[0] = chr(ord(self.data_[0]) - 32)
        for i in self.data_:
            if not loop_ == self.len_ - 1:
                if ord(self.data_[loop_ + 1]) >= 65 and ord(self.data_[loop_ + 1]) <= 90:
                    self.data_[loop_ + 1] = chr(ord(self.data_[loop_ + 1]) + 32)
            loop_ += 1
        return self.data_
    








obj1_ = ArrayString("2,3")
obj2_ = ArrayString("Hello")
obj3_ = ArrayString("Hi ")
y = obj1_ + obj2_ + obj3_
y = ArrayString("Hello ")
#print(y.is_title_())
#print(" a23  3hEllo".capitalize())
#x = ArrayString("ArrayString")
#print(x.isidentifier_())