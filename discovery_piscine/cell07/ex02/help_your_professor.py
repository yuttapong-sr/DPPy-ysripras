#!/usr/bin/env python3

def average(scores_dict):
    if not scores_dict:
        return 0.0
    
    total_score = sum(scores_dict.values())
    
    num_students = len(scores_dict)
    
    return total_score / num_students

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")