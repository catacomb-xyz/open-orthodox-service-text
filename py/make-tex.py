#!/bin/env python3

import sys

out_dir = "/home/anon/Git/open-orthodox-service-text/.tmp"

if __name__ == '__main__':
  for txt in sys.argv:
    if -1 == txt.find(".txt"):
      continue

    name = txt[:txt.find(".")]
    print(txt, txt[:txt.find(".")])
    name = name + ".tex"
    name = out_dir + "/" + name
    print(name)

    fout = open(name, "w")

    # n = 0
    # for line in open(txt):
      # n = n + 1
      # vnum = str(n) + " "
      # fout.write(vnum + line)

    fout.close()
