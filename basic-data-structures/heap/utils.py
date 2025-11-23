def get_left_child_index(parent_idx) -> int:
    return 2 * parent_idx + 1

def get_right_child_index(parent_idx) -> int:
    return 2 * parent_idx + 2

def get_parent_index(child_idx) -> int:
    return (child_idx - 1) // 2

def has_parent(idx) -> bool:
    return get_parent_index(idx) >= 0