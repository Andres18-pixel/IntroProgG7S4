hombres = int(input("Ingrese la cantidad de hombres que hay en el aula: "))
mujeres = int(input("Ingrese la cantidad de mujeres que hay en el aula: "))
suma = (hombres + mujeres)
porcentaje_h = hombres / suma * 100
porcentaje_m = mujeres / suma * 100
print(f"El porcentaje de hombres que hay en el aula es: {porcentaje_h}")
print(f"El porcentaje de mujeres que hay en el aula es: {porcentaje_m}")
