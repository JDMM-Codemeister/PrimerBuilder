
def main();


def check_primer_quality(primer: primer) -> str:
    #Check primer quality and report to user
    #Report a % confidence and warning messages
    mutagenic_primer = False
    green_flags = 0
    total_flags = 9

    if(is_GC_clamp(primer)):
        green_flags += 1
    else:
        #print warning


    if(is_GC_content(primer)):
        green_flags += 1
    else:
        #print warning


    if(is_GC_repeats(primer)):
        green_flags += 1
    else:
        #print warning

    if(is_primer_length(primer)):
        green_flags += 1
    else:
        #print warning

    if(is_Tm(primer)):
        green_flags += 1
    else:
        #print warning

    if(is_5Prime_overhang(primer)):
        green_flags += 1
    else:
        #print warning

    if(is_GC_AT_ratio(primer)):
        green_flags += 1
    else:
        #print warning

    if(is_NT_repeats_and_runs(primer)):
        green_flags += 1
    else:
        #print warning

    if(is_intraprimer_complementarity(primer)):
        green_flags += 1
    else:
        #print warning

    if(is_mismatched_middle(primer)):
        mutagenic_primer = True
    else:
        #print warning


def is_GC_clamp(primer: sequence) -> bool:
    #is there one on 3'

def is_GC_content(primer: sequence) -> bool:
    #GC content 40-60%?

def is_GC_repeats(primer: sequence) -> bool:
    #few G/C repeats (< 3)

def is_primer_length(primer: sequence) -> bool:
    #length of primer 18-30 perfect, <12 terrible, 12-17 bad, 31-40 bad, >40 risky

def is_Tm(primer: sequence) -> bool:
    #Tm between 65-75 C?

def is_5Prime_overhang(primer: sequence) -> bool:
    #Are there 3-6 extra bp on the 5' end for restriction enzymes?

def is_GC_AT_ratio(primer: sequence) -> bool:
    #Ratio of A/T and G/C bps within 20%?

def is_NT_repeats_and_runs(primer: sequence) -> bool:
    #No runs of NT repeats or runs of diNTs? (GAAAA or ATATATAT)

def is_intraprimer_complementarity(primer: sequence) -> bool:
    #no intraprimer complementarity

def is_mismatched_middle(primer: sequence) -> bool:
    #mismatched primer in middle of primer only ? (for mutagenesis)



def is_primer_pair_compatible() -> bool:
    #Tm within 5 C of eachother?

    #No interprimer complimentarity






if __name__ == '__main__':
    main()