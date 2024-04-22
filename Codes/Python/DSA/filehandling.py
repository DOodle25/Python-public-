def remove_symbols(input_string, symbols_to_remove):
    translation_table = str.maketrans("", "", symbols_to_remove)
    return input_string.translate(translation_table)

file = open("C:\\Users\\OMEN\\OneDrive\\Desktop\\PythonCodes\\DSA\\hello.txt", "r")
content = file.read()
#print(content)
#print(type(content))
sep_content = content.split('\n')
#print(sep_content)
sep_final = [0] * int(len(sep_content))
for id in sep_content:
    sep_final[int(sep_content.index(id))] = [a for a in id.split(',')]
#print(sep_final)
#sep_end = [0] * int(len(sep_final))
#for id in sep_final:
    #sep_end[int(sep_final.index(id))] = [a for a in id.split(':')]
#print(sep_end)
#name = input("input the name : ")
str_end = [0] * int(len(sep_final))
for i in sep_final:
    str_name = str(i)
    sy = "["
    str_name = remove_symbols(str_name,sy)
    sy = "]"
    str_name = remove_symbols(str_name,sy)
    sy = '"'
    str_name = remove_symbols(str_name,sy)
    sy = ":"
    str_name = remove_symbols(str_name,sy)
    sy = "'"
    str_name = remove_symbols(str_name,sy)
    str_end[int(sep_final.index(i))] = str_name.split(",")
file.close()
#print(str_end)
type_search = str(input("Enter the element you want to search(name/surname/class/language) : "))
match type_search:
    case "name":
        j = int(1)
        name = input("Enter the name : ")
        for i in str_end:
            if i[0] == f"name{name}":
                print(f"user number {j}")
                j = j + 1
                str_name = str(i[0])
                print("name :" ,str_name[4:])
                str_name = str(i[1])
                print("surname :" ,str_name[8:])
                str_name = str(i[2])
                print("class :" ,str_name[6:])
                str_name = str(i[3])
                print("language :" ,str_name[9:])
    case "surname":
        j = int(1)
        surname = input("Enter the surname : ")
        for i in str_end:
            if i[1] == f" surname{surname}":
                print(f"user number {j}")
                j = j + 1
                str_name = str(i[0])
                print("name :" ,str_name[4:])
                str_name = str(i[1])
                print("surname :" ,str_name[8:])
                str_name = str(i[2])
                print("class :" ,str_name[6:])
                str_name = str(i[3])
                print("language :" ,str_name[9:])
    case "class":
        j = int(1)
        class_t = input("Enter the class : ")
        for i in str_end:
            if i[2] == f" class{class_t}":
                print(f"user number {j}")
                j = j + 1
                str_name = str(i[0])
                print("name :" ,str_name[4:])
                str_name = str(i[1])
                print("surname :" ,str_name[8:])
                str_name = str(i[2])
                print("class :" ,str_name[6:])
                str_name = str(i[3])
                print("language :" ,str_name[9:])
    case "language":
        j = int(1)
        language = input("Enter the name : ")
        for i in str_end:
            if i[3] == f" language{language}":
                print(f"user number {j}")
                j = j + 1
                str_name = str(i[0])
                print("name :" ,str_name[4:])
                str_name = str(i[1])
                print("surname :" ,str_name[8:])
                str_name = str(i[2])
                print("class :" ,str_name[6:])
                str_name = str(i[3])
                print("language :" ,str_name[9:])