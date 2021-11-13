from freelance.task1.client_test_cases import SOURCE_TEXT_1, SOURCE_TEXT_2, SOURCE_TEXT_3
from string import Template


def source_to_destination_text(source_text: str) -> str:
    # TODO: реализовать функцию, которая преобразует текст сообщения из формата source channel в формат
    #  destination channel
    pair = ""
    action = ""
    entry_pr = ""
    sl = ""
    tp = ""
    nb = ""
    end_string = ""
    text_lines = source_text.split("\n")
    for line in text_lines:
        line_lower = line.lower()
        if line_lower.startswith("instrument:"):
            line = line.strip()
            line_parts = line.split(" ")
            pair = line_parts[-1]
            pair = pair.replace("/", "")
        if line_lower.startswith("my opinion:"):
            line_lower = line_lower.strip()
            line_parts = line_lower.split(" ")
            if line_parts[3] == "limit" or line_parts[3] == "stop":
                action = " ".join(line_parts[2:4]).upper()
            else: action = line_parts[2].upper()
        if line_lower.startswith("entry price:"):
            line = line.strip()
            line_parts = line.split(" ")
            entry_pr = line_parts[-1]
        if line_lower.startswith("stop:"):
            line = line.strip()
            line_parts = line.split(" ")
            sl = line_parts[-1]
        if line_lower.startswith("target:"):
            line = line.strip()
            line_parts = line.split(" ")
            tp = line_parts[-1]
        if line_lower.startswith("nb:"):
            line = line.strip()
            line_parts = line.split(" ")
            nb = line_parts[-2]
    if nb != '':
        answer = Template(destination_text_1)
        return answer.substitute(pair=pair, action=action, entry_pr=entry_pr, tp=tp, sl=sl, nb=nb)
    else:
        answer = Template(destination_text_2)
        return answer.substitute(pair=pair, action=action, entry_pr=entry_pr, tp=tp, sl=sl)

destination_text_1 = '''🔥 $pair - $action $entry_pr

🟢 TP $tp
❌ SL $sl

👉 close if not triggered within $nb hours'''
destination_text_2 = '''🔥 $pair - $action $entry_pr

🟢 TP $tp
❌ SL $sl'''
