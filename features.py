#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:09:57 2021

@author: shuizeren
"""

# allowable multiple choice node and edge features 
allowable_features = {
    'possible_atomic_num_list' : (list(range(1, 119)) + ['misc'], 0),
    'possible_chirality_list' : ([
        'CHI_UNSPECIFIED',
        'CHI_TETRAHEDRAL_CW',
        'CHI_TETRAHEDRAL_CCW',
        'CHI_OTHER'
    ], 119),
    'possible_degree_list' : ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'misc'], 123),
    'possible_formal_charge_list' : ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 'misc'], 135),
    'possible_numH_list' : ([0, 1, 2, 3, 4, 5, 6, 7, 8, 'misc'], 147),
    'possible_number_radical_e_list': ([0, 1, 2, 3, 4, 'misc'], 157),
    'possible_hybridization_list' : ([
        'SP', 'SP2', 'SP3', 'SP3D', 'SP3D2', 'misc'
        ], 163),
    'possible_is_aromatic_list': ([False, True], 169),
    'possible_is_in_ring_list': ([False, True], 171),
    'possible_bond_type_list' : ([
        'SINGLE',
        'DOUBLE',
        'TRIPLE',
        'AROMATIC',
        'misc'
    ], 173),
    'possible_bond_stereo_list': ([
        'STEREONONE',
        'STEREOZ',
        'STEREOE',
        'STEREOCIS',
        'STEREOTRANS',
        'STEREOANY',
    ], 178), 
    'possible_is_conjugated_list': ([False, True], 184),
}

def safe_index(l, e):
    """
    Return index of element e in list l. If e is not present, return the last index
    """
    try:
        return l[0].index(e) + l[1]
    except:
        return len(l[0]) - 1 + l[1]
# # miscellaneous case
# i = safe_index(allowable_features['possible_atomic_num_list'], 'asdf')
# assert allowable_features['possible_atomic_num_list'][i] == 'misc'
# # normal case
# i = safe_index(allowable_features['possible_atomic_num_list'], 2)
# assert allowable_features['possible_atomic_num_list'][i] == 2

def atom_to_feature_vector(atom):
    """
    Converts rdkit atom object to feature list of indices
    :param mol: rdkit atom object
    :return: list
    """
    atom_feature = [
            safe_index(allowable_features['possible_atomic_num_list'], atom.GetAtomicNum()),
            safe_index(allowable_features['possible_chirality_list'], str(atom.GetChiralTag())),
            safe_index(allowable_features['possible_degree_list'], atom.GetTotalDegree()),
            safe_index(allowable_features['possible_formal_charge_list'], atom.GetFormalCharge()),
            safe_index(allowable_features['possible_numH_list'], atom.GetTotalNumHs()),
            safe_index(allowable_features['possible_number_radical_e_list'], atom.GetNumRadicalElectrons()),
            safe_index(allowable_features['possible_hybridization_list'], str(atom.GetHybridization())),
            safe_index(allowable_features['possible_is_aromatic_list'], atom.GetIsAromatic()),
            safe_index(allowable_features['possible_is_in_ring_list'], atom.IsInRing()),
            ]
    return atom_feature
# from rdkit import Chem
# mol = Chem.MolFromSmiles('Cl[C@H](/C=C/C)Br')
# atom = mol.GetAtomWithIdx(1)  # chiral carbon
# atom_feature = atom_to_feature_vector(atom)
# assert atom_feature == [5, 2, 4, 5, 1, 0, 2, 0, 0]

def bond_to_feature_vector(bond):
    """
    Converts rdkit bond object to feature list of indices
    :param mol: rdkit bond object
    :return: list
    """
    bond_feature = [
                safe_index(allowable_features['possible_bond_type_list'], str(bond.GetBondType())),
                safe_index(allowable_features['possible_bond_stereo_list'], str(bond.GetStereo())),
                safe_index(allowable_features['possible_is_conjugated_list'], bond.GetIsConjugated()),
            ]
    return bond_feature
# uses same molecule as atom_to_feature_vector test
# bond = mol.GetBondWithIdx(2)  # double bond with stereochem
# bond_feature = bond_to_feature_vector(bond)
# assert bond_feature == [1, 2, 0]