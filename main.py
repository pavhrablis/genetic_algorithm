import argparse
import numpy as np
from generate_population import calculate_m, create_matrix, convert_rows_binary_numbers, przesuniecie_do_przedzialu_ab,gen_population
from select_methods import ranking_select
from mutation import mutation, inversion
from krzyzowanie import crucifixion
from statistics import mean
def main(args=None):
    
    parser = argparse.ArgumentParser(description= 'Parametrs for genetic algorithm')
    parser.add_argument('--epochs',help='number epochs', type=int,default=10)
    parser.add_argument('--mutation',help='mutation', type=bool,default=True)
    parser.add_argument('--inversion',help='inversion', type=bool,default=False)
    #parser.add_argument('--suksesfull',help='suksesja calkowita,elitarna,losowa',type=str)
    args = parser.parse_args(args)

    p_mutation = 0.1
    p_inversion = 0.1
    dokladnosc = 6
    a = -1 
    b = 1
    ilosc_lancuchow_binarnych = 10

    m = calculate_m(dokladnosc, a ,b)
    pop_binary = create_matrix(ilosc_lancuchow_binarnych,m)
    maxi = []
    for _ in range(args.epochs):
        

        liczbe_dzies = convert_rows_binary_numbers(pop_binary)
        
        liczby_z_ab = przesuniecie_do_przedzialu_ab(liczbe_dzies, a, b, m )
        
        population_eval = gen_population(liczby_z_ab)

        index_select_pop = ranking_select(population_eval, max=True)

        list_population = [list(pop_binary[i]) for i in range(0,pop_binary.shape[0])]

        select_population = np.asarray([list_population[i] for i in index_select_pop]) 

        if args.mutation:

            pop_binary = mutation(select_population,p_mutation)

        if args.inversion:

            pop_binary = inversion(pop_binary,p_inversion)

        #suksesja

        crucifixion_pop = crucifixion(pop_binary)

        sukses = np.vstack((pop_binary,np.array(crucifixion_pop)))

        ld = convert_rows_binary_numbers(sukses)

        ab = przesuniecie_do_przedzialu_ab(ld,a,b,m)

        pop = gen_population(ab)
        
        pop.sort()
        
        new_pop = pop[1:10] 

        index = [pop.index(i) for i in new_pop]

        new_pop_binary = [sukses[i] for i in index]

        max_f = max(new_pop)

        maxi.append(max_f)

        pop_binary = np.array(new_pop_binary)
    print(mean(maxi))


if __name__== "__main__":
    main()

