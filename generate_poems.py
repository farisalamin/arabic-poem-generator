import rhymes
import markovify
from tqdm import tqdm

def markov(text_file):
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()
    text_model = markovify.NewlineText(text)
    return text_model

def generate_poem_single_rhyme(poet_name, rhyme, iterations=3000, use_tqdm=False):
    n_of_rhyme_letters = len(rhyme)
    input_file = './input/{}.txt'.format(poet_name)
    text_model = markov(input_file)
    rhymes_list = rhymes.rhymes_with_last_n_chars(rhyme, n_of_rhyme_letters)
    bayts = set()
    used_rhymes = set()

    poem = ""

    if use_tqdm == True:
        if hasattr(tqdm, '_instances'): tqdm._instances.clear()
        it_range = tqdm(range(iterations))
    else:
        it_range = range(iterations)

    for i in it_range:
        bayt = text_model.make_short_sentence(280, tries=100)
        last_word = bayt.split()[-1]
        if (last_word in rhymes_list) and (last_word not in used_rhymes) and (bayt not in bayts):
            bayts.add(bayt)
            used_rhymes.add(last_word)
            poem += "{}\n".format(bayt)
            if not use_tqdm:
                print(bayt)
    return poem

def generate_poem_2_rhymes(poet_name, rhyme_1, rhyme_2, iterations=3000, use_tqdm=False):
    n_of_rhyme_1_letters = len(rhyme_1)
    n_of_rhyme_2_letters = len(rhyme_2)

    input_file = './input/{}.txt'.format(poet_name)
    text_model = markov(input_file)

    rhymes_1_list = rhymes.rhymes_with_last_n_chars(rhyme_1, n_of_rhyme_1_letters)
    rhymes_2_list = rhymes.rhymes_with_last_n_chars(rhyme_2, n_of_rhyme_2_letters)

    bayts_1 = set()
    bayts_2 = set()

    used_rhymes_1 = set()
    used_rhymes_2 = set()

    poem = ""

    if use_tqdm == True:
        if hasattr(tqdm, '_instances'): tqdm._instances.clear()
        it_range = tqdm(range(iterations))
    else:
        it_range = range(iterations)

    for i in it_range:
        bayt = text_model.make_short_sentence(280, tries=100)
        last_word = bayt.split()[-1]

        if (last_word in rhymes_1_list) and (last_word not in used_rhymes_1) and (bayt not in bayts_1):
            bayts_1.add(bayt)
            used_rhymes_1.add(last_word)

        if (last_word in rhymes_2_list) and (last_word not in used_rhymes_2) and (bayt not in bayts_2):
            bayts_2.add(bayt)
            used_rhymes_2.add(last_word)

    len_of_poem = min(len(bayts_1), len(bayts_2))
    for i in range(len_of_poem):
        poem += "{}\n{}\n".format(list(bayts_1)[i], list(bayts_2)[i])

    return poem

# x = generate_poem_single_rhyme(
#                             'ذو الرمة',
#                             'الا',
#                             iterations=3000,
#                             use_tqdm=False
#                             )
