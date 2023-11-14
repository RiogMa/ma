import numpy as np
import pickle
from os.path import join as pjoin

POS_enumerator = {
    'VERB': 0,
    'NOUN': 1,
    'DET': 2,
    'ADP': 3,
    'NUM': 4,
    'AUX': 5,
    'PRON': 6,
    'ADJ': 7,
    'ADV': 8,
    'Loc_VIP': 9,
    'Body_VIP': 10,
    'Obj_VIP': 11,
    'Act_VIP': 12,
    'Desc_VIP': 13,
    'OTHER': 14,
}

Loc_list = ('left', 'right', 'clockwise', 'counterclockwise', 'anticlockwise', 'forward', 'back', 'backward',
            'up', 'down', 'straight', 'curve','reverse','diagonal','upleft','bottom','semicircle')

Body_list = ('arm', 'chin', 'foot', 'feet', 'face', 'hand', 'mouth', 'leg', 'waist', 'eye', 'knee', 'shoulder', 'thigh', 'head',
             'chest', 'toe', 'tiptoe', 'torso','hip','elbow','wrist','forearm','stomach','neck','finger','eye')

Obj_List = ('stair', 'dumbbell', 'chair', 'window', 'floor', 'car', 'ball', 'handrail', 'baseball', 'basketball','phone',
            'table','rope','rail','cartwheel','golf','wall','box','treadmill','chicken','wheel','screen','handrail','camera','violin',
            'door','shoe','plane','dog','seat','obstacle','cup','stool','football','monkey','window','bird')

Act_list = ('walk', 'run', 'swing', 'pick', 'bring', 'kick', 'put', 'squat', 'throw', 'hop', 'dance', 'jump', 'turn',
            'stumble', 'dance', 'stop', 'sit', 'lift', 'lower', 'raise', 'wash', 'stand', 'kneel', 'stroll',
            'rub', 'bend', 'balance', 'flap', 'jog', 'shuffle', 'lean', 'rotate', 'spin', 'spread', 'climb', 'move',
            'take', 'step', 'hold', 'make', 'wave', 'use', 'start', 'stop', 'look', 'do', 'jog', 'stretch', 'get', 'reach',
            'appear','go', 'push', 'swinge', 'grab', 'cross', 'return', 'shake', 'extend', 'touch', 'crawl', 'drop', 'clap',
            'sway', 'come', 'crouch', 'play', 'catch', 'set', 'keep','punch','scratch','drink','fall','pull','wipe','open',
            'outstretche','twist','hit','act','sidestep','gesture','bounce','shift','rest','slide','check',
            'bow','stay','eat','lay','tilt','skip','point','follow','pretend','clean','roll','swim','drag','lunge','hang',
            'dodge','stir','avoid','lead','pause','wiggle','limp','exercise','lose','talk','march','give','stagger','practice',
            'flex','carry','trip','fight','show','toss','tap','mix','sprint','switch','straighten','strum','support','adjust',
            'wait','prepare','prepare','see','stomp','wind','have','pat','work','drive','rise','change','press','sneak','leap',
            'wobble','shoot','swat','hurt','circle','knock','struggle','shrug','draw','slap','releasec','dig','twirl','pump',
            'veer','thrust','uncross','creep','close','brace','swipe','swivel','write','salute','stride','strafe','plant','loosen',
            'saunter','answer','jerk','stoop','cut','shout','unscrew','shove','laugh','jab','transfer','watch','waltz','pray',
            'gain','slouch','stare','fly','cry','reel','speak','stroke','receive','stroll','grip','twitch','bob','swe','wrap','bump',
            'hug') 

Desc_list = ('slowly', 'carefully', 'fast', 'careful', 'slow', 'quickly', 'happy', 'angry', 'sad', 'happily',
             'angrily', 'sadly', 'slightly', 'very', 'repeatedly', 'casually', 'briskly', 'lightly', 'suddenly', 'briefly', 'directly', 
             'loosely', 'rapidly', 'confidently', 'cautiously', 'completely', 'horizontally', 'calmly', 'well', 'aggressively', 'vertically', 
             'abruptly', 'steadily', 'fastly', 'randomly', 'vigorously','unsteadily','awkwardly','angrily','possibly','nearly')

VIP_dict = {
    'Loc_VIP': Loc_list,
    'Body_VIP': Body_list,
    'Obj_VIP': Obj_List,
    'Act_VIP': Act_list,
    'Desc_VIP': Desc_list,
}


class WordVectorizer(object):
    def __init__(self, meta_root, prefix):
        vectors = np.load(pjoin(meta_root, '%s_data.npy'%prefix))
        words = pickle.load(open(pjoin(meta_root, '%s_words.pkl'%prefix), 'rb'))
        word2idx = pickle.load(open(pjoin(meta_root, '%s_idx.pkl'%prefix), 'rb'))
        self.word2vec = {w: vectors[word2idx[w]] for w in words}

    def _get_pos_ohot(self, pos):
        pos_vec = np.zeros(len(POS_enumerator))
        if pos in POS_enumerator:
            pos_vec[POS_enumerator[pos]] = 1
        else:
            pos_vec[POS_enumerator['OTHER']] = 1
        return pos_vec

    def __len__(self):
        return len(self.word2vec)

    def __getitem__(self, item):
        word, pos = item.split('/')
        if word in self.word2vec:
            word_vec = self.word2vec[word]
            vip_pos = None
            for key, values in VIP_dict.items():
                if word in values:
                    vip_pos = key
                    break
            if vip_pos is not None:
                pos_vec = self._get_pos_ohot(vip_pos)
            else:
                pos_vec = self._get_pos_ohot(pos)
        else:
            word_vec = self.word2vec['unk']
            pos_vec = self._get_pos_ohot('OTHER')
        return word_vec, pos_vec