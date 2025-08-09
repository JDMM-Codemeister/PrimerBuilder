"""
Primer Quality Check
"""
import re

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
        output_message += "Primer length is outside of the recommended 18-30 bp. \n"


    if is_Tm(primer):
        green_flags += 1
    else:
        output_message += "Primer melting temperature is outside of the recommended 65-75 C. \n"


    if is_GC_AT_ratio(primer):
        green_flags += 1
    else:
        output_message += "GC/AT or AT/GC ratios outside of the recommended 40/60. \n"


    if is_NT_repeats_and_runs(primer):
        green_flags += 1
    else:
        output_message += "Primer contains NT runs and/or diNT repeats. \n"


    if no_intraprimer_complementarity(primer):
        green_flags += 1
    else:
        output_message += "Potential for hairpin formation. \n"

    #get confidence score
    confidence_percentage = green_flags / total_flags * 100

    output_message += f"\nConfidence in primer: {confidence_percentage:.0f}%."

    #Check if primer i valid and overwrite message if not (Eventually Try/except user input)
    if not is_sequence_NTs(primer):
        output_message = "Not a valid sequence."


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

def is_sequence_NTs(primer: str) -> bool:
    """Return true if primer contains only DNA nucleotides"""
    for letter in primer:
        if letter not in ('A','T','G','C', 'a', 't', 'g', 'c'):
            return False

    #if good sequence
    return True

def get_Tm(primer: str) -> bool:
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

    return tm



def no_intraprimer_complementarity(primer: str) -> bool:
    """Return true if no intraprimer complementarity"""
    reverse_primer = primer[::-1]
    reverse_primer_complementary = ""

    #return false if primer too short
    if len(primer) < 3:
        return False

    #convert each base in reverse_primer to its complement
    for letter in reverse_primer:
        if letter == 'A':
            reverse_primer_complementary += 'T'
        if letter == 'T':
            reverse_primer_complementary += 'A'
        if letter == 'G':
            reverse_primer_complementary += 'C'
        if letter == 'C':
            reverse_primer_complementary += 'G'


    #check for potential hairpinning, 3x or more
    for i in range(len(primer) - 2):
        #Make sure comparison of 3+ and avoid OutOfIndexErrors
        #Compare last NT of primer with 1st complement of reversed primer
        #Check sections of 3 bp at a time while "scanning"
        if primer[len(primer) - 1 - i] == reverse_primer_complementary[i] and primer[len(primer) - 1 - (i + 1)] == reverse_primer_complementary[i + 1] and primer[len(primer) - 1 - (i + 2)] == reverse_primer_complementary[i + 2]:
            return False

    #return true if no palindomic sections
    return True

#TODO validate
def is_primer_pair_compatible(primer1: str, primer2: str) -> str:
    output_message = ""

    #Tm within 5 C of eachother?
    if abs(get_Tm(primer1) - get_Tm(primer2)) > 5:
        melting_temps_good = False
    else:
        melting_temps_good = True


    #No interprimer complimentarity
    #check which one is longer
    if len(primer1) > len(primer2):
        long = primer1
        short = primer2
    else:
        long = primer2
        short = primer1

    #complementary matches
    matches = 0

    #convert each base in reverse_primer to its complement
    short_complementary = ""

    for letter in short:
        if letter == 'A':
            short_complementary += 'T'
        if letter == 'T':
            short_complementary += 'A'
        if letter == 'G':
            short_complementary += 'C'
        if letter == 'C':
            short_complementary += 'G'

    for j in range(len(short_complementary) - 2):  # -2 because we want 3-letter chunks
        short_chunk = short_complementary[j:j + 3]

        #Scan run small primer along long and mark if codon matching (would be complementary in non-reversed primer)
        for i in range(len(long) - 2):  # -3 so slicing stays within bounds
            chunk = long[i:i + 3]

            if short_chunk == chunk:
                matches += 1

    reversed_long = long[::-1]

    # run with one reversed
    for j in range(len(short_complementary) - 2):  # -2 because we want 3-letter chunks
        short_chunk = short_complementary[j:j + 3]

        #Scan run small primer along long and mark if codon matching (would be complementary in non-reversed primer)
        for i in range(len(reversed_long) - 2):  # -3 so slicing stays within bounds
            chunk = reversed_long[i:i + 3]

            if short_chunk == chunk:
                matches += 1

    if matches >= 4:
        no_interprimer_complementary = False
    else:
        no_interprimer_complementary = True


    #result output
    if melting_temps_good and no_interprimer_complementary:
        output_message += "Primers appear compatible."
    elif melting_temps_good and not no_interprimer_complementary:
        output_message += "Primers have regions of complementarity, may form primer dimers."
    elif not melting_temps_good and no_interprimer_complementary:
        output_message += "Primer melting temperatures differ by more than 5 C."
    else:
        output_message += "Primer melting temperatures differ by more than 5 C, and potential for primer dimers."

    return output_message



def main():
    # get user primer/sequence and do check
    test = ""

if __name__ == '__main__':
    main()