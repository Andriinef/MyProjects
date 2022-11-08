"""  Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
    and carries the "instructions" for the development and functioning
    of living organisms.
"""
from codewars_test import assert_equals


def DNA_strand(dna):
    dna_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    # result = []
    # for i in dna:
    #     new_i = dna_dict[i]
    #     result.append(new_i)
    # return ''.join(result)

    return "".join([dna_dict[i] for i in dna])
    # return ''.join([{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[letter] for letter in dna])


test0 = assert_equals(DNA_strand("AAAA"), "TTTT", "String AAAA is")
test1 = assert_equals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
test2 = assert_equals(DNA_strand("GTAT"), "CATA", "String GTAT is")
