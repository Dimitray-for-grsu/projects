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

def rle_decode(code_str):
    decoded = ""
    i = 0
    while i < len(code_str):
        if code_str[i].isdigit():
            count = int(code_str[i])
            char = code_str[i + 1]
            decoded += char * count
            i += 2
        else:
            decoded += code_str[i]
            i += 1
    return decoded


def genetic_data(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for item in f:
            parts = item.strip().split('\t')
            protein_data = (
                parts[0].strip(),
                parts[1].strip(),
                rle_decode(parts[2].strip())
            )
            data.append(protein_data)
        return data


def read_commands(filename):
    commands = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if parts[0] == 'search' or parts[0] == 'mode':
                command_data = (
                    parts[0].strip(),
                    parts[1].strip()
                )
            else:
                command_data = (
                    parts[0].strip(),
                    parts[1].strip(),
                    parts[2].strip()
                )
            commands.append(command_data)
        return commands




print(rle_encode("AAAADDSAAADW"))
#print(rle_decode((rle_encode("AAAADDSAAADWW"))))
