A simple python script intended to convert existing resource packs to the new format for 1.21.4

## Usage

1. Download the `converter.py` script and run it.
2. The script will ask you for the path to your resource pack, please provide the path to the folder where your `pack.mcmeta` file lives, make sure to give an absolute path (usually starting with `C:/`)
3. The script will convert all json files living in `assets/minecraft/models/item` into the newer file format, and place them in `assets/minecraft/items`
4. The script will update your `pack.mcmeta` `pack_format` to 46

This script uses names to address items. The names used are the names of the models.

As such, a give command looks like this:

```
/give @p minecraft:<base_item>[minecraft:custom_model_data={strings:["<model_name>"]}]
```
