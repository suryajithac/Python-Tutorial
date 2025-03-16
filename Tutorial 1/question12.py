def sum_and_avg(numbers):
    positives = [n for n in numbers if n > 0]
    negatives = [n for n in numbers if n < 0]
    return sum(negatives), sum(positives), sum(negatives)/len(negatives) if negatives else 0, sum(positives)/len(positives) if positives else 0