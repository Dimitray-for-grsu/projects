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

1
def search(data, input_sequence):
    input_sequence = rle_decode(input_sequence)
    for sequence in data:
        if input_sequence in sequence[2]:
            return f'organism\t\t\t\tprotein\n{sequence[1]}\t{sequence[0]}'
    return f'organism\t\t\t\tprotein\nnot found'


def diff(data, protein1, protein2):
    seq1 = seq2 = None
    for protein in data:
        if protein[0] == protein1:
            seq1 = protein[2]
        elif protein[0] == protein2:
            seq2 = protein[2]
    if seq1 is None and seq2 is None:
        return f"missing: {protein1}, {protein2}"
    elif seq1 is None:
        return f"missing: {protein1}"
    elif seq2 is None:
        return f"missing: {protein2}"
    min_length = min(len(seq1), len(seq2))
    difference = 0
    for i in range(min_length):
        if seq1[i] != seq2[i]:
            difference += 1
    difference = difference + abs(len(seq1) - len(seq2))
    return str(difference)


def mode(data, protein):
    for line in data:
        if line[0] == protein:
            sequence = line[2]
            letters = {}
            for amino_acid in sequence:
                letters[amino_acid] = letters.get(amino_acid, 0) + 1
            max_value = max(letters.values())
            answer_letter = None
            for key in sorted(letters):
                if letters[key] == max_value:
                    max_value = letters[key]
                    answer_letter = key
                    break
            return answer_letter, max_value
    return 'missing'


data1 = genetic_data('sequences.0.txt')
file = open('genedata.txt', 'w', encoding = 'utf-8')
file.write('Gerasimchik Dmitrey\n')
file.write('Genetic Searching\n')
file.write('-' * 80 + '\n')
commands_ = read_commands('commands.0.txt')
for index, command in enumerate(commands_):
    operation = command[0]
    param = command[1]
    if operation == 'search':
        result_ = search(data1, param)
        file.write(f'{index + 1:03d}   {operation}   {rle_decode(param)}\n{result_}\n')
        file.write('-' * 80 + '\n')
        index += 1
    elif operation == 'diff':
        param1 = command[2]
        result_ = diff(data1, param, param1)
        file.write(f'{index + 1:03d}   {operation}   {param}   {param1}\namino-acids difference:\n{result_}\n')
        file.write('-' * 80 + '\n')
        index += 1
    elif operation == 'mode':
        result_ = mode(data1, param)
        file.write(f'{index + 1:03d}   {operation}   {param}\namino-acid occurs:\n{result_[0]}\t\t\t{result_[1]}\n')
        file.write('-' * 80 + '\n')
        index += 1
