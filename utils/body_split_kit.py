body_kit_parts_all = ['left lower limb', 'right lower limb', 'torso', 'left upper limb', 'right upper limb']


body_kit_chain = [[0, 11, 12, 13, 14, 15],  # llb
              [0, 16, 17, 18, 19, 20],  # rlb
              [0, 1, 2, 3, 4],  # troso
              [3, 8, 9, 10],  # lub
              [3, 5, 6, 7]]  # rub

body_kit_mask_llb = [0] * 251
body_kit_mask_rlb = [0] * 251
body_kit_mask_torso = [0] * 251
body_kit_mask_lub = [0] * 251
body_kit_mask_rub = [0] * 251
body_kit_mask_all = [0] * 251

def set_elements_to_1(mask, indices):
    for index in indices:
        mask[index] = 1

# root
set_elements_to_1(body_kit_mask_llb, list(range(0, 4)))
set_elements_to_1(body_kit_mask_rlb, list(range(0, 4)))
set_elements_to_1(body_kit_mask_torso, list(range(0, 4)))

# foot 
set_elements_to_1(body_kit_mask_llb, list(range(247, 251)))
set_elements_to_1(body_kit_mask_rlb, list(range(247, 251)))
    

# 处理 body_mask_llb
llb_indices = body_kit_chain[0]
for n in llb_indices:
    set_elements_to_1(body_kit_mask_llb, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_kit_mask_llb, list(range(64 + (n - 1) * 6, 64 + n * 6)))
    set_elements_to_1(body_kit_mask_llb, list(range(184 + n * 3, 184 + (n + 1) * 3)))

# 处理 body_mask_rlb
rlb_indices = body_kit_chain[1]
for n in rlb_indices:
    set_elements_to_1(body_kit_mask_rlb, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_kit_mask_rlb, list(range(64 + (n - 1) * 6, 64 + n * 6)))
    set_elements_to_1(body_kit_mask_rlb, list(range(184 + n * 3, 184 + (n + 1) * 3)))

# 处理 body_mask_troso
troso_indices = body_kit_chain[2]
for n in troso_indices:
    set_elements_to_1(body_kit_mask_torso, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_kit_mask_torso, list(range(64 + (n - 1) * 6, 64 + n * 6)))
    set_elements_to_1(body_kit_mask_torso, list(range(184 + n * 3, 184 + (n + 1) * 3)))

# 处理 body_mask_lub
lub_indices = body_kit_chain[3]
for n in lub_indices:
    set_elements_to_1(body_kit_mask_lub, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_kit_mask_lub, list(range(64 + (n - 1) * 6, 64 + n * 6)))
    set_elements_to_1(body_kit_mask_lub, list(range(184 + n * 3, 184 + (n + 1) * 3)))

# 处理 body_mask_rub
rub_indices = body_kit_chain[4]
for n in rub_indices:
    set_elements_to_1(body_kit_mask_rub, list(range(4 + (n - 1) * 3, 4 + n * 3)))
    set_elements_to_1(body_kit_mask_rub, list(range(64 + (n - 1) * 6, 64 + n * 6)))
    set_elements_to_1(body_kit_mask_rub, list(range(184 + n * 3, 184 + (n + 1) * 3)))

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