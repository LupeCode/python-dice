import re
import dice
from argparse import ArgumentParser

parser = ArgumentParser(description='Roll some dice.')
parser.add_argument('dice', help='The dice roll string, e.g. 2d6 or 1d20+2')
parser.add_argument('-H', '--high', action='store_true', help='Sets the dice to be weighted to roll bigger numbers')
parser.add_argument('-L', '--low', action='store_true', help='Sets the dice to be weighted to roll smaller numbers')
parser.add_argument('-F', '--factor', default=2.0, help='Sets the factor of the weighted dice, from 0.0 to 10.0')

args = parser.parse_args()
pattern = re.compile('^(\d+)d(\d+)([-+])?(\d+)?$', re.IGNORECASE)
matches = pattern.match(args.dice)
if matches:
    groups = matches.groups()
    if args.high:
        total = dice.roll_high(int(groups[0]), int(groups[1]), float(args.factor))
        fairness = '(The dice are weighted high)'
    elif args.low:
        total = dice.roll_low(int(groups[0]), int(groups[1]), float(args.factor))
        fairness = '(The dice are weighted low)'
    else:
        total = dice.roll_dice(int(groups[0]), int(groups[1]))
        fairness = '(The dice are fair)'

    if groups[2] is None:
        print('Rolled', total, 'for a total of', sum(total), fairness)
    else:
        if groups[2] == '-':
            modifier = int(groups[3]) * -1
            print('Rolled', total, 'minus', groups[3], 'for a total of', sum(total) + modifier, fairness)
        else:
            modifier = int(groups[3])
            print('Rolled', total, 'plus', groups[3], 'for a total of', sum(total) + modifier, fairness)
else:
    print('No dice string found.')
