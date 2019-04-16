# Średnica kulki 5 cm
# Stół 300 x 150 cm

class World:
    def __init__(self):
        # milimeters
        self.__MAX_X__ = 3000
        self.__MAX_Y__ = 1500
        self.__GRID_COUNT_X__ = 30
        self.__GRID_COUNT_Y__ = 15
        self.grid = []
        self.__initialize_grid__()

    def __initialize_grid__(self):
        for y in range(self.__GRID_COUNT_Y__):
            self.grid.append([])
            for x in range(self.__GRID_COUNT_X__):
                self.grid[y].append([])

    def __calculate_grid_index__(self, x: float, y: float) -> (int, int):
        return (int(x / self.__MAX_X__ * self.__GRID_COUNT_X__), int(y / self.__MAX_Y__ * self.__GRID_COUNT_Y__))
