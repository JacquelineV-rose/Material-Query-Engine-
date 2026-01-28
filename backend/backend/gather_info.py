import os
import json
from dotenv import load_dotenv
from mp_api.client import MPRester
from tqdm import tqdm

api_key = "aKMJVctL4R3e65yyTw9a7QshQS5DWVjL"
material_list = [
    "material_id",
    "formula_pretty",
    "energy_above_hull",
    "symmetry",
    "band_gap",
    "formation_energy_per_atom",
    "is_magnetic",
    "total_magnetization"
   # "experimentally_observed" unable to find the correct field
    
]




all_materials = []

with MPRester(api_key) as mpr:
    print("Loading")

    results = mpr.materials.summary.search(
        fields=material_list,
        all_fields=False,
        chunk_size=500,
        deprecated=False
    )



for m in tqdm(results, desc="Loading"):
    all_materials.append({

        "material_id": m.material_id,
        "pretty_formula": m.formula_pretty,
        "energy_above_hull": m.energy_above_hull,
        "space_group": m.symmetry.symbol if m.symmetry else "~",
        "band_gap": m.band_gap,
        "formation_energy_per_atom": m.formation_energy_per_atom,
        "magnetic_ordering": "Magnetic" if m.is_magnetic else "Non-magnetic",
        "total_magnetization": m.total_magnetization,
       # "experimentally_observed": getattr(m, "experimentally_observed", False)

})



with open("data/api_results.json", "w", encoding="utf-8") as f:
    json.dump(all_materials, f, indent=2, ensure_ascii=False)