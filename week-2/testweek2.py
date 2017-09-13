#Functions during week 2

#Strings
string = "The top 2 is {0} and {1}".format(winner, runner_up, format_spec='{1}')
open_string = "Sammy loves {}."
print(open_string.format("open source"))
string[7:10]
self.assertEqual(97, ord('a')) #Transform to ASCII code
string = "Sausage Egg Cheese"
words = string.split()

string = "the,rain;in,spain"
pattern = re.compile(',|;')
words = pattern.split(string)

words = ["Now", "is", "the", "time"]
self.assertEqual("Now is the time", ' '.join(words))

self.assertEqual('Guido', 'guido'.capitalize())
self.assertEqual('GUIDO', 'guido'.upper())
self.assertEqual('timbot', 'TimBot'.lower())
self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())

True
False

if:
else:
elif:
==
!=
while
break
continue
in

iter()
next()


winner = 65
runner_up = 58

print(string)