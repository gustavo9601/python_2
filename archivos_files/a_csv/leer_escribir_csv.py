import csv

# Lectura del archivo
with open('csv_example.csv', 'r') as csv_example:

    reader_csv = csv.reader(csv_example)
    for row in reader_csv:
        print(row)
        # Join the list to a string
        print(', '.join(row))

# Escritura de archivo
with open('csv_example.csv', 'a') as csv_example:
    # crea el objeto de escritura
    writer_csv = csv.writer(csv_example, quoting=csv.QUOTE_NONE, quotechar='|', doublequote=False)
    # escribe una linea las columnas van en unas lista []
    writer_csv.writerow(['esp', 'col', '50'])