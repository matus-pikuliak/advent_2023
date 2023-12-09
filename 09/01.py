
def predict(seq):

    seqs = [seq]
    while any(dif := [b - a for a, b in zip(seqs[-1], seqs[-1][1:])]):
        seqs.append(dif)
    return sum(seq[-1] for seq in seqs), sum(seq[0] for seq in seqs[::2]) - sum(seq[0] for seq in seqs[1::2])


print(
    sum(
        predict(list(map(int, line.split())))[0]
        for line in open('input')
    )
)

print(
    sum(
        predict(list(map(int, line.split())))[1]
        for line in open('input')
    )
)

