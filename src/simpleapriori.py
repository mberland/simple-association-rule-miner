import sys,csv,operator
from collections import Counter,defaultdict

all_counts = defaultdict(Counter)
all_support = defaultdict(float)
all_lift = defaultdict(float)
number_of_rows = 0

def find_ngrams(input_list,n):
    return zip(*[input_list[i:] for i in range(n)])

K_MAX = 7
def apriori_sub(transactions,candidates,k,min_lift,min_support):
    valid_candidates = False
    number_of_rows = len(transactions)
    if k > (2 + number_of_rows):
        print "not enough data!!"
        return []
    if k > K_MAX:
        print "greater than",K_MAX,"not yet implemented!"
        return []
    result = []
    all_ngrams = []
    print 'candidates[' + str(len(candidates)) + '], k =', str(k)
    for row in transactions:
        all_ngrams.extend(find_ngrams(row,k))
    all_counts[k].update(all_ngrams)
    total_for_k = sum(all_counts[k].values())
    print 'all',k,'tuples:',total_for_k
    for ngram in all_counts[k]:
        # this isnt support, exactly, but it is equivalent for no-repeats-per-line
        all_support[ngram] = all_counts[k][ngram] / (1.0 * number_of_rows)
    for ngram in all_counts[k]: # needs to be after support is fully calculated
        if (k > 1):
            all_lift[ngram] = all_support[ngram] / (all_support[ngram[-1:]] * all_support[ngram[:-1]])
            if (all_lift[ngram] > min_lift and all_support[ngram] > min_support):
                print "%1.2f"%all_lift[ngram],"%1.2f"%all_support[ngram],'=',ngram, ngram[-1:], 
                print all_support[ngram[-1:]], ngram[:-1], all_support[ngram[:-1]]
                valid_candidates = True
        else:
            valid_candidates = True
    if valid_candidates:
        return apriori_sub(transactions,candidates,k+1,min_lift,min_support)    
    elif k < 3:
        print "NO VALID CANDIDATES AT ALL"
    return []


def apriori(transactions,min_lift,min_support):
    number_of_rows = len(transactions)
    candidates = set()
    for row in transactions:
        for item in row:
            candidates.add(item)
    print 'initial candidates = ',candidates
    apriori_sub(transactions,candidates,1,min_lift,min_support)
    
if len(sys.argv) < 2:
    print "no input file! gimme a csv."
else:
    infilename = sys.argv[1]
    try:
        min_support = float(sys.argv[2])
        min_lift = float(sys.argv[3])
    except:
        print 'min_support/min_lift unspecified! using defaults!'
        min_support = 0.03
        min_lift = 1.0
    print 'min_support = %1.2f, min_lift = %1.2f' % (min_support,min_lift)
    print 'filename =',infilename
    data = [row for row in csv.reader(open(infilename,'r'))]
    apriori(data,min_lift,min_support)
        