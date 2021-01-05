import string


def rot13(message):

    new_massage = []
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)

    for el in message:

        if el in alphabet_lower:
            count = 0

            while el != alphabet_lower[count]:
                count += 1

            if count + 13 < len(alphabet_lower):
                count += 13
                i = alphabet_lower[count]
                new_massage.append(i)

            else:
                count += 13
                count = count - len(alphabet_lower)
                i = alphabet_lower[count]
                new_massage.append(i)

        elif el in alphabet_upper:
            count = 0

            while el != alphabet_upper[count]:
                count += 1

            if count + 13 < len(alphabet_upper):
                count += 13
                i = alphabet_upper[count]
                new_massage.append(i)

            else:
                count += 13
                count = count - len(alphabet_upper)
                i = alphabet_upper[count]
                new_massage.append(i)

        else:
            new_massage.append(el)

    caesar = ''.join(new_massage)

    return caesar


a = 'Test'

rot13(a)