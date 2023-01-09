import pandas as pd
from tqdm import tqdm

df = pd.read_csv("Arabic_poetry_dataset.csv", encoding="utf-8")

allowed_chars = ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'د', 'ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م',
                 'ك', 'ط', 'ئ', 'ء', 'ؤ', 'ر' , 'ى', 'ة', 'و', 'ز', 'ظ', 'إ' ,'أ', 'آ', ' ', '\n', 'ذ', 'ّ']

def delete_puncs(poem):
    for l in poem:
        if l not in allowed_chars:
            poem = poem.replace(l, "")
    return poem

def extract_poems(poet_name):
    with open('./input/{}.txt'.format(poet_name), 'w', encoding="utf-8") as f:
        for i in range(len(df)):
            if df['poet_name'][i].format(poet_name) == poet_name:
                poem = delete_puncs(df['poem_text'][i])
                f.write("{}\n\n".format(poem))

all_poets = set()
for poet_name in df['poet_name']:
    all_poets.add(poet_name)

# for poet in tqdm(all_poets):
#     extract_poems(poet)

# extract_poems('أبو العلاء المعري')
