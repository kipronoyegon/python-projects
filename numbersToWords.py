def convert_to_words(num):
    if num == 0:
        return "zero"

    ones = ["", "agenge", "oeng'", "somok", "ang'wan", "mut", "lok", "tisab", "sisit", "sogol"]
    tens = ["", "", "tiptem", "sosom", "artam", "konom", "tamonwakik lok", "tamonwakik tisab", "tamonwakik sisit", "tamonwakik sogol"]
    teens = ["taman", "taman ak agenge", "tamna ak oeng'", "taman ak somok", "tamn ak ang'wan", "taman ak mut", "taman ak lok", "taman ak tisap", "taman ak sisit", "taman ak sogol"]

    words = ""
    
    if num >= 1000:
        words += ones[num // 1000] + " eliput "
        num %= 1000

    if num >= 100:
        words +=  " pokol " + ones[num // 100] + " ak "
        num %= 100

    if num >= 10 and num <= 19:
        words += teens[num - 10] + " "
        num = 0

    elif num >= 20:
        words += tens[num // 10] + " "
        num %= 10

    if num >= 1 and num <= 9:
        words += ones[num] + " "

    return words.strip()

num = int(input("Enter a number: "))
words = convert_to_words(num)
print(words)
