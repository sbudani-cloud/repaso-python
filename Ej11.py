usuarios_act = ["amarusin", "rami", "mati","mama", "papa"]
newgens = ["luli", "la carbita", "val", "persona1", "persona2", "AMArusin"]
for e in usuarios_act:
    for i in newgens:
        if e.lower() == i.lower():
            print(f"cambiate el usuario pq {i.lower()} ya esta en uso")