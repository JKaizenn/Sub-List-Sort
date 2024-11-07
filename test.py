
#Test Cases for Sub-List Sort Program
from main import sort_sublists

def test_sort_sublists():
    # Test case 1: Regular case with positive integers
    input_data = [[3, 2, 1], [6, 5, 4]]
    expected_output = [[1, 2, 3], [4, 5, 6]]
    assert sort_sublists(input_data) == expected_output

    # Test case 2: Case with negative integers
    input_data = [[-3, -2, -1], [-6, -5, -4]]
    expected_output = [[-3, -2, -1], [-6, -5, -4]]
    assert sort_sublists(input_data) == expected_output

    # Test case 3: Case with mixed positive and negative integers
    input_data = [[3, -2, 1], [-6, 5, -4]]
    expected_output = [[-2, 1, 3], [-6, -4, 5]]
    assert sort_sublists(input_data) == expected_output

    # Test case 4: Case with empty sub-lists
    input_data = [[], [3, 2, 1]]
    expected_output = [[], [1, 2, 3]]
    assert sort_sublists(input_data) == expected_output

    # Test case 5: Case with single element sub-lists
    input_data = [[1], [2], [3]]
    expected_output = [[1], [2], [3]]
    assert sort_sublists(input_data) == expected_output

    # Test case 6: Case with already sorted sub-lists
    input_data = [[1, 2, 3], [4, 5, 6]]
    expected_output = [[1, 2, 3], [4, 5, 6]]
    assert sort_sublists(input_data) == expected_output

    # Test case 7: Case with duplicate elements in sub-lists
    input_data = [[3, 3, 1], [6, 5, 5]]
    expected_output = [[1, 3, 3], [5, 5, 6]]
    assert sort_sublists(input_data) == expected_output

if __name__ == "__main__":
    test_sort_sublists()
    print("All tests passed.")