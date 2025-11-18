def rle_encode(instr):
    count_of_words = 0
    rude_sequaence = []
    encode_str = ""

    for i in range(1, len(instr)):
        if instr[i] == instr[i - 1]:
            count_of_words  += 1
        else:
            rude_sequaence.append(count_of_words + 1)
            rude_sequaence.append(instr[i - 1])
            count_of_words = 0

    ind_of_end = instr.find(instr[len(instr) - 1])
    rude_sequaence.append(len(instr) - ind_of_end)
    rude_sequaence.append(instr[len(instr) - 1])

    for i in range(0, len(rude_sequaence)):
        if rude_sequaence[i] == 1:
            rude_sequaence[i] = ''
        if rude_sequaence[i] == 2:
            rude_sequaence[i] = rude_sequaence[i + 1]

    for i in range(0, len(rude_sequaence)):
        encode_str += str(rude_sequaence[i])

    return encode_str
