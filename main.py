from groundhog import groundhog_day
from gears import gears
from asd import brackets
def main():

        data1 = ['Groundhog Festival in Punxsutawney.',
                'Groundhog Festival in Punksutawney.',
                'Groundhog Festivel in Punxsutowney.']

        data2 = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]

        line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"

        print(groundhog_day(data1))
        print(gears(data2, 30, 7))
        print(brackets(line))


if __name__ == '__main__':
    main()