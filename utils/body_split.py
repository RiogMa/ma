body_parts_all = ['left lower limb', 'right lower limb', 'torso', 'left upper limb', 'right upper limb']


body_chain = [[2, 5, 8, 11],  # llb
              [1, 4, 7, 10],  # rlb
              [3, 6, 9, 12, 15],  # troso
              [9, 14, 17, 19, 21],  # lub
              [9, 13, 16, 18, 20]]  # rub

body_mask_llb = [0] * 263
body_mask_rlb = [0] * 263
body_mask_torso = [0] * 263
body_mask_lub = [0] * 263
body_mask_rub = [0] * 263
body_mask_all = [0] * 263

def set_elements_to_1(mask, indices):
    for index in indices:
        mask[index] = 1

# root
set_elements_to_1(body_mask_llb, list(range(0, 4)))
set_elements_to_1(body_mask_rlb, list(range(0, 4)))
set_elements_to_1(body_mask_torso, list(range(0, 4)))

# foot 
set_elements_to_1(body_mask_llb, list(range(259, 263)))
set_elements_to_1(body_mask_rlb, list(range(259, 263)))
    

# 处理 body_mask_llb
llb_indices = body_chain[0]
for n in llb_indices:
    set_elements_to_1(body_mask_llb, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_mask_llb, list(range(67 + (n - 1) * 6, 67 + n * 6)))
    set_elements_to_1(body_mask_llb, list(range(193 + n * 3, 193 + (n + 1) * 3)))

# 处理 body_mask_rlb
rlb_indices = body_chain[1]
for n in rlb_indices:
    set_elements_to_1(body_mask_rlb, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_mask_rlb, list(range(67 + (n - 1) * 6, 67 + n * 6)))
    set_elements_to_1(body_mask_rlb, list(range(193 + n * 3, 193 + (n + 1) * 3)))

# 处理 body_mask_troso
troso_indices = body_chain[2]
for n in troso_indices:
    set_elements_to_1(body_mask_torso, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_mask_torso, list(range(67 + (n - 1) * 6, 67 + n * 6)))
    set_elements_to_1(body_mask_torso, list(range(193 + n * 3, 193 + (n + 1) * 3)))

# 处理 body_mask_lub
lub_indices = body_chain[3]
for n in lub_indices:
    set_elements_to_1(body_mask_lub, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_mask_lub, list(range(67 + (n - 1) * 6, 67 + n * 6)))
    set_elements_to_1(body_mask_lub, list(range(193 + n * 3, 193 + (n + 1) * 3)))

# 处理 body_mask_rub
rub_indices = body_chain[4]
for n in rub_indices:
    set_elements_to_1(body_mask_rub, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_mask_rub, list(range(67 + (n - 1) * 6, 67 + n * 6)))
    set_elements_to_1(body_mask_rub, list(range(193 + n * 3, 193 + (n + 1) * 3)))

def find_indices_of_ones(arr):
    indices = []
    for i in range(len(arr)):
        if arr[i] == 1:
            indices.append(i)
    return indices

# arr = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
# print(find_indices_of_ones(arr))
# 示例用法
# indices_of_llb = find_indices_of_ones(body_mask_llb)
# indices_of_rlb = find_indices_of_ones(body_mask_rlb)
# indices_of_troso = find_indices_of_ones(body_mask_troso)
# indices_of_lub = find_indices_of_ones(body_mask_lub)
# indices_of_rub = find_indices_of_ones(body_mask_rub)
# print("llb : ", indices_of_llb)
# print("rlb : ", indices_of_rlb)
# print("troso : ", indices_of_troso)
# print("lub : ", indices_of_lub)
# # # print("rub : ", indices_of_rub)
# print("llb : ", body_mask_llb)
# print("rlb : ", body_mask_rlb)
# print("lub : ", body_mask_lub)
# print("rub : ", body_mask_rub)
# print("torso : ", body_mask_torso)
# import torch
# batch_mask = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
# batch_mask = torch.tensor(batch_mask) 
# old_body_mask = 1 - batch_mask
# print(old_body_mask)