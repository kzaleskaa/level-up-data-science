import copy


class Vertex:
    """Class represents every number (vertex) in given triangle."""

    def __init__(self, value: int, cumulated_sum: int = 0, paths: list = []):
        """Vertex constructor.

        Args:
            value (int) - number representing a given vertex
            cumulated_sum (int) - sum calculated from the bottom to the top of the triangle.
            paths (list) - maximum paths from the bottom to a given vertex
        """
        self.value = value
        self.paths = paths
        self.cumulated_sum = cumulated_sum


def read_from_file(path: str) -> list:
    """Read input data from file and create list.

    Args:
        path (str) - path to text file with input data

    Return:
        array_lines (list) - a list representing the elements of each row
    """

    with open(path, 'r') as f:
        content = f.readlines()

        array_lines = []

        for line in content:
            el = []

            for i in line:
                if i.isdigit():
                    el.append(int(i))

            array_lines.append(el)

    return array_lines


def create_vertex(path: str) -> list:
    """Create list of Vertex.

    Args:
        path (str) - path to text file with input data

    Return:
        A (list) - a list representing vertices
    """
    A = read_from_file(path)

    n = len(A)

    for row in reversed(range(n)):
        for column in range(len(A[row])):
            if row == n - 1:
                A[row][column] = Vertex(A[row][column], cumulated_sum=A[row][column], paths=[str(A[row][column])])
            else:
                A[row][column] = Vertex(A[row][column], cumulated_sum=A[row][column])

    return A


def update_paths(number: int, new_paths: list) -> list:
    """Create new paths for parent vertex.

    Args:
        number (int) - value of parent vertex
        new_paths (list) - paths to left/right child

    Return:
        paths (list) - updated paths
    """
    paths = copy.deepcopy(new_paths)

    for idx, x in enumerate(new_paths):
        paths[idx] = str(number) + paths[idx]

    return paths


def calculate_paths(path: str) -> tuple:
    """
    Calculate max sum and print path.

    Args:
        path (str) - path to text file with input data
    """
    vertex = create_vertex(path)

    # length of list without last line
    n = len(vertex[:-1])

    # go through the triangle from bottom to top
    for row in reversed(range(n)):

        # check the neighbors of each element in selected row
        for column in range(len(vertex[row])):

            basic_vertex = vertex[row][column]
            left_child = vertex[row + 1][column]
            right_child = vertex[row + 1][column + 1]

            # update path based od neighbours
            if left_child.cumulated_sum > right_child.cumulated_sum:
                basic_vertex.paths = update_paths(basic_vertex.value, left_child.paths)
            elif left_child.cumulated_sum < right_child.cumulated_sum:
                basic_vertex.paths = update_paths(basic_vertex.value, right_child.paths)
            else:
                left_paths = update_paths(basic_vertex.value, left_child.paths)
                right_paths = update_paths(basic_vertex.value, right_child.paths)
                basic_vertex.paths = left_paths + right_paths

            # update the sum by selecting the largest neighbor
            basic_vertex.cumulated_sum += max(left_child.cumulated_sum, right_child.cumulated_sum)

    return vertex[0][0].cumulated_sum, vertex[0][0].paths


def find_sum_and_path(path: str) -> None:
    """Print maximum sum and every possible path.

    Args:
        path (str) - path to text file with input data
    """
    max_sum, paths = calculate_paths(path)

    # max calculated sum
    print(max_sum)

    # paths
    for x in paths:
        print(x)


if __name__ == "__main__":
    find_sum_and_path("1-very_easy.txt")
    find_sum_and_path("2-easy.txt")
    find_sum_and_path("3-medium.txt")

