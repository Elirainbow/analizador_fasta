# 1. parsear_argumentos
# entrada: argumentos de la línea de comandos
# Responsabilidad: leer los argumentos dados por el usuario
# Salida: un objeto args con los argumentos

import argparse
from email import parser


def parsear_argumentos():

    parser = argparse.ArgumentParser(
        description="Analizador de secuencias FASTA en base a filtros dados por usuario"
    )
    parser.add_argument("-input", help="Ruta al archivo FASTA a analizar")
    parser.add_argument(
        "--min-gc",
        type=float,
        default=0.0,
        help="Porcentaje mínimo de GC para filtrar secuencias",
    )
    parser.add_argument(
        "--max-gc",
        type=float,
        default=100.0,
        help="Porcentaje máximo de GC para filtrar secuencias",
    )
    parser.add_argument(
        "--min-len",
        type=int,
        default=0,
        help="Longitud mínima de secuencia para filtrar",
    )
    parser.add_argument(
        "--max-len",
        type=int,
        default=float("inf"),
        help="Longitud máxima de secuencia para filtrar",
    )
    parser.add_argument(
        "-output",
        default="resultados.tsv",
        help="Ruta del archivo de salida en formato TSV",
    )

    args = parser.parse_args()
    return args


# 2. leer_fasta(ruta)
# Entrada: archivo fasta
# Responsabilidad: corroborar que existe, leer encabezados y secuencias
# Salida: lista de tuplas con los encabezados y secuencias


def leer_fasta(input):
    secuencias = []
    with open(input, "r") as file:
        encabezado = None
        secuencia = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if encabezado is not None:
                    secuencias.append((encabezado, secuencia))
                encabezado = line[1:]  # Eliminar el '>'
                secuencia = ""
            else:
                secuencia += line
        if encabezado is not None:
            secuencias.append((encabezado, secuencia))
    return secuencias
