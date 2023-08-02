import json
import random
from typing import List
import os
from models.Question import Question


def get_data() -> Question: 
    file_path: str = os.path.join(os.path.dirname(__file__), '../databases/data.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        data: List[Question] = json.load(file)
        number: int = random.randint(0, len(data) - 1)
        response: Question = data[number]
    return response
