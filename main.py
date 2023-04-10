"""
License: Apache
Organization: UNIR
"""

import os
import sys
import re
from unicodedata import normalize

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = "asc"


def sort_list(items, order=DEFAULT_ORDER):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(order == "desc"))


def eliminar_diacriticos(cadena):
    # NFD y eliminar diacriticos
    cadena = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize("NFD", cadena), 0, re.I
    )

    # -> NFC
    cadena = normalize('NFC', cadena)

    return cadena


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    order = DEFAULT_ORDER

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento indica el orden (asc o desc)")
        sys.exit(1)

    if len(sys.argv) >= 3:
        remove_duplicates = sys.argv[2].lower() == "yes"

    if len(sys.argv) >= 4:
        order = sys.argv[3].lower()

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)

    if os.path.isfile(file_path):
        word_list = []

        with open(file_path, "r") as file:
            for line in file:
                word_list.append(eliminar_diacriticos(line.strip()))
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, order))