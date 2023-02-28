from implementations import Built_in_Data_Strucutes
from linked_list import Node
from linked_list import LinkedLists

data_methods = Built_in_Data_Strucutes()
#print(find_month)

#data_methods.add_greens()
#data_methods.print_greens()

#data_methods.print_contact_info()

#data_methods.name_relationship_printer()

linked_list = LinkedLists()
linked_list.append_node(55)
linked_list.append_node(60)
linked_list.append_node(65)
linked_list.append_node(70)

find1 = linked_list.find_node(60)
find2 = linked_list.find_node(90)

print(find1)
print(find2)