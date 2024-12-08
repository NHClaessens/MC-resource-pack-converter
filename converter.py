import json
import os
from pathlib import Path

path = ""

relative_output_dir = "/assets/minecraft/items/"

def convert_json(input_json):
    # Parse the input JSON
    parent = input_json.get("parent", "")
    textures = input_json.get("textures", {})
    overrides = input_json.get("overrides", [])
    
    # Extract fallback texture and model
    fallback_model = textures.get("layer0", "").split(":")[-1]
    
    # Build the cases array from overrides
    cases = []
    for override in overrides:
        predicate = override.get("predicate", {})
        custom_model_data = predicate.get("custom_model_data")
        model = override.get("model", "")
        name = model.split("/")[-1]
        
        if custom_model_data is not None and model:
            cases.append({
                "when": name,
                "model": {
                    "type": "model",
                    "model": f"{model}"
                }
            })
    
    # Create the output JSON
    output_json = {
        "model": {
            "type": "select",
            "property": "custom_model_data",
            "fallback": {
                "type": "model",
                "model": f"item/{fallback_model}"
            },
            "cases": cases
        }
    }
    
    return output_json

def get_json_files(dir_path):
    json_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(".json") and os.path.isfile(os.path.join(dir_path, f))]

    return json_files

def main():
    
    raw_path = input("Enter the path to the root folder of your resource pack (containing the .mcmeta file): ")
    if(Path(raw_path).exists() and Path(raw_path+"/assets").exists()):
        path = raw_path
    else:
        print("Path", raw_path, "does not exist or is not the root folder of your resource pack")
        return -1

    files = get_json_files(path + "/assets/minecraft/models/item")

    for f in files:
        file = Path(f)
        print("Converting", file.name)
        contents = file.read_text().replace("\\\\", "/")

        result = convert_json(json.loads(contents))

        dest_file = Path(path + relative_output_dir + file.name)

        dest_file.parent.mkdir(parents=True, exist_ok=True)

        dest_file.write_text(json.dumps(result, indent=1))

if __name__ == "__main__":
    main()
