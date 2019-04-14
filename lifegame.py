'''
Created on Apr 12, 2019

@author: yulay
'''
import random


class Lifegame:

    def __init__(self, ncols, nrows, cell_alive_probability):
        self.ncols = ncols
        self.nrows = nrows
        self.generation = 0
        self.alive_cells = []
        self.cells_with_alive_neighbour = set()
        self.field = self._get_new_field()
        self._set_random_init_field(cell_alive_probability)
    
    def _set_random_init_field(self, cell_alive_probability):
        for icol in range(self.ncols):
            for irow in range(self.nrows):
                if random.random() < cell_alive_probability:
                    self.field[icol][irow] = 1 
                    self.alive_cells.append((icol, irow))
                    self.cells_with_alive_neighbour.update(self._get_set_cells_with_alive_neighbour(icol, irow))
                else :
                    self.field[icol][irow] = 0
        self._count_neighbours()
    
    def set_next_generation_field(self):
        field_next_generation = self._get_new_field()
        alive_cells_next_generation = []
        cells_with_alive_neighbour_next_generation = set()
        
#         for cell in self.cells_with_alive_neighbour:
#             icol = cell[0]
#             irow = cell[1]
#             field_next_generation[icol][irow] = self._will_cell_live_in_next_generation(icol, irow)
#             if(field_next_generation[icol][irow] == 1):
#                 alive_cells_next_generation.append((icol, irow))
#                 cells_with_alive_neighbour_next_generation.update(self._get_set_cells_with_alive_neighbour(icol, irow))
          
        for icol in range(self.ncols):
            for irow in range(self.nrows):
                field_next_generation[icol][irow] = self._will_cell_live_in_next_generation(icol, irow)
                if(field_next_generation[icol][irow] == 1):
                    alive_cells_next_generation.append((icol, irow))
                    
        self.field = field_next_generation
        self.alive_cells = alive_cells_next_generation
        self.cells_with_alive_neighbour = cells_with_alive_neighbour_next_generation
        self.generation += 1
        self._count_neighbours()
        
    def _get_new_field(self):
        new_field = [0] * self.ncols
        for icol in range(self.ncols):
            new_field[icol] = [0] * self.nrows
        return new_field

    def _get_empty_neighbours_counter(self):
        return self._get_new_field()
    
    def _will_cell_live_in_next_generation(self, icol, irow):
        nneighbours = self.nneighbours[icol][irow]
        if self.field[icol][irow] == 0:
            if nneighbours == 3:
                return True
            else:
                return False
        if self.field[icol][irow] == 1:
            if nneighbours < 2 or nneighbours > 3:
                return False
            else:
                return True

    def _get_set_cells_with_alive_neighbour(self, col, row):
        cells_with_alive_neighbour = set()
        cells_with_alive_neighbour.add((col - 1, row - 1))
        cells_with_alive_neighbour.add((col , row - 1))
        cells_with_alive_neighbour.add(((col + 1) % self.ncols, row - 1))
        cells_with_alive_neighbour.add((col - 1, row))
        cells_with_alive_neighbour.add((col, row))
        cells_with_alive_neighbour.add(((col + 1) % self.ncols, row))
        cells_with_alive_neighbour.add((col - 1, (row + 1) % self.nrows))
        cells_with_alive_neighbour.add((col , (row + 1) % self.nrows))
        cells_with_alive_neighbour.add(((col + 1) % self.ncols, (row + 1) % self.nrows))
        return cells_with_alive_neighbour
            
    def _count_neighbours(self):
        self.nneighbours = self._get_empty_neighbours_counter()
        for cell in self.alive_cells:
            col = cell[0]
            row = cell[1]
            self.nneighbours[col - 1][row - 1] += 1
            self.nneighbours[col][row - 1] += 1
            self.nneighbours[(col + 1) % self.ncols][row - 1] += 1
            self.nneighbours[col - 1][row] += 1
            self.nneighbours[(col + 1) % self.ncols][row] += 1
            self.nneighbours[col - 1][(row + 1) % self.nrows] += 1
            self.nneighbours[col][(row + 1) % self.nrows] += 1
            self.nneighbours[(col + 1) % self.ncols][(row + 1) % self.nrows] += 1
