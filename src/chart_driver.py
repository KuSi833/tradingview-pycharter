from Charter import Charter

myCharter = Charter(chart_name="chartex", timeframe=1000*60*60)

# myCharter.draw_label(1619168400000, -1, "lol", "bar_time", "belowbar",
#                                      "red", "style_label_up", "white", "large", "align_left", "lol explanation")

# myCharter.draw_label(1619168400000, "close", text="test text")
# myCharter.draw_line(1619168400000, "close", 1619168400000+1, "close", extend="extend.right")
myCharter.draw_vertical_line(1619168400000, "close", color="color.red")

myCharter.write_instructions()