import numpy as np
import random 
import math


def create_matrix(n,m):
   return np.random.randint(2, size=(n, m))


def convert_rows_binary_numbers(matrix):
  list_numbers = []
  for i in range(matrix.shape[0]):
    binary_numbers = list(matrix[i])
    binary_numbers.reverse()
    length_binary_numbers = len(binary_numbers)
    number = 0
    for j in range(length_binary_numbers):
      number += (binary_numbers[j] * (2**j))
    list_numbers.append(number)
  return list_numbers


def random_rows(matrix):
  number_rows = random.randrange(2,matrix.shape[0])
  if number_rows % 2 != 0:
    number_rows -= 1
  random_rows = []
  while len(random_rows) < number_rows:
    rnd = random.randint(0,matrix.shape[0] - 1)
    if rnd in random_rows:
      continue
    else:
      random_rows.append(rnd)
  return random_rows

def krzyzowanie(matrix):
  rows = random_rows(matrix)
  print("Wybrane losowe wierszy " + str(rows))
  select_rows = []
  final_list = [] 
  for i in rows:   
    select_rows.append(list(matrix[i]))
  print("Macierz z wybranych wierszy")
  print(np.array(select_rows))
  index_split = random.randint(0,matrix.shape[0]-1)
  if index_split == 0:
    index_split = 1
  print("Indeks podzialu wiersza macierzy " + str(index_split))
  i = 0
  while i < len(select_rows):
    list1 = select_rows[i]
    list2 = select_rows[i+1]
    sublist_list1_1 = list1[:index_split]
    sublist_list1_2 = list1[index_split:]
    sublist_list2_1 = list2[:index_split]
    sublist_list2_2 = list2[index_split:]
    new_list_1 = sublist_list1_1 + sublist_list2_2
    new_list_2 = sublist_list2_1 + sublist_list1_2
    final_list.append(new_list_1)
    final_list.append(new_list_2)
    i += 2
  print("Macierz skrzyzowana")
  return np.array(final_list) 

  
  ##############to one methods
def calculate_m(dokladnosc = 6, a = -1 , b = 1):
  m = 0
  dlugosc = b - a
  while (2**m) < (b-a) * 10**dokladnosc:
    m+=1
  return m

def przesuniecie_do_przedzialu_ab(liczbe_dzies, a, b, m ):
  liczby_z_przidzialu_ab = []
  dlugosc = b - a
  ilosc = len(liczbe_dzies)
  for i in range(0,ilosc):
    x = a + ((dlugosc * liczbe_dzies[i]) / (2**m - 1))
    liczby_z_przidzialu_ab.append(x)
  return liczby_z_przidzialu_ab

def f(x,w,A,n):
  return A*n + x**2 - A * math.cos(w * x)

def gen_population(liczby_z_ab):
  pop = []
  ilosc = len(liczby_z_ab)
  for i in range(0,ilosc):
    pop.append(f(liczby_z_ab[i], 20 * math.pi , 10 , 1 ))
  return pop