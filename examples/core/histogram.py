# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Histogram Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/core/HistogramExample.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Importing the required Java class
Histogram = jp.JClass('zemberek.core.collections.Histogram')

# Creating the first histogram
histogram = Histogram()
fruits = ['apple', 'pear', 'grape', 'apple', 'apple', 'appricot', 'grape']
histogram.add(fruits)

# Creating the second histogram
other_histogram = Histogram()
other_fruits = ['apple', 'apple', 'banana']
other_histogram.add(other_fruits)

# Some Histogram methods:

print('Histogram 1: %s' % histogram.map)
print('Histogram 2: %s\n' % other_histogram.map)

print('Histogram 1 Keys: %s' % ', '.join(histogram.getKeySet()))
print('Histogram 2 Keys: %s\n' % ', '.join(other_histogram.getKeySet()))

print('Histogram 1 Sorted Keys: %s' % ', '.join(histogram.getSortedList()))
print('Histogram 2 Sorted Keys: %s\n' % ', '.join(other_histogram.getSortedList()))

print('Histogram 1 Entries: %s' % histogram.getEntryList())
print('Histogram 2 Entries: %s\n' % other_histogram.getEntryList())

print('Histogram 1 Sorted Entries: %s' % histogram.getSortedEntryList())
print('Histogram 2 Sorted Entries: %s\n' % other_histogram.getSortedEntryList())

print('Histogram 1 Total Count: %d' % histogram.totalCount())
print('Histogram 2 Total Count: %d\n' % other_histogram.totalCount())

print('Intersection of Histogram 1 and 2: %s' % ', '.join(histogram.getIntersectionOfKeys(other_histogram)))

# Shutting down the JVM
jp.shutdownJVM()