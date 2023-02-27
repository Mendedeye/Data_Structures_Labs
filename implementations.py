class Built_in_Data_Strucutes:

    def __init__(self):
        pass

# TASK 1: Dictionary, Tuple, and Set

    # A tuple of all 12 months
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

    # Determines what month it is based on an integer in the range of 1-12
    def determine_month(self, find_month):

        if int(find_month) < 12:
            for month in range(len(self.months)):
                if int(find_month) == month:
                    return self.months[month - 1]
        else: 
            find_month = input("Please enter in a number between 1-12: ")

    # A set of fruits and vegetables
    set_of_greens = set()

    # Has the user add two fruits and two vegetables to a set
    def add_greens(self):

        print("")
        for iteration in range(2):
            new_green = input("Please put in a fruit to be added: ")
            self.set_of_greens.add(new_green)
        
        print("")
        for iteration in range(2):
            new_green = input("Please put in a vegetable to be added: ")
            self.set_of_greens.add(new_green)

    # Prints the greens from a set
    def print_greens(self):
        print("")
        for green in self.set_of_greens:
            print(green)
        
    # A dictionary containing first and last name, email address and phone number
    contact_dictionary = {
        "first_name": "Ethan",
        "last_name" : "Doering",
        "email"     : "ethanwdoering@icloud.com",
        "phone"     : 5052152554
    }

    # Prints out a contacts first and last name, email address and phone number
    def print_contact_info(self):
        print("\nHello my name is %s %s"                       % (self.contact_dictionary.get("first_name"), self.contact_dictionary.get("last_name")))
        print("And my email is %s and my phone number is (%d)" % (self.contact_dictionary.get("email"), self.contact_dictionary.get("phone")))

# TASK 2: List of Dictionaries

    # A list of dictionaries that contain family names and relationships
    family_list = [
        {
            "first_name"   : "Sophie",
            "last_name"    : "Doering",
            "relationship" : "Sister"
        },
        {
            "first_name"   : "Micah",
            "last_name"    : "Doering",
            "relationship" : "Dad"
        },
        {
            "first_name"   : "Abby",
            "last_name"    : "Chiardia",
            "relationship" : "Fiancéé"
        }
    ]

    # Prints the first name and relationship from family_list
    def name_relationship_printer(self):
        index = 0
        for member in self.family_list:
            print("\n%s is in my family and they are my %s." % (self.family_list[index["first_name"]], self.family_list[index["relationship"]]))
            index += 1