'''Streaming pickle implementation for efficiently serializing and
de-serializing an iterable (e.g., list)

Created on 2010-06-19 by Philip Guo

Limitations:

  - Only works with ASCII-based pickles (protocol=0), since s_load reads
  in one line at a time

'''

from pickle import dumps, loads, HIGHEST_PROTOCOL


def s_dump(iterable_to_pickle, file_obj):
  '''dump contents of an iterable iterable_to_pickle to file_obj, a file
  opened in write mode'''
  for elt in iterable_to_pickle:
    s_dump_elt(elt, file_obj)


def s_dump_elt(to_pickle, file_obj):
  '''dumps one element to file_obj, a file opened in write mode'''
  pickled_elt_str = dumps((to_pickle[0].encode('unicode-escape'), to_pickle[1].encode('unicode-escape')), protocol=HIGHEST_PROTOCOL)
  file_obj.write(pickled_elt_str)
  # record separator is a blank line
  # (since pickled_elt_str might contain its own newlines)
  file_obj.write(b'\n * - * \n')


def s_load(file_obj):
  '''load contents from file_obj, returning a generator that yields one
  element at a time'''
  file_obj.seek(0)
  cur_elt = []
  for line in file_obj:
    if line == b' * - * \n':
      pickled_elt_str = b''.join(cur_elt)
      elt = loads(pickled_elt_str)
      cur_elt = []
      yield (elt[0].decode('unicode-escape'), elt[1].decode('unicode-escape'))
      continue
    cur_elt.append(line)
