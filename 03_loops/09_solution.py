items = ["orange", "apple", "banana", "apple" , "coconut","banana"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("duplicate :", item)
        break
    unique_items.add(item)

