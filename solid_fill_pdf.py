#!/usr/bin/env python3
import os
import sys
import csv
from fdfgen import forge_fdf


def fin_translation(fin_value):
    if fin_value == '1':
        return ('single', 'X')
    elif fin_value == '2':
        return ('twin', 'X')
    elif fin_value == '3':
        return ('thruster', 'X')
    elif fin_value == '4':
        return ('quad', 'X')
    elif fin_value == '5':
        return ('fivefin', 'X')
    else:
        return ('otherfin', 'X')


def tail_translation(tail_value):
    if tail_value == 'square':
        return ('square', 'X')
    elif tail_value == 'squash':
        return ('squash', 'X')
    elif tail_value == 'round':
        return ('round', 'X')
    elif tail_value == 'round pin':
        return ('round pin', 'X')
    elif tail_value == 'pin':
       return ('pin', 'X')
    elif tail_value == 'swallow':
        return ('swallow', 'X')
    elif tail_value == 'fish':
        return ('fish', 'X')
    else:
        return ('tail', tail_value)


def type_translation(type_value):
    if type_value == 'future':
        return ('future', 'X')
    elif type_value == 'fcs2':
        return ('fcstwo', 'X')
    elif type_value == 'fcsii':
        return ('fcstwo', 'X')
    elif type_value == 'glasson':
        return ('glasson', 'X')
    else:
        return ('othertype', 'X')


def generate_key_value_tuples(header, row):
    key_value_tuples = []
    for i in range(len(header)):
        value = row[i].strip()
        if header[i] == 'fins':
            fin_tuple = fin_translation(value)
            if fin_tuple[0] == 'otherfin':
                key_value_tuples.append(fin_tuple)
                key_value_tuples.append((header[i], value))
            else:
                key_value_tuples.append(fin_tuple)
        elif header[i] == 'tail':
            tail_tuple = tail_translation(value.lower())
            key_value_tuples.append(tail_tuple)
        elif header[i] == 'type':
            type_tuple = type_translation(value.lower())
            key_value_tuples.append(type_tuple)
        elif header[i] == 'or':
            if value:
                key_value_tuples.append(('or', 'X'))
                key_value_tuples.append(('ortext', value))
        else:
            key_value_tuples.append((header[i], value))
    return key_value_tuples


def process_csv(csv_data):
    header = []
    output_data = []
    for row_number, row in enumerate(csv_data):
        if row_number == 0:
            continue
        if row_number == 1:
            header = row
            header = [word.lower().strip() for word in header]
            continue
        key_value_tuples = generate_key_value_tuples(header, row)
        output_data.append(key_value_tuples)
    return output_data


def fill_pdf_template(row, pdf_template, output_file):
    tmp_file = "tmp.fdf"
    fdf = forge_fdf("", row, [], [], [])
    with open(tmp_file, "wb") as fdf_file:
        fdf_file.write(fdf)
    cmd = "pdftk '{0}' fill_form '{1}' output '{2}' dont_ask".format(pdf_template, tmp_file, output_file)
    os.system(cmd)
    os.remove(tmp_file)


if __name__ == "__main__":
    """
    Batch fill pdf template with data from csv file
    """
    try:
        pdf_template = sys.argv[1]
        csv_file = sys.argv[2]
    except IndexError:
        print("python3 solid_fill_pdf.py pdf_template csv_file ")
    else:
        with open(csv_file) as f:
            csv_data = csv.reader(f)

            data = process_csv(csv_data)
            output_dir = os.path.join(os.getcwd(), 'output')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            for row in data:
                orderid = row[3][1]
                output_path = os.path.join(output_dir, orderid)
                output_file = output_path + ".pdf"
                fill_pdf_template(row, pdf_template, output_file)
                print("Generated {0}.pdf".format(orderid))
