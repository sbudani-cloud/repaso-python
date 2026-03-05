personas = ["Mati", "Rami", "Amarusin"]
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")
    
print(f"{personas[2]} no pudo venir")
personas[2] = "Amarusin bebe"
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")
    
print("La mesa es más grande y ahora puede venir mas gente")
personas.insert(0, "Mama")
lol = len(personas) // 2
personas.insert(lol, "Papa")
personas.append("Un bebe")
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")