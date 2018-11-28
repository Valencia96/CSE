word_list = []

word_list.append(input("Type in a noun:"))
word_list.append(input("Type in an adjective ending in -ic:"))
word_list.append(input("Type in another noun:"))
word_list.append(input("Type in another noun:"))
word_list.append(input("Type in a verb ending in -ing:"))
word_list.append(input("Type in another noun:"))
word_list.append(input("Type in an onomatopoeia:"))
word_list.append(input("Type in another noun:"))
word_list.append(input("Type in another onomatopoeia:"))
word_list.append(input("Type in the final noun:"))

print("The %s™ Pacer Test is a multi-stage %s capacity "
      "test that progressively gets more difficult as it continues." % (word_list[0], word_list[1]))
print()
print("The 20-%s Pacer test will begin in 30 %s. Line up at the start. " % (word_list[2], word_list[3]))
print("The %s speed starts slowly, but gets faster every %s after you hear this signal: *%s*" %
      (word_list[4], word_list[5],
       word_list[6]))
print()
print("A single %s should be completed every time you hear this sound: *%s*" % (word_list[7], word_list[8]))
print()
print("The second time you fail to complete a lap, your test is over. ")
print()
print("The test will begin on the word %s. Ready? Set? %s." % (word_list[9], word_list[9]))
