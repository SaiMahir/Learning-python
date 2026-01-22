names = ["Saima", "Ayesha", "Zainab", "Amna"]
a_names = [name for name in names if (lambda name: name.startswith("A"))(name)]
print(a_names)