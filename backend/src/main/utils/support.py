import pandas as pd
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
from typing import Tuple, List, Dict, Union


def create_clause(_range: Tuple[int, int], name: str, dict_terms: Dict[str, List[float]], ant_cons=0) -> (
        Union)[ctrl.Antecedent, ctrl.Consequent]:
    if ant_cons == 0:
        clause = ctrl.Antecedent(np.arange(*_range), name)
    else:
        clause = ctrl.Consequent(np.arange(*_range), name)

    for term, values in dict_terms.items():
        if len(values) == 3:
            clause[term] = fuzzy.trimf(clause.universe, values)
        elif len(values) == 4:
            clause[term] = fuzzy.trapmf(clause.universe, values)
        else:
            raise ValueError("Não há função para isso")

    return clause


def create_rule(activating_antecedents_terms: List[ctrl.Antecedent],
                consequent_term_expected: [ctrl.Consequent]) -> ctrl.Rule:
    set_of_rules = activating_antecedents_terms[0]
    for term in activating_antecedents_terms[1:]:
        set_of_rules &= term

    return ctrl.Rule(set_of_rules, consequent_term_expected)


def create_multiple_rules(antecedents_list: List[ctrl.Antecedent], results_dict: Dict[str, List[str]],
                          expected_consequent: ctrl.Consequent) -> List[ctrl.Rule]:
    rules = []
    for expected_term, set_of_rules in results_dict.items():
        expected_result_list = []
        for antecedent, term in zip(antecedents_list, set_of_rules):
            expected_result_list.append(antecedent[term])

        rules.append(create_rule(expected_result_list, expected_consequent[expected_term]))

    return rules


def split_antecedents_names(df: pd.DataFrame) -> List[str]:
    names = []
    for col in df.columns:
        parts = col.split('_')
        if parts[0] not in names:
            names.append(parts[0])
    return names[:-1]


def set_terms_to_dictionary(df: pd.DataFrame, name: str) -> Dict[str, List[float]]:
    df_filtered = df.filter(regex=name, axis=1)
    result = {}

    for col in df_filtered.columns:
        parts = col.split('_')
        key_name = parts[1]
        values = df_filtered[col].tolist()
        values = [float((str(val).replace(',', '.'))) if pd.notna(val) else np.nan for val in values]
        values = [val for val in values if not np.isnan(val)]
        result[key_name] = values

    return result


def set_sentences(df: pd.DataFrame) -> Dict[str, List[str]]:
    sentences = {}

    for index, row in df.iterrows():
        expected_value = row.tolist()[0]
        conditional_terms = row.tolist()[1:]
        sentences[expected_value] = conditional_terms

    return sentences


def find_result(items: Dict[str, List[float]], value: float) -> str:
    for key, values in items.items():
        if min(values) <= value <= max(values):
            return key
