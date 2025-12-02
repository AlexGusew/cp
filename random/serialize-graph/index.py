from collections import defaultdict
from typing import Optional

# List<Integer> encode(Node root);
# Node decode(List<Integer> encodedList>);


class Node:
    def __init__(self, val: int):
        self.val = val
        self.children = []


def encode(root: Node) -> list[int]:
    adj = defaultdict(list)
    res = []

    def dfs(node, seen):
        if node in seen:
            return
        seen.add(node)
        adj[node]
        for nei in node.children:
            if nei in seen:
                continue
            adj[node].append(nei)
            dfs(nei, seen)

    dfs(root, set())

    for node, neis in adj.items():
        res.extend([node.val, len(neis), *[nei.val for nei in neis]])

    return res


def decode(serialized: list[int]) -> Optional[Node]:
    i = 0
    valNode = {}

    while i < len(serialized):
        val = serialized[i]
        if val not in valNode:
            valNode[val] = Node(val)
        childCount = serialized[i + 1]
        i += 2
        for _ in range(childCount):
            nei = serialized[i]
            if nei not in valNode:
                valNode[nei] = Node(nei)
            valNode[val].children.append(valNode[nei])
            i += 1

    return valNode[serialized[0]]


def get_tree_structure(node, visited=None):
    """Convert tree to dict for comparison"""
    if node is None:
        return None
    if visited is None:
        visited = set()
    if node in visited:
        return {}
    visited.add(node)
    result = {node.val: sorted([child.val for child in node.children])}
    for child in node.children:
        result.update(get_tree_structure(child, visited))
    return result


# Tests
def test_single_node():
    """Test a tree with just one node"""
    root = Node(1)
    encoded = encode(root)
    decoded = decode(encoded)
    assert decoded.val == 1
    assert len(decoded.children) == 0
    print("✓ test_single_node passed")


def test_root_with_one_child():
    """Test: 1 -> 2"""
    root = Node(1)
    child = Node(2)
    root.children.append(child)

    encoded = encode(root)
    decoded = decode(encoded)

    assert decoded.val == 1
    assert len(decoded.children) == 1
    assert decoded.children[0].val == 2
    print("✓ test_root_with_one_child passed")


def test_root_with_three_children():
    """Test: 1 -> [2, 3, 4]"""
    root = Node(1)
    root.children = [Node(2), Node(3), Node(4)]

    encoded = encode(root)
    decoded = decode(encoded)

    assert decoded.val == 1
    assert len(decoded.children) == 3
    child_vals = sorted([c.val for c in decoded.children])
    assert child_vals == [2, 3, 4]
    print("✓ test_root_with_three_children passed")


def test_two_level_tree():
    """
    Test:
        1
       / \
      2   3
     /
    4
    """
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    grandchild = Node(4)

    root.children = [child1, child2]
    child1.children = [grandchild]

    encoded = encode(root)
    decoded = decode(encoded)

    structure = get_tree_structure(decoded)
    print(structure)
    assert structure[1] == [2, 3]
    assert structure[2] == [4]
    assert structure[3] == []
    assert structure[4] == []
    print("✓ test_two_level_tree passed")


def test_linear_chain():
    """Test: 1 -> 2 -> 3 -> 4"""
    nodes = [Node(i) for i in range(1, 5)]
    for i in range(len(nodes) - 1):
        nodes[i].children = [nodes[i + 1]]

    root = nodes[0]
    encoded = encode(root)
    decoded = decode(encoded)

    # Walk the chain
    current = decoded
    for expected_val in range(1, 5):
        assert current.val == expected_val
        if expected_val < 4:
            assert len(current.children) == 1
            current = current.children[0]
        else:
            assert len(current.children) == 0
    print("✓ test_linear_chain passed")


def test_complex_tree():
    """
    Test:
          1
        / | \
       2  3  4
      /   |   \
     5    6    7
    """
    root = Node(1)
    n2, n3, n4 = Node(2), Node(3), Node(4)
    n5, n6, n7 = Node(5), Node(6), Node(7)

    root.children = [n2, n3, n4]
    n2.children = [n5]
    n3.children = [n6]
    n4.children = [n7]

    encoded = encode(root)
    decoded = decode(encoded)

    structure = get_tree_structure(decoded)
    assert structure[1] == [2, 3, 4]
    assert structure[2] == [5]
    assert structure[3] == [6]
    assert structure[4] == [7]
    print("✓ test_complex_tree passed")


def test_negative_values():
    """Test with negative numbers"""
    root = Node(-1)
    root.children = [Node(-2), Node(-3)]

    encoded = encode(root)
    decoded = decode(encoded)

    assert decoded.val == -1
    child_vals = sorted([c.val for c in decoded.children])
    assert child_vals == [-3, -2]
    print("✓ test_negative_values passed")


def test_zero_value():
    """Test with zero"""
    root = Node(0)
    root.children = [Node(1), Node(2)]

    encoded = encode(root)
    decoded = decode(encoded)

    assert decoded.val == 0
    assert len(decoded.children) == 2
    print("✓ test_zero_value passed")


def test_encode_output_is_list():
    """Verify encode returns a list"""
    root = Node(1)
    encoded = encode(root)
    assert isinstance(encoded, list)
    print("✓ test_encode_output_is_list passed")


def run_all_tests():
    """Run all tests and report results"""
    tests = [
        test_single_node,
        test_root_with_one_child,
        test_root_with_three_children,
        test_two_level_tree,
        test_linear_chain,
        test_complex_tree,
        test_negative_values,
        test_zero_value,
        test_encode_output_is_list,
    ]

    print("Running tests...\n")
    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1

    print(f"\n{'=' * 50}")
    print(f"Results: {passed} passed, {failed} failed")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    run_all_tests()
