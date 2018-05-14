from collections import OrderedDict

keywords = OrderedDict()

keywords["for"] = "Used to iterate through a collection of objects or a range of values."
keywords["if"] = "Keyword used to make boolean evaluations."
keywords["else"] = "Default option for an if statement."
keywords["elif"] ="Statement used to evaluate a logic statement after an opening if statement."
keywords["and"] = "Clause used to join two logic statement that are being evaluated."
keywords["items"] = "Method used to get all pbject in a collection."
keywords["keys"] = "Used to get list of key values in a dictionary."
keywords["in"] = "Used with for statement to get individual values in a collection of objects."
keywords["print"] = "System method used to print to standard IO"
keywords["not"] = "Used to negate various logic statements."


for key, value in keywords.items():
    print(key + ": " + value)

#for key, value in my_dictionary.items():
#    print(key + ": " + value)