import jsonpointer
import json
import csv

PLACES_TO_PUT_CODE_ITEMS = [
    "/properties/answer/anyOf"
]

FILENAMES = {
    "codes.csv": "schema-compiled.json",
    "codes-reduced.csv": "schema-compiled-reduced.json",
}

def compile(codes_filename_in, schema_filename_out):
    # Load JSON Schema
    with open("schema.json") as fp:
        schema = json.load(fp)

    # Load Codes
    codes_with_key = {}
    with open(codes_filename_in, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if not row[0] in codes_with_key:
                codes_with_key[row[0]] = [ row[0] ]
            if row[1]:
                codes_with_key[row[0]].append(row[1])
    codes = list(codes_with_key.values())
    codes_max_length = [len(i) for i in codes]
    #print(codes)
    #print(codes_max_length)

    # Calculate all possible allowed combinations of codes
    number_combinations = _get_all_possible_number_combinations(codes_max_length)
    #print(number_combinations)

    # Generate new schema to add
    new_schema = []
    for number_combination in number_combinations:
        new_schema.append({
            "type": "array",
            "minLength": 1,
            "additionalItems": False,
            "items": {
                "anyOf": [{"const": x} for x in _get_codes_for_number_combination(codes, number_combination)]
            }
        })
    #print(new_schema)

    # Add new schema in right places
    for place in PLACES_TO_PUT_CODE_ITEMS:
        jsonpointer.set_pointer(schema, place, new_schema)

    # Finally write back
    with open(schema_filename_out, "w") as fp:
        json.dump(schema, fp, indent=2)



def _get_all_possible_number_combinations(max_lengths_of_data):
    out = []

    lengths_of_data_to_add = max_lengths_of_data.copy()

    # First value; set up out easily
    length_to_add = lengths_of_data_to_add.pop(0)
    for i in  range(0, length_to_add):
        out.append([i])

    # Further values must be added to all current values!
    while lengths_of_data_to_add:
        length_to_add = lengths_of_data_to_add.pop(0)
        new_out = []
        for i in  range(0, length_to_add):
            for o in out:
                new_value = o.copy()
                new_value.append(i)
                new_out.append(new_value)
        out = new_out

    return out


def _get_codes_for_number_combination(codes, number_combination):
    out = []
    for i in range(0, len(codes)):
        out.append(codes[i][number_combination[i]])
    return out


for codes_filename_in,schema_filename_out in FILENAMES.items():
    compile(codes_filename_in, schema_filename_out)
