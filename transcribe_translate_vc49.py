
# coding: utf-8
import seq_tools_vc49 as vc
##############################################for "one_nt_seqs.fa" file ############
f_one=vc.load_fasta("one_nt_seq.fa")
print(vc.get_reverse_complement(f_one))
print(vc.get_transcript(f_one))
print(vc.get_translate(f_one,True))
print(vc.get_translate(f_one,False))
############################################################## for "multiple_nt_seqs.fa"##################
f_multiple=vc.load_fasta("multiple_nt_seqs.fa")
print(f_multiple)
type(f_multiple)
print(vc.get_reverse_complement(f_multiple))
print(vc.get_transcript(f_multiple))
print(vc.get_translate(f_multiple,True))
print(vc.get_translate(f_multiple,False))
