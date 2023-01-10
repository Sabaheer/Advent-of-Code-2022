def solution(task):
    structure_file = open('data/5-structure.in')
    moves_file = open('data/5-moves.in')
    raw_crate_list = structure_file.readlines()[::-1]
    raw_moves = moves_file.readlines()
    crate_dict = map_input_structure_to_dict(raw_crate_list)
    move_list = map_moves_to_list(raw_moves)
    for current_move in move_list:
        crate_dict = move_crates(crate_dict, current_move, task)
    return ''.join([column[-1] for column in crate_dict.values()])