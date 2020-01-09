from typing import List
from sympy import Symbol, Eq, solve


def roulette_minimum(probability_list: List) -> List:
    """
    This function, given a list of probabilities for events, reverse the probabilities while keeping proportions.

    :param probability_list: List with the probabilities of event occurrences.
    :return: List with reversed probabilities.
    """

    # Create a list of symbols representing each of events and get both value and symbol for least probable to occur
    # event.
    symbols_list = [Symbol(f'x_{i}') for i, _ in enumerate(probability_list)]
    least_probable_value = min(probability_list)
    least_probable_symbol = symbols_list[probability_list.index(least_probable_value)]

    # Create list containing proportions of probability of least probable event to all others.
    proportions_list = [round(least_probable_value / probability, 2) for probability in probability_list]

    # Create expressions list and calculate reversed value for least probable event.
    expressions_list = [proportions_list[i] * least_probable_symbol for i in range(len(probability_list))]
    least_probable_value_reversed = round(solve(Eq(sum(expressions_list), 1))[0], 2)

    # Lastly return a list of reversed values, calculated by substituting symbols in expressions list.

    return [round(expression.subs(least_probable_symbol, least_probable_value_reversed), 2) for expression
            in expressions_list]


# Calculate values for some examples:
for probs in [[0.1, 0.5, 0.25, 0.15], [0.4, 0.4, 0.2]]:
    results = roulette_minimum(probs)
    print(results)
