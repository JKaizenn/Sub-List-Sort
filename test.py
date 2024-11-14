
#Test Cases for Sub-List Sort Program
from main import subListSort

def test_sort_sublists():
    # Test empty list
    assert subListSort([]) == []
    
    # Test single sublist
    assert subListSort([[3,2,1]]) == [[1,2,3]]
    
    # Test multiple sublists
    assert subListSort([[3,2,1], [6,5,4]]) == [[1,2,3], [4,5,6]]
    
    # Test sublists of different lengths
    assert subListSort([[3,1], [5,4,2]]) == [[1,3], [2,4,5]]
    
    # Test sublists with negative numbers
    assert subListSort([[-1,-3,-2], [0,2,1]]) == [[-3,-2,-1], [0,1,2]]
    
    # Test sublists with duplicates
    assert subListSort([[2,2,1], [3,3,3]]) == [[1,2,2], [3,3,3]]
    
    # Test single element sublists
    assert subListSort([[1], [2], [3]]) == [[1], [2], [3]]
    
    # Test mixed number types
    assert subListSort([[3.14, 2, 1], [5, 4.5, 4]]) == [[1, 2, 3.14], [4, 4.5, 5]]

    print("All test cases passed!")

if __name__ == "__main__":
    test_sort_sublists()