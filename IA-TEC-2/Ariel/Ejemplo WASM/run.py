from arpeggio import NoMatch
from arpeggio.cleanpeg import ParserPEG

peg = '''
    sentence = adjective noun verb adjective noun EOF
    adjective = "big" / "small" / "red" / "green" / "blue" / "fast" / "slow"
    noun = "dog" / "cat" / "worm" / "bird" / "fish"
    verb = "runs" / "jumps" / "eats" / "sleeps" / "flies"
'''


def main():
    parser = ParserPEG(peg, 'sentence')
    try:
        tree = parser.parse('big dog runs fast cat')
        print(tree.tree_str())
    except NoMatch as e:
        print('No match:', e)


if __name__ == '__main__':
    main()
