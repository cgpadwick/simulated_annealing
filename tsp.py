class TravelingSalesmanProblem:
  """Representation of a traveling salesman optimization problem.  The goal
  is to find the shortest path that visits every city in a closed loop path.

  Students should only need to implement or modify the successors() and
  get_values() methods.

  Parameters
  ----------
  cities : list
      A list of cities specified by a tuple containing the name and the x, y
      location of the city on a grid. e.g., ("Atlanta", (585.6, 376.8))

  Attributes
  ----------
  names
  coords
  path : list
      The current path between cities as specified by the order of the city
      tuples in the list.
  """

  def __init__(self, cities):
    self.path = copy.deepcopy(cities)

  def copy(self):
    """Return a copy of the current board state."""
    new_tsp = TravelingSalesmanProblem(self.path)
    return new_tsp

  @property
  def names(self):
    """Strip and return only the city name from each element of the
    path list. For example,
        [("Atlanta", (585.6, 376.8)), ...] -> ["Atlanta", ...]
    """
    names, _ = zip(*self.path)
    return names

  @property
  def coords(self):
    """Strip the city name from each element of the path list and return
    a list of tuples containing only pairs of xy coordinates for the
    cities. For example,
        [("Atlanta", (585.6, 376.8)), ...] -> [(585.6, 376.8), ...]
    """
    _, coords = zip(*self.path)
    return coords

  def successors(self):
    """Return a list of states in the neighborhood of the current state by
    switching the order in which any adjacent pair of cities is visited.

    For example, if the current list of cities (i.e., the path) is [A, B, C, D]
    then the neighbors will include [A, B, D, C], [A, C, B, D], [B, A, C, D],
    and [D, B, C, A]. (The order of successors does not matter.)

    In general, a path of N cities will have N neighbors (note that path wraps
    around the end of the list between the first and last cities).

    Returns
    -------
    list<Problem>
        A list of TravelingSalesmanProblem instances initialized with their list
        of cities set to one of the neighboring permutations of cities in the
        present state
    """

    # find the adjacent pairs.
    pairs = []
    for idx in range(len(self.path) - 1):
      pairs.append((self.path[idx], self.path[idx + 1]))
    pairs.append((self.path[0], self.path[-1]))

    rtn_list = []
    for p in pairs:
      idx0 = self.path.index(p[0])
      idx1 = self.path.index(p[1])
      cities_copy = copy.deepcopy(self.path)
      cities_copy[idx0] = p[1]
      cities_copy[idx1] = p[0]
      rtn_list.append(TravelingSalesmanProblem(cities_copy))

    print rtn_list

    rtn_list

  def get_value(self):
    """Calculate the total length of the closed-circuit path of the current
    state by summing the distance between every pair of adjacent cities.  Since
    the default simulated annealing algorithm seeks to maximize the objective
    function, return -1x the path length. (Multiplying by -1 makes the smallest
    path the smallest negative number, which is the maximum value.)

    Returns
    -------
    float
        A floating point value with the total cost of the path given by visiting
        the cities in the order according to the self.cities list

    Notes
    -----
        (1) Remember to include the edge from the last city back to the
        first city

        (2) Remember to multiply the path length by -1 so that simulated
        annealing finds the shortest path
    """
    raise NotImplementedError