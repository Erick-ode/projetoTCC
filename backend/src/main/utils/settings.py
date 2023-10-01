from ..utils.support import split_antecedents_names, set_terms_to_dictionary, create_clause, \
    set_sentences, pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TERMS_CSV_PATH = os.path.join(BASE_DIR, '..', 'terms_and_values', 'terms.csv')
RULES_CSV_PATH = os.path.join(BASE_DIR, '..', 'terms_and_values', 'rules.csv')

DF_TERMS = pd.read_csv(TERMS_CSV_PATH, sep=';')
DF_RULES = pd.read_csv(RULES_CSV_PATH, sep=';')

LIMITS = [12, 200, 30, 48, 100, 10, 100]
ANTECEDENTS_NAMES = split_antecedents_names(DF_TERMS)

CONSEQUENT_DATA = set_terms_to_dictionary(DF_TERMS, 'tecnica')
CONSEQUENT = create_clause((0, 110), 'tecnica', CONSEQUENT_DATA, 1)

SENTENCES = set_sentences(DF_RULES)

ANTECEDENTS_DATA = [set_terms_to_dictionary(DF_TERMS, name) for name in ANTECEDENTS_NAMES]
