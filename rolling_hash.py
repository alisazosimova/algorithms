def rolling_hash(pattern, text):
    alphabet = 256  # number of chars in input alphabet
    pat_len = len(pattern)
    txt_len = len(text)
    prime_n = 11  # rolling hash step
    H = 1
    pat_hash = 0 # hash value for pattern
    txt_hash = 0
    for i in range(pat_len - 1):   # The value of H would be "pow(d, M-1)%q"
        H = (H * alphabet) % prime_n
        print(f'H = {H}')
    # Calculate the hash value of pattern and first window of text
    for i in range(pat_len):
        pat_hash = (alphabet * pat_hash + ord(pattern[i])) % prime_n
        print(f'pat_hash = {pat_hash}')
        txt_hash = (alphabet * txt_hash + ord(text[i])) % prime_n
        print(f'txt_hash = {txt_hash}')
    for i in range(txt_len - pat_len + 1):
        if pat_hash == txt_hash:
            for j in range(pat_len):
                if text[i+j] != pattern[j]:
                    break
                j += 1
                if j == pat_len:
                    return True
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < txt_len - pat_len:
            txt_hash = (alphabet * (txt_hash -ord(text[i]) * H) +
                                                  ord(text[i+pat_len])) % prime_n
            # We might get negative values of text, converting it to
            # positive
            if txt_hash < 0:
                txt_hash = txt_hash + prime_n


pattern = 'dabc'
text = 'abcd'
print(rolling_hash(pattern, text))