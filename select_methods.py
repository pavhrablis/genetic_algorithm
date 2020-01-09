from typing import List
from sympy import Symbol, Eq, solve
import random 

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


def rolette_select(eval_list : List , max : bool) -> List:
    """
    :
    :
    """

    #
    F = sum(eval_list)
    #
    probability = [round(eval_list[i] / F, 2) for i in range(0,len(eval_list))]

    #
    if max:
        probability_list = probability
    else:
        probability_list = roulette_minimum(probability)
    
    #calculate cumulative distribution
    cumulative_distribution = []
    for i in range(0,len(probability_list)):
        distribut = 0

        for j in range(0,i):
        
            distribut += probability_list[j]
        cumulative_distribution.append(distribut)
    cumulative_distribution.append(1.0)
    index_select_individual = []

    #
    j = 0 
    while j < len(probability_list):
        r = random.random()
        for i in range(0,len(cumulative_distribution)):
    
            
            if r < cumulative_distribution[1]:
    
                index_select_individual.append(1)
    
            else:
                if r > cumulative_distribution[i - 1] and r <= cumulative_distribution[i]:
                    index_select_individual.append(i)
        j+=1
    return index_select_individual

    #

    #


def ranking_select(eval_list : List , max : bool) -> List:
    """
    :
    :
    """
    sort_list = eval_list.sort()

    if max:

        sort_list = sort_list

    else:

        sort_list = sort_list.reverse()
    
    lista_wybranych = []

    i = 0 
    while i < len(eval_list):
        r = random.randint(0,random.randint(0,len(eval_list)))
        lista_wybranych.append(r)
        i+=1
    return lista_wybranych


def turniowa_select(eval_list : List , return0 : bool, number_subgroup : int) -> List:

    subgroup = []

    lista_wybranych = []
    if return0:
        for j in range(0, len(eval_list)):
            subgroup = [random.randint(0,len(eval_list)- 1) for i in range(0,number_subgroup)]
            list_help = []
            for i in range(0,len(subgroup)):
                list_help.append(eval_list[subgroup[i]])
                max_el = max(list_help)
            lista_wybranych.append(eval_list.index(max_el))
    else:
        for j in range(0,len(eval_list)):
            subgroup = []
            i = 0
            while i < number_subgroup:
                r = random.randint(0,len(eval_list) - 1)
                if r  in subgroup:
                    continue
                else:
                    subgroup.append(r)
                    i+=1
            list_help = []
            for i in range(0,len(subgroup)):
                list_help.append(eval_list[subgroup[i]])
                max_el = max(list_help)
            lista_wybranych.append(eval_list.index(max_el))  
    
    return lista_wybranych







        
        

eval_list = [16.826777962367217,13.171331488048155,20.108812912369757,11.252849360449007,20.671484392316017,17.604844551829707,9.117624983846248,14.608048390393867,9.622431694170567,16.884451337374287] 

"""
# Calculate values for some examples:
for probs in [[0.1, 0.5, 0.25, 0.15], [0.4, 0.4, 0.2]]:
    results = roulette_minimum(probs)
    print(results)
"""


#print(rolette_select(eval_list,True))
#print(ranking_select(eval_list,True))
#print(turniowa_select(eval_list,False, 3))

#calkowite 
# 

















