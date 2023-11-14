import ast
from utils.body_split import body_mask_all,body_mask_llb,body_mask_lub,body_mask_rlb,body_mask_rub,body_mask_torso
from utils.body_split_kit import body_kit_mask_all, body_kit_mask_llb, body_kit_mask_lub, body_kit_mask_rlb, body_kit_mask_rub, body_kit_mask_torso
import torch
import numpy as np

def get_core(motion, model_kwargs, name):
    if name == "humanml":
        # get body_parts
        body_parts = model_kwargs['y']['body_parts']
        # string -> list
        body_parts_list = [ast.literal_eval(bp) for bp in body_parts]
        # creat mask_list
        mask_dict = {
            'left upper limb': body_mask_lub,
            'right upper limb': body_mask_rub,
            'left lower limb': body_mask_llb,
            'right lower limb': body_mask_rlb,
            'right lo  wer limb': body_mask_rlb,
            'torso': body_mask_torso,
        }

        batch_mask_list = []
        for parts in body_parts_list:
            combined_mask = np.zeros(263, dtype=int)
            for part in parts:
                combined_mask += mask_dict[part]                   
            combined_mask = np.clip(combined_mask, 0, 1)             
            batch_mask_list.append(combined_mask.tolist())
        
        # print(body_parts_list)
        # print(batch_mask_list)
        batch_mask = torch.tensor(batch_mask_list)
        # (64, 263) -> (64, 263, 1, 1)
        expand_body_mask = batch_mask.unsqueeze(dim = 2).unsqueeze(dim = 3)
        motion = motion.to("cuda:0")
        expand_body_mask = expand_body_mask.to("cuda:0")
        old_body_mask = 1 - expand_body_mask
        # print(expand_body_mask)
        # print(expand_body_mask.shape)
        
        core_body = expand_body_mask * motion
        non_core_body = old_body_mask * motion    
        core_body = core_body.to("cuda:0")
        non_core_body = non_core_body.to("cuda:0")            

    if name == "kit":
        # get body_parts
        body_parts = model_kwargs['y']['body_parts']
        # string -> list
        body_parts_list = [ast.literal_eval(bp) for bp in body_parts]
        # creat mask_list
        mask_dict = {
            'left upper limb': body_kit_mask_lub,
            'right upper limb': body_kit_mask_rub,
            'left lower limb': body_kit_mask_llb,
            'right lower limb': body_kit_mask_rlb,
            'right lo  wer limb': body_kit_mask_rlb,
            'torso': body_kit_mask_torso,
        }

        batch_mask_list = []
        for parts in body_parts_list:
            combined_mask = np.zeros(251, dtype=int)
            for part in parts:
                combined_mask += mask_dict[part]                   
            combined_mask = np.clip(combined_mask, 0, 1)             
            batch_mask_list.append(combined_mask.tolist())
        
        # print(body_parts_list)
        # print(batch_mask_list)
        batch_mask = torch.tensor(batch_mask_list)
        # (64, 263) -> (64, 263, 1, 1)
        expand_body_mask = batch_mask.unsqueeze(dim = 2).unsqueeze(dim = 3)
        motion = motion.to("cuda:0")
        expand_body_mask = expand_body_mask.to("cuda:0")
        old_body_mask = 1 - expand_body_mask
        # print(expand_body_mask)
        # print(expand_body_mask.shape)
        
        core_body = expand_body_mask * motion
        non_core_body = old_body_mask * motion    
        core_body = core_body.to("cuda:0")
        non_core_body = non_core_body.to("cuda:0")  
    
    return core_body, non_core_body       