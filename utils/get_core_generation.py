import ast
from utils.body_split import body_mask_all,body_mask_llb,body_mask_lub,body_mask_rlb,body_mask_rub,body_mask_torso
from utils.body_split_kit import body_kit_mask_all, body_kit_mask_llb, body_kit_mask_lub, body_kit_mask_rlb, body_kit_mask_rub, body_kit_mask_torso
import torch
import numpy as np

def get_core(motion, model_kwargs, name):
    core_body = torch.empty_like(motion)
    non_core_body = torch.empty_like(motion)
    non_core_body   
    if name == "humanml":
        # get body_parts
        body_parts = model_kwargs
        # string -> list
        body_parts_list = [part.strip("' ") for part in body_parts.strip("[]' ").split(",")]
        # creat mask_list
        mask_dict = {
            'left upper limb': body_mask_lub,
            'right upper limb': body_mask_rub,
            'left lower limb': body_mask_llb,
            'right lower limb': body_mask_rlb,
            'right lo  wer limb': body_mask_rlb,
            'torso': body_mask_torso,
            'lub': body_mask_lub,
            'rub': body_mask_rub,
            'llb': body_mask_llb,
            'rlb': body_mask_rlb,
            'tor': body_mask_torso
        }

        core_mask = np.zeros(263, dtype=int)
        for part in body_parts_list:
            core_mask += mask_dict[part]
            core_mask = np.clip(core_mask, 0, 1)

        core_mask = torch.tensor(core_mask)
        # Step 3
        core_mask = core_mask.unsqueeze(1)
        core_mask = core_mask.unsqueeze(2)
        core_mask = core_mask.expand(motion.shape[0], 263, 1, 196)

        
        motion = motion.to("cuda:0")
        core_mask = core_mask.to("cuda:0")
        non_core_mask = 1 - core_mask
        # print(expand_body_mask)
        # print(expand_body_mask.shape)
        
        core_body = core_mask * motion
        non_core_body = non_core_mask * motion    
        core_body = core_body.to("cuda:0")
        non_core_body = non_core_body.to("cuda:0")            

    if name == "kit":
        # get body_parts
        body_parts = model_kwargs
        # string -> list
        body_parts_list = [part.strip("' ") for part in body_parts.strip("[]' ").split(",")]
        # creat mask_list
        mask_dict = {
            'left upper limb': body_kit_mask_lub,
            'right upper limb': body_kit_mask_rub,
            'left lower limb': body_kit_mask_llb,
            'right lower limb': body_kit_mask_rlb,
            'right lo  wer limb': body_kit_mask_rlb,
            'torso': body_kit_mask_torso,
            'lub': body_kit_mask_lub,
            'rub': body_kit_mask_rub,
            'llb': body_kit_mask_llb,
            'rlb': body_kit_mask_rlb,
            'tor': body_kit_mask_torso
        }

        core_mask = np.zeros(251, dtype=int)
        for part in body_parts_list:
            core_mask += mask_dict[part]
            core_mask = np.clip(core_mask, 0, 1)

        core_mask = torch.tensor(core_mask)
        # Step 3
        core_mask = core_mask.unsqueeze(1)
        core_mask = core_mask.unsqueeze(2)
        core_mask = core_mask.expand(motion.shape[0], 251, 1, 196)
        
        motion = motion.to("cuda:0")
        core_mask = core_mask.to("cuda:0")
        non_core_mask = 1 - core_mask
        # print(expand_body_mask)
        # print(expand_body_mask.shape)
        
        core_body = core_mask * motion
        non_core_body = non_core_mask * motion    
        core_body = core_body.to("cuda:0")
        non_core_body = non_core_body.to("cuda:0")  
    
    return core_body, non_core_body       