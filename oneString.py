def compactTxt(txtName):
    with open(txtName, 'r') as f:
        lines = f.readlines()

    # Group the lines into pairs
    pairs = zip(lines[::2], lines[1::2])

    # Build up a string with the desired prefixes and newline characters
    result = ''
    for a, b in pairs:
        result += f'Q: {a.strip()}\n'
        result += f'A: {b.strip()}\n'

    # Print the resulting string without quotes
    return(result)

def save(i, o, txtName):
    f = open(txtName, "a")
    try:
      f.write(i+"\n")
      f.write(o+"\n")
    finally:f.close();

    # list to store file lines
    lines = []
    # read file
    with open(txtName, 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()

    # Write file
    with open(txtName, 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            # delete line 1 and 2. or pass any Nth line you want to remove
            # note list index starts from 0
            if number not in [0, 1]:
                fp.write(line)
