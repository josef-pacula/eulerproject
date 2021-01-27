words_single = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
words_tens = ['','ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hudred = 'hundred'

def spell_out(num):
    if num > 1000 or num < 0:
        raise Exception('no man')
    if num == 1000:
        return 'one thousand'
    if num < 10:
        return words_single[num]
    if num < 20:
        return words_teens[num-10]
    if num < 100:
        return words_tens[int(num/10)] + (spell_out(num%10) if num%10 > 0 else '')
    return words_single[int(num/100)] + ' hundred ' + (('and ' + spell_out(num%100)) if num%100 > 0 else '')

def count(words):
    return len(words.translate(str.maketrans('', '', ' ')))

total = 0
for i in range(1,1001):
    print(spell_out(i))
    spelled = spell_out(i)
    total += count(spelled)

print(total)
