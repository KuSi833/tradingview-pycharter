from Charter import Charter

myCharter = Charter("chartex")

# myCharter.draw_label(1619168400000, -1, "lol", "bar_time", "belowbar",
#                                      "red", "style_label_up", "white", "large", "align_left", "lol explanation")

myCharter.draw_label(1619168400000, "close", text="test text")
myCharter.draw_line(1619168400000, "close", 1619168400000+1, "close", extend="extend.right")

myCharter.write_instructions()