import json
import yaml


def get_file():
    with open("data.json", encoding="utf-8") as file:
        return json.load(file)


if __name__ == '__main__':
    ppls = get_file()
    ppl_ages = ppls['ppl_ages']
    summary = {}
    for k, v in ppl_ages.items():
        if v < 11:
            if '11' not in summary:
                summary['11'] = []
            summary['11'].append(k)
        elif 11 <= v < 20:
            if '11-20' not in summary:
                summary['11-20'] = []
            summary['11-20'].append(k)
        elif 20 <= v < 25:
            if '20-25' not in summary:
                summary['20-25'] = []
            summary['20-25'].append(k)
        elif 25 <= v < 40:
            if '25-40' not in summary:
                summary['25-40'] = []
            summary['25-40'].append(k)
        elif 40 <= v < 102:
            if '40-102' not in summary:
                summary['40-102'] = []
            summary['40-102'].append(k)
        with open('data.yaml', 'w', encoding='utf-8') as data:
            yaml.dump(summary, data)
    print(summary)
