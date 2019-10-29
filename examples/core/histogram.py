"""
Zemberek: Histogram Example
Original Java Example: https://bit.ly/2PmUyIV
"""

from os.path import join

from jpype import (
    JClass, JInt, JString, getDefaultJVMPath, java, shutdownJVM, startJVM)

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    Histogram: JClass = JClass('zemberek.core.collections.Histogram')

    histogram_1: Histogram = Histogram()
    histogram_1.add(
        ['apple', 'pear', 'grape', 'apple', 'apple', 'appricot', 'grape']
    )

    histogram_2: Histogram = Histogram()
    histogram_2.add(['apple', 'apple', 'banana'])

    print('Histogram 1:', histogram_1)
    print('Histogram 2:', histogram_2)

    print('\nHistogram 1, Keys:', histogram_1.getKeySet())
    print('Histogram 2, Keys:', histogram_2.getKeySet())

    print('\nHistogram 1, Sorted Keys:', histogram_1.getSortedList())
    print('Histogram 2, Sorted Keys:', histogram_2.getSortedList())

    print('\nHistogram 1, Entries:', histogram_1.getEntryList())
    print('Histogram 2, Entries:', histogram_2.getEntryList())

    print('\nHistogram 1, Sorted Entries:', histogram_1.getSortedEntryList())
    print('Histogram 2, Sorted Entries:', histogram_2.getSortedEntryList())

    print('\nHistogram 1, Total Count:', histogram_1.totalCount())
    print('Histogram 2, Total Count:', histogram_2.totalCount())

    print(
        '\nIntersection of Histogram 1 and 2:',
        histogram_1.getIntersectionOfKeys(histogram_2)
    )

    print('\nHistogram 1, Size:', histogram_1.size())
    print('Histogram 2, Size:', histogram_2.size())

    print(
        '\nHistogram 1, \'apple\' Count:',
        histogram_1.getCount(JString('apple'))
    )
    print(
        'Histogram 2, \'apple\' Count:',
        histogram_2.getCount(JString('apple'))
    )

    print(
        '\nHistogram 1, Contains \'grape\':',
        histogram_1.contains(JString('grape'))
    )
    print(
        'Histogram 2, Contains \'grape\':',
        histogram_2.contains(JString('grape'))
    )

    print('\nHistogram 1, Top 3:', histogram_1.getTop(JInt(3)))
    print('Histogram 2, Top 3:', histogram_2.getTop(JInt(3)))

    print('\nHistogram 1, Less Than 2:', histogram_1.sizeSmaller(JInt(2)))
    print('Histogram 2, Less Than 2:', histogram_2.sizeSmaller(JInt(2)))

    print('\nHistogram 1, More Than 2:', histogram_1.sizeLarger(JInt(2)))
    print('Histogram 2, More Than 2:', histogram_2.sizeLarger(JInt(2)))

    print(
        '\nHistogram 1, Between 1 and 3:',
        histogram_1.totalCount(JInt(1), JInt(3))
    )
    print(
        'Histogram 2, Between 1 and 3:',
        histogram_2.totalCount(JInt(1), JInt(3))
    )

    print('\nHistogram 1, Max Count:', histogram_1.maxValue())
    print('Histogram 2, Max Count:', histogram_2.maxValue())

    print('\nHistogram 1, Min Count:', histogram_1.minValue())
    print('Histogram 2, Min Count:', histogram_2.minValue())

    print(
        '\nHistogram 1, Equals to 2:',
        histogram_1.getItemsWithCount(JInt(2))
    )
    print(
        'Histogram 2, Equals to 2:',
        histogram_2.getItemsWithCount(JInt(2))
    )

    print(
        '\nHistogram 1, >= 2 AND <= 3:',
        histogram_1.getItemsWithCount(JInt(2)), JInt(3)
    )
    print(
        'Histogram 2, >= 2 AND <= 3:',
        histogram_2.getItemsWithCount(JInt(2), JInt(3))
    )

    print(
        '\nHistogram 1, % of >= 2 AND <= 3:',
        histogram_1.countPercent(JInt(2), JInt(3))
    )
    print(
        'Histogram 2, % of >= 2 AND <= 3:',
        histogram_2.countPercent(JInt(2), JInt(3))
    )

    print('\nHistogram 1, Sorted:', histogram_1.getSortedList())
    print('Histogram 2, Sorted:', histogram_2.getSortedList())

    print('\nHistogram 1, More Than 2:', histogram_1.sizeLarger(2))
    print('Histogram 2, More Than 2:', histogram_2.sizeLarger(2))

    print(
        '\nHistogram 1, Contains Apple:',
        histogram_1.contains(JString('apple')))
    print(
        'Histogram 2, Contains Apple:',
        histogram_2.contains(JString('apple'))
    )

    histogram_1.set(JString('apple'), 5)
    histogram_2.set(JString('apple'), 5)
    print('\nHistogram 1, Set Apple Count to 5:', histogram_1.getEntryList())
    print('Histogram 2, Set Apple Count to 5:', histogram_2.getEntryList())

    histogram_1.remove(JString('apple'))
    histogram_2.remove(JString('apple'))
    print('\nHistogram 1, Remove Apple:', histogram_1.getEntryList())
    print('Histogram 2, Remove Apple:', histogram_2.getEntryList())

    histogram_1.decrementIfPositive(JString('appricot'))
    histogram_2.decrementIfPositive(JString('appricot'))
    print(
        '\nHistogram 1, Decrease Appricot If Positive:',
        histogram_1.getEntryList()
    )
    print(
        'Histogram 2, Decrease Appricot If Positive:',
        histogram_2.getEntryList()
    )

    remove: java.util.ArrayList = java.util.ArrayList()
    remove.add(JString('grape'))
    remove.add(JString('banana'))
    histogram_1.removeAll(remove)
    histogram_2.removeAll(remove)
    print(
        '\nHistogram 1, Remove All Grape and Banana:',
        histogram_1.getEntryList()
    )
    print(
        'Histogram 2, Remove All Grape and Banana:',
        histogram_2.getEntryList()
    )

    shutdownJVM()
