personas = ["Mati", "Rami", "Amarusin"]
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")
    
print(f"{personas[2]} no pudo venir")
personas[2] = "Amarusin bebe"
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")
    
print("La mesa es más grande y ahora puede venir más gente")
personas.insert(0, "Mama")
lol = len(personas) // 2
personas.insert(lol, "Papa")
personas.append("Un bebe")
for e in personas: 
    print(f"Hola {e} veni a cenar jaja")

print("Solo pueden venir 2 personas porque la mesa no alcanza, asi que solo vienen los 2 bebes.")
no_vienen = ["Mati", "Rami", "Mama", "Papa"]
for e in no_vienen:
    personas.remove(e)
    print(f"Hola perdon {e} no vas a poder venir pq no sos un bebe.")
for e in personas:
    print(f"Hola {e} vos si venis pq sos un bebe.")