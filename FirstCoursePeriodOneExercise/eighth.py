valid_words = {}
dictionary_answers = {}
dictionary_scores = {}

def ready_up() -> None:
    global valid_words
    with open("esm_famil_data.csv", "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
        headers = lines[0].strip().split(",")
        valid_words = {field: set() for field in headers}
        
        for line in lines[1:]:
            values = line.strip().split(",")
            for i in range(len(values)):
                word = values[i].replace(" ", "")
                if word:
                    valid_words[headers[i]].add(word)

def add_participant(participant: str, answers: dict[str, str]):
    global dictionary_answers
    cleaned_answers = {key: value.replace(' ', '') for key, value in answers.items()}
    dictionary_answers[participant] = cleaned_answers

def calculate_all() -> dict[str, int]:
    scores = {}
    fields = list(valid_words.keys())

    for participant, answers in dictionary_answers.items():
        score = 0
        for field in fields:
            response = answers.get(field, "").replace(' ', '')
            if response == "":
                continue
            if response not in valid_words.get(field, set()):
                continue
            count = sum(1 for other, ans in dictionary_answers.items()
                        if other != participant and ans.get(field, "").replace(' ', '') == response)
            if count == 0:
                score += 15
            elif count == 1:
                score += 10
            else:
                score += 5
        scores[participant] = score
    return scores
