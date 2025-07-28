import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-v',  # must start with a character '-' / optional arguments start with "-"
                       '--verb',  # Name of the Attribute to Be Added to the Object Once Parsed and must start with "--"
                       metavar='VERB_LEVEL',  # defines name of flag/arguement
                       action='store',
                       type=int,
                       # nargs='+',
                       # dest="my_verb",  # overrides and re-specify the name of the arguement
                       )
my_parser.add_argument('integers',  # Positional arguments doesn't starts with "-"
                                    # if using without "-" then only flag is defined name is not defined and
                                    # this will not work "python argparse1.py   integers 99"
                       metavar='N',
                       type=float,
                       nargs='+',
                       help='an integer for the accumulator')
args = my_parser.parse_args()
print(vars(args))
print(args.verb)
# print(args.my_verb)
print(args.integers)
