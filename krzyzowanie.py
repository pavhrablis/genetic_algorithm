import math
import numpy as np 
from typing import List, Tuple
import random


def create_punkt_crucifixion(matrix : np.ndarray , number_punkts : int) -> List:
    
    if number_punkts > matrix.shape[1]:

        number_punkts = matrix.shape[1] - 1

        print('Number punkts > number rows in matrix, number_punkts = matrix.shape[0] - 1') 

        
    punkts = []
    
    number_rows = matrix.shape[0]
    i = 0
    while i < number_punkts:

        punkt = random.randint(0,number_rows - 1)
        
        if punkt in punkts  or punkt == 0:
            continue 

        punkts.append(punkt)

        i+=1

    return punkts


def random_r_chromosom(matrix : np.ndarray) -> List:
    
    return [random.uniform(0,1) for i in range(0,matrix.shape[0])]


def swap(list_1 : List, list_2 : List, index_split : int) -> Tuple:

    sublist_list1_1 = list_1[:index_split]

    sublist_list1_2 = list_1[index_split:]
    
    sublist_list2_1 = list_2[:index_split]
    
    sublist_list2_2 = list_2[index_split:]
    
    new_list_1 = sublist_list1_1 + sublist_list2_2
    
    new_list_2 = sublist_list2_1 + sublist_list1_2

    return new_list_1, new_list_2


def array_to_list(matrix : np.ndarray) -> List:

    return [list(matrix[i]) for i in range(0,matrix.shape[0])]



def crucifixion(matrix : np.ndarray,pk = 0.5, number_punkts = 1) -> np.ndarray:
    
    r = random_r_chromosom(matrix)
    
    list_punkts = create_punkt_crucifixion(matrix, number_punkts)
    
    parents_index =  [r.index(i) for i in r if i < pk]
    
    if len(parents_index) % 2 != 0:

        parents_index.pop(random.randrange(len(parents_index)))
    
    random.shuffle(parents_index)
    
    list_chromosom = array_to_list(matrix)
    
    list_chromosom_crcfxn = [list_chromosom[i] for i in parents_index]

    for i in list_punkts:

        j = 0

        while j < len(list_chromosom_crcfxn):
            
            list_chromosom_crcfxn[j],list_chromosom_crcfxn[j+1] = swap(list_chromosom_crcfxn[j],list_chromosom_crcfxn[j+1],i)

            j += 2
    
    return list_chromosom_crcfxn



        



    
     
