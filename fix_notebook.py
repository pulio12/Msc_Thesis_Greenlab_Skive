
import json
import re

filename = r"c:\Users\Pulin\Desktop\Msc_Thesis_Greenlab_Skive\Test_file2.ipynb"

try:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Modify Cell 35 (add_TES_rondo)
    cell35 = data['cells'][35]
    source35 = cell35['source']
    new_source35 = []
    for line in source35:
        if 'bus1="Heat_Bus_Skive"' in line and 'TES_Rondo_to_Heat_Bus_Skive' in "".join(source35):
             # Ensure we are in the TES_Rondo_to_Heat_Bus_Skive link block
             # (Simple replacement might be safe enough given the context check)
             new_source35.append(line.replace('bus1="Heat_Bus_Skive"', 'bus1="Heat_Exchanger_Bus"'))
        else:
            new_source35.append(line)
    data['cells'][35]['source'] = new_source35

    # Modify Cell 45 (add_heat_exchanger)
    cell45 = data['cells'][45]
    source45 = "".join(cell45['source'])
    source45 = source45.replace('n.add("Bus", "Medium_Temp_Heat_Bus", carrier="heat",)', 'n.add("Bus", "Heat_Exchanger_Bus", carrier="heat",)')
    source45 = source45.replace('bus0="TES_Rondo"', 'bus0="Heat_Exchanger_Bus"')
    source45 = source45.replace('bus1="Medium_Temp_Heat_Bus"', 'bus1="Heat_Bus_Skive"')
    
    # Split back into lines ending with \n
    # simple splitlines keeps stripped lines, we want to preserve newlines?
    # Actually, let's just use re.sub or replace on the list if possible, but the list is cleaner.
    # But replacing line by line is safer for JSON format preservation.
    
    new_source45 = []
    for line in cell45['source']:
        l = line
        l = l.replace('n.add("Bus", "Medium_Temp_Heat_Bus", carrier="heat",)', 'n.add("Bus", "Heat_Exchanger_Bus", carrier="heat",)')
        l = l.replace('bus0="TES_Rondo"', 'bus0="Heat_Exchanger_Bus"')
        l = l.replace('bus1="Medium_Temp_Heat_Bus"', 'bus1="Heat_Bus_Skive"')
        new_source45.append(l)
    data['cells'][45]['source'] = new_source45

    # Modify Cell 52 (Execution)
    cell52 = data['cells'][52]
    source52 = cell52['source']
    new_source52 = []
    added = False
    for line in source52:
        if 'n.add("Bus", "TES_Rondo", carrier="heat")' in line and not added:
             new_source52.append('\n')
             new_source52.append('n.add("Bus", "Heat_Exchanger_Bus", carrier="heat")\n')
             new_source52.append('add_heat_exchanger()\n')
             new_source52.append('\n')
             added = True
        new_source52.append(line)
    data['cells'][52]['source'] = new_source52

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1) # indent=1 to match typical ipynb format (often 1 or 2)
    
    print("Notebook updated successfully.")

except Exception as e:
    print(f"Error: {e}")
