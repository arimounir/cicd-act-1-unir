# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución
>python3 main.py **\<filename\>** **\<dup\>** **\<order\>**  

filename: **ruta** al fichero que contiene la lista de palabras, una por línea.

dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista.

order: **asc|desc**, asc, valor por defecto para ordenar las palabras de forma ascendente, desc, para ordenar de forma descendente.

```python
# Ejecución en windows en este ejemplo, la lista de palabras del archivo "words.txt" se ordenará en orden descendente y los duplicados se eliminarán antes de la ordenación.

  python main.py words.txt yes desc
```

### Integrantes Equipo 2 - Grupo 5:

- Moguillansky Ariel
- Benitez Guayuan Marcos
- Alfredo Mendoza Fuentes