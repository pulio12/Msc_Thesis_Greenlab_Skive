
import json

filename = r"c:\Users\Pulin\Desktop\Msc_Thesis_Greenlab_Skive\Test_file2.ipynb"
search_term = "TES_Rondo_to_Heat_Bus_Skive"

try:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)



    for cell_idx, cell in enumerate(data['cells']):

        if cell_idx in [35, 52]:
            print(f"--- Cell {cell_idx} ---")
            for line in cell['source']:
                print(repr(line))

except Exception as e:
    print(f"Error: {e}")
