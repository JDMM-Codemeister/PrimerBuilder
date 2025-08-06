"""
Primer Quality Check
"""
import re

def main();
    #get user primer/sequence and do check
    #TODO main code








def check_primer_quality(primer: str) -> str:
    #Check primer quality and report to user
    #Report a % confidence and warning messages
    mutagenic_primer = False
    green_flags = 0
    total_flags = 9
    output_message = ""

    if is_GC_clamp(primer):
        green_flags += 1
    else:
        output_message += "No GC clamp on 3' end of primer. \n"


    if is_GC_content_modest(primer):
        green_flags += 1
    else:
        output_message += "GC content not within 40-60% sweet spot. \n"


    if are_GC_repeats_good(primer):
        green_flags += 1
    else:
        output_message += "More than 5 GC repeats. \n"


    if is_primer_length(primer):
        green_flags += 1
    else:
        output_message += "Primer length is outside of the recommended 18-30. \n"


    if is_Tm(primer):
        green_flags += 1
    else:
        output_message += "Primer melting temperature is outside of the recommended 65-75 C. \n"


    if is_GC_AT_ratio(primer):
        green_flags += 1
    else:
        output_message += "GC/AT ratios outside of the recommended 60/40. \n"


    if is_NT_repeats_and_runs(primer):
        green_flags += 1
    else:
        output_message += "Primer contains NT runs and/or diNT repeats. \n"


    if no_intraprimer_complementarity(primer):
        green_flags += 1
    else:
        output_message += "Potential for hairpin formation. \n"



    return output_message


def is_GC_clamp(primer: str) -> bool:
    """Returns true is primer 3' end with G or C. Must enter primer 5' to 3'"""
    if primer[-1] == 'C' or primer[-1] == 'G':
        return True
    else:
        return False

def is_GC_content_modest(primer: str) -> bool:
    """Return true if G/C content is between 40-60% of primer"""
    gc_count = 0

    #Count each G or C
    for letter in primer:
        if letter == 'G' or letter == 'C':
            gc_count += 1

    #Get GC percentage
    if gc_count/len(primer) < 0.4 or gc_count/len(primer) > 0.6:
        return False
    else:
        return True


def are_GC_repeats_good(primer: str) -> bool:
    """Return true if less than 5 GC repeats"""
    repeats = 0

    #loop through primer and count repeats
    for i in range(len(primer) - 1):
        if primer[i] in ('G', 'C') and primer[i + 1] in ('C', 'G'):
            repeats += 1

    if repeats <= 5:
        return True
    else:
        return False



def is_primer_length(primer: str) -> bool:
    """Return true if length of primer is 18-30"""
    if len(primer) >= 18 and len(primer) <= 30:
        return True
    else:
        return False


def is_Tm(primer: str) -> bool:
    """Return true if Tm is between 65-75 C?. Using Wallace rule: Tm = 2°C (A+T) + 4°C (G+C)."""
    at_count = 0
    gc_count = 0
    tm = 0

    for letter in primer:
        if letter in ('A','T'):
            at_count += 1
        if letter in ('G','C'):
            gc_count += 1

    tm = 2*at_count + 4*gc_count

    if tm >= 65 and tm <= 75:
        return True
    else:
        return False


def is_GC_AT_ratio(primer: str) -> bool:
    """Return true if ratio of A/T and G/C bps within 20%?"""
    at_count = 0
    gc_count = 0

    for letter in primer:
        if letter in ('A','T'):
            at_count += 1
        if letter in ('G','C'):
            gc_count += 1

    #Check ratio
    if at_count/len(primer) < 0.40 or gc_count/len(primer) > 0.65:
        return False
    else:
        return True


def is_NT_repeats_and_runs(primer: str) -> bool:
    """Return true if no runs of NT repeats (< 4x) or runs of diNTs? (< 4x)"""
    #Check NT runs
    if bool(re.search(r'(A{4,}|T{4,}|C{4,}|G{4,})', primer)):
        return False

    #Check diNT runs
    if bool(re.search(r'((AT){4,}|(TA){4,}|(GC){4,}|(CG){4,})', primer)):
        return False

    return True

#TODO need to update this to check the complement with rev primer
def no_intraprimer_complementarity(primer: str) -> bool:
    """Return true if no intraprimer complementarity"""
    reverse_primer = primer[::-1]

    repeat_count = 0

    #check for potential hairpinning, 3x or more
    for i in range(len(primer) -2):
        #Make sure comparison of 3+ and avoid OutOfIndexErrors
        if i >= 3:
         if primer[len(primer) - 1 - i] == reverse_primer[i] and primer[len(primer) - 1 - (i + 1)] == reverse_primer[i + 1] and primer[len(primer) - 1 - (i + 2)] == reverse_primer[i + 2]:
                return False

    #return true if no palindomic sections
    return True

#TODO compare 2 primers
def is_primer_pair_compatible() -> bool:
    #Tm within 5 C of eachother?

    #No interprimer complimentarity




if __name__ == '__main__':
    main()