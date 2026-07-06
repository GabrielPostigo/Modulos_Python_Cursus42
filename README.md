# Módulos Python Cursus 42

Repositorio con ejercicios de Python organizados por módulos. La temática general gira en torno a jardines, plantas, cosechas y errores, y cada archivo practica un concepto concreto.

Nota: por ahora este README solo resume los módulos presentes en el repositorio. La carpeta PyMo03 se omite de forma expresa.

## Resumen de archivos

### Raíz

| Archivo | Resumen |
|---|---|
| `README.md` | Documento principal del proyecto con una visión general de los módulos y ejercicios. |

### `observaciones/`

| Archivo | Resumen |
|---|---|
| `observaciones/observaciones_00_06.md` | Nota explicativa sobre funciones con parámetros por defecto y recursión. |
| `observaciones/observaciones_01_03.md` | Explicación del decorador `@classmethod` y del parámetro `cls`. |
| `observaciones/observaciones_01_06.md` | Resumen sobre métodos estáticos y su uso con `@staticmethod`. |

### `PyMo_00/` - Fundamentos de Python

| Archivo | Resumen |
|---|---|
| `PyMo_00/main.py` | Programa auxiliar para probar los ejercicios del módulo 00 desde un menú interactivo. |
| `PyMo_00/ex0/ft_hello_garden.py` | Imprime un saludo sencillo al estilo del jardín. |
| `PyMo_00/ex1/ft_garden_name.py` | Pide el nombre del jardín y muestra un mensaje de estado. |
| `PyMo_00/ex2/ft_plot_area.py` | Calcula el área de una parcela a partir de largo y ancho. |
| `PyMo_00/ex3/ft_harvest_total.py` | Suma la cosecha de tres días y muestra el total. |
| `PyMo_00/ex4/ft_plant_age.py` | Comprueba si una planta tiene edad suficiente para cosecharse. |
| `PyMo_00/ex5/ft_water_reminder.py` | Indica si toca regar según los días transcurridos desde el último riego. |
| `PyMo_00/ex6/ft_count_harvest_iterative.py` | Cuenta los días hasta la cosecha usando un bucle `for`. |
| `PyMo_00/ex6/ft_count_harvest_recursive.py` | Cuenta los días hasta la cosecha usando recursión. |
| `PyMo_00/ex7/ft_seed_inventory.py` | Gestiona un inventario de semillas con `type hints` y diferentes unidades. |

### `PyMo_01/` - Programación orientada a objetos

| Archivo | Resumen |
|---|---|
| `PyMo_01/ex0/ft_garden_intro.py` | Presentación básica del jardín con variables y salida por pantalla. |
| `PyMo_01/ex1/ft_garden_data.py` | Define una clase `Plant` y crea varias plantas con sus datos. |
| `PyMo_01/ex2/ft_plant_grown.py` | Simula el crecimiento de una planta durante varios días con métodos de clase. |
| `PyMo_01/ex3/ft_plant_factory.py` | Introduce un método de clase para crear plantas con estilo fábrica. |
| `PyMo_01/ex4/ft_garden_security.py` | Añade validaciones para proteger atributos como altura y edad de la planta mediante setters. |
| `PyMo_01/ex5/ft_plant_types.py` | Define una jerarquía de clases con `Plant`, `Flower`, `Tree` y `Vegetable`, usando herencia y métodos específicos. |
| `PyMo_01/ex6/ft_garden_analytics.py` | Amplía la jerarquía con estadísticas de uso, clases anidadas y comportamientos distintos por tipo de planta. |

### `PyMo_02/` - Excepciones

Esta carpeta se centra en aprender a detectar, lanzar y manejar errores en Python. Cada archivo prueba un aspecto distinto del tratamiento de excepciones.

| Archivo | Resumen |
|---|---|
| `PyMo_02/ex0/ft_first_exception.py` | Muestra el primer uso de `try/except`. Intenta convertir texto a entero y captura el fallo cuando la entrada no es numérica. |
| `PyMo_02/ex1/ft_raise_exception.py` | Añade validación de rango para la temperatura. Lanza una excepción si el valor es demasiado bajo o demasiado alto para las plantas. |
| `PyMo_02/ex2/ft_different_errors.py` | Simula varios tipos de errores y enseña cómo reaccionar ante cada uno usando `try/except` y `match/case`. |
| `PyMo_02/ex3/ft_custom_errors.py` | Define errores personalizados relacionados con el jardín, como problemas de agua o plantas en mal estado. |

### Qué se aprende en `PyMo_02`

- Capturar errores sin romper el programa.
- Lanzar excepciones cuando los datos no son válidos.
- Diferenciar varios tipos de errores.
- Crear excepciones propias para casos concretos del proyecto.

## Ideas que se trabajan

- Entrada y salida por consola.
- Tipos de datos y operaciones básicas.
- Condicionales, bucles y recursión.
- Clases, objetos, herencia y métodos especiales.
- Captura y lanzamiento de excepciones.

## Estructura general

- `PyMo_00`: ejercicios de fundamentos.
- `PyMo_01`: ejercicios de POO.
- `PyMo_02`: ejercicios de manejo de errores.

