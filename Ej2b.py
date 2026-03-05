personas = ["Mati", "Rami", "Amarusin"]
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")

print(f"{personas[2]} no pudo venir")
personas[2] = "Amarusin bebe"
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")