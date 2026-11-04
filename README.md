# Módulos Python Cursus 42

Repositorio con ejercicios de Python organizados por módulos. La temática general gira en torno a jardines, plantas, cosechas y errores, y cada archivo practica un concepto concreto.

Este README resume los módulos y ejercicios presentes actualmente en el repositorio.

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

### `PyMo_03/` - Herramientas y estructuras de datos

| Archivo | Resumen |
|---|---|
| `PyMo_03/ex0/ft_command_quest.py` | Procesa y muestra argumentos recibidos desde la línea de comandos. |
| `PyMo_03/ex1/ft_score_analytics.py` | Analiza puntuaciones y calcula totales, medias, máximos, mínimos y rangos. |
| `PyMo_03/ex2/ft_coordinate_system.py` | Trabaja con coordenadas y operaciones sobre puntos. |
| `PyMo_03/ex3/ft_achievement_tracker.py` | Registra logros y progreso mediante estructuras de datos. |
| `PyMo_03/ex4/ft_inventory_system.py` | Gestiona un inventario con diferentes tipos de objetos. |
| `PyMo_03/ex5/ft_data_stream.py` | Procesa datos recibidos como un flujo de información. |
| `PyMo_03/ex6/ft_data_alchemist.py` | Combina y transforma datos usando varias estructuras de Python. |

### `PyMo_04/` - Entrada, salida y archivos

| Archivo | Resumen |
|---|---|
| `PyMo_04/ex0/ft_ancient_text.py` | Lee y muestra archivos controlando errores de acceso. |
| `PyMo_04/ex1/ft_archive_creation.py` | Crea y escribe archivos de archivo. |
| `PyMo_04/ex2/ft_stream_management.py` | Gestiona flujos de entrada y salida. |
| `PyMo_04/ex3/ft_vault_security.py` | Trabaja con archivos protegidos y errores de permisos. |

### `PyMo_05/` - Clases abstractas y procesamiento de datos

| Archivo | Resumen |
|---|---|
| `PyMo_05/ex0/data_processor.py` | Define procesadores numéricos, de texto y de registros mediante una clase abstracta común. |
| `PyMo_05/ex1/data_stream.py` | Implementa el procesamiento de datos en forma de flujo. |
| `PyMo_05/ex2/data_pipeline.py` | Construye una canalización para encadenar procesadores de datos. |

### `PyMo_06/` - Módulos, paquetes y alquimia

| Archivo | Resumen |
|---|---|
| `PyMo_06/ft_alembic_0.py` – `ft_alembic_5.py` | Practica la importación de módulos, paquetes y subpaquetes. |
| `PyMo_06/ft_distillation_0.py` – `ft_distillation_1.py` | Usa funciones importadas desde módulos de alquimia. |
| `PyMo_06/ft_kaboom_0.py` – `ft_kaboom_1.py` | Explora errores relacionados con imports. |
| `PyMo_06/ft_transmutation_0.py` – `ft_transmutation_2.py` | Trabaja con paquetes, recetas y transmutaciones. |
| `PyMo_06/alchemy/elements.py` | Proporciona funciones para crear elementos alquímicos. |
| `PyMo_06/alchemy/potions.py` | Define pociones de curación y fuerza. |
| `PyMo_06/alchemy/grimoire/` | Contiene grimorios y validadores de hechizos claros y oscuros. |
| `PyMo_06/alchemy/transmutation/recipes.py` | Define recetas de transmutación. |

### `PyMo_07/` - Patrones de diseño

| Archivo | Resumen |
|---|---|
| `PyMo_07/ex0/creature.py` | Define criaturas mediante una jerarquía de clases abstractas. |
| `PyMo_07/ex0/factory.py` | Crea criaturas usando el patrón Factory. |
| `PyMo_07/ex1/capabilities.py` | Define capacidades que pueden tener las criaturas. |
| `PyMo_07/ex1/creatures.py` | Amplía los tipos de criaturas y sus comportamientos. |
| `PyMo_07/ex1/factories.py` | Centraliza la creación de criaturas y capacidades. |
| `PyMo_07/ex2/strategy.py` | Implementa estrategias intercambiables para los combates. |
| `PyMo_07/battle.py` | Ejecuta simulaciones de batalla. |
| `PyMo_07/tournament.py` | Organiza torneos entre criaturas. |
| `PyMo_07/capacitor.py` | Sirve de apoyo para la gestión de participantes y combates. |

### `PyMo_08/` - Entornos virtuales, dependencias y validación

| Archivo | Resumen |
|---|---|
| `PyMo_08/ex0/construct.py` | Detecta y describe el entorno virtual de Python activo. |
| `PyMo_08/ex1/loading.py` | Carga y trabaja con dependencias externas. |
| `PyMo_08/ex1/pyproject.toml` | Configura el proyecto y sus dependencias. |
| `PyMo_08/ex1/requirements.txt` | Lista dependencias del ejercicio. |
| `PyMo_08/ex2/oracle.py` | Valida datos de entrada con modelos de Pydantic. |
| `PyMo_08/ex2/.env.example` | Ejemplo de configuración mediante variables de entorno. |

### `PyMo_09/` - Modelado y validación de datos

| Archivo | Resumen |
|---|---|
| `PyMo_09/ex0/space_station.py` | Modela una estación espacial con campos y restricciones de Pydantic. |
| `PyMo_09/ex1/alien_contact.py` | Modela y valida información de contacto alienígena. |
| `PyMo_09/ex2/space_crew.py` | Modela y valida los datos de una tripulación espacial. |

## Ideas que se trabajan

- Entrada y salida por consola.
- Tipos de datos y operaciones básicas.
- Condicionales, bucles y recursión.
- Clases, objetos, herencia y métodos especiales.
- Captura y lanzamiento de excepciones.
- Argumentos de línea de comandos y entrada/salida de archivos.
- Clases abstractas, módulos, paquetes y patrones de diseño.
- Entornos virtuales, dependencias y validación de datos con Pydantic.

## Estructura general

- `PyMo_00`: ejercicios de fundamentos.
- `PyMo_01`: ejercicios de POO.
- `PyMo_02`: ejercicios de manejo de errores.
- `PyMo_03`: herramientas y estructuras de datos.
- `PyMo_04`: entrada, salida y archivos.
- `PyMo_05`: clases abstractas y procesamiento de datos.
- `PyMo_06`: módulos y paquetes.
- `PyMo_07`: patrones de diseño.
- `PyMo_08`: entornos virtuales y dependencias.
- `PyMo_09`: modelado y validación de datos.
