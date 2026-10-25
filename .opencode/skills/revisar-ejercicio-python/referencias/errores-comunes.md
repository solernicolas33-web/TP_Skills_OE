# Errores comunes en Python de primer año

Este documento lista los errores conceptuales y sintácticos más frecuentes en alumnos de primer año de Programación I, junto con pistas para orientarlos sin darles la solución.

---

## 1. No convertir lo que devuelve input()
`input()` siempre devuelve un dato de tipo texto (`str`). Si se intenta operar matemáticamente o comparar con números sin convertirlo previa o directamente con `int()` o `float()`, el programa lanzará un `TypeError` o se comportará de manera inesperada.
- **Pista para el alumno:** "¿De qué tipo es el dato que devuelve `input()`? Recordá qué función se usa para transformar un texto en un número entero o decimal."

---

## 2. Divisibilidad y precedencia de operadores
Al calcular promedios o fórmulas matemáticas complejas, es común olvidar los paréntesis necesarios para alterar el orden predeterminado de los operadores matemáticos (por ejemplo, escribir `a + b + c / 3` en lugar de `(a + b + c) / 3`).
- **Pista para el alumno:** "Revisá el orden en que Python resuelve las operaciones matemáticas. ¿Qué se calcula primero, la suma o la división?"

---

## 3. Imprimir (print) en lugar de retornar (return) dentro de una función
Confundir el objetivo de mostrar algo por pantalla con devolver un valor utilizable por el programa principal. Si una función hace un `print()` y no incluye un `return`, devolverá implícitamente `None`.
- **Pista para el alumno:** "Fijate si la función está devolviendo el resultado con `return` para que el resto del programa pueda guardarlo en una variable, o si solo lo está mostrando por consola."

---

## 4. Comparaciones redundantes con booleanos
Escribir condiciones del estilo `if expresion == True:` o `if bandera == False:`.
- **Pista para el alumno:** "En las estructuras condicionales no hace falta comparar explícitamente contra `True` o `False`, ya que la condición evalúa por sí misma el valor booleano."

---

## 5. Comparaciones encadenadas involuntarias
Escribir condiciones como `if p >= 6 == True:`. Python evalúa esto como `(p >= 6) and (6 == True)`, lo cual falla lógicamente ya que `6 == True` es siempre falso.
- **Pista para el alumno:** "Ojo con encadenar comparaciones con `== True`. Simplificá la condición usando únicamente la comparación lógica directa (por ejemplo, `p >= 6`)."

---

## 6. Variables no inicializadas o fuera de alcance (Scope)
Utilizar una variable dentro de una función asumiendo que existe porque fue creada en el bloque principal, o intentar usar una variable dentro de un bucle sin haberle asignado un valor previo (por ejemplo, acumuladores o contadores).
- **Pista para el alumno:** "¿La variable tiene un valor inicial asignado antes de usarse? Comprobá si la variable fue declarada dentro del bloque o función donde la querés usar."

---

## 7. Bucle infinito o rangos incorrectos
En bucles `while`, olvidar actualizar la variable de control dentro del cuerpo del bucle. En bucles `for`, configurar mal los argumentos de `range(inicio, fin, paso)`, recordando que el límite superior no se incluye.
- **Pista para el alumno:** "Revisá el criterio de parada de tu bucle: ¿hay algún valor que cambie dentro para que la condición deje de cumplirse en algún momento?"

---

## 8. Modificar la lista mientras se la recorre
Intentar eliminar o agregar elementos a una lista utilizando un bucle `for` que itera sobre esa misma lista, lo que altera los índices y produce comportamientos inconsistentes o salta elementos.
- **Pista para el alumno:** "Modificar una lista mientras se la recorre altera sus posiciones. Considerá iterar sobre una copia de la lista o crear una lista nueva con los resultados."