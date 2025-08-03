def good_fruits(fruits: tuple[dict]) -> dict[str, int]:
    filter_dict = {}
    for item in fruits :
        if item["shape"] == "sphere" and ( 300 <= item["mass"] <= 600) and (100 <= item["volume"] <= 500) :
            filter_dict[item["name"]] = filter_dict.get(item["name"],0) + 1
    return filter_dict
print(good_fruits((
{'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
{'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
{'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
{'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})))
 