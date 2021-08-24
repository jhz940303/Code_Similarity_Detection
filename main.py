import math
from nltk import ngrams

if __name__ == '__main__':
    s1 = """
        Natural-language processing (NLP) is an area of
        computer science and artificial intelligence
        concerned with the interactions between computers
        and human (natural) languages.
    """

    s2 = """
            Natural-language processing (NLP) is an area of
            computer science and artificial intelligence
        """

    """Cut the file into 3 words combination using ngrams"""
    s1 = s1.lower()
    output1 = list(ngrams(s1.split(), 3))

    s2 = s2.lower()
    output2 = list(ngrams(s2.split(), 3))

    """combine two file words combination into one set"""
    word_set = set(output1).union(output2)

    """Create a words combination dictionary"""
    word_dict = dict()
    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1

    """Rewrite two file into numbers using words dictionary"""
    cut_code1 = [word_dict[word] for word in output1]
    cut_code1 = [0] * len(word_dict)

    for word in output1:
        cut_code1[word_dict[word]] += 1

    cut_code2 = [word_dict[word] for word in output2]
    cut_code2 = [0] * len(word_dict)

    for word in output2:
        cut_code2[word_dict[word]] += 1

    """Use Cosine Similarity Algorithm to calculate two files' similarity"""
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(cut_code1)):
        sum += cut_code1[i] * cut_code2[i]
        sq1 += pow(cut_code1[i], 2)
        sq2 += pow(cut_code2[i], 2)

    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0

    """Print out result as percentage"""
    percentResult = str(round(result * 100)) + '%'
    print(percentResult)
