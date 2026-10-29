#!/usr/bin/env python3

def find_the_redheads(family_dict):
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))