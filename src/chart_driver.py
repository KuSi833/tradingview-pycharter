from Charter import Charter

myCharter = Charter(chart_name="chartex", timeframe=1000*60*60)

# myCharter.draw_label(1619168400000, -1, "lol", "bar_time", "belowbar",
#                                      "red", "style_label_up", "white", "large", "align_left", "lol explanation")

myCharter.draw_label(1619168400000, "close", text="test text")
# myCharter.draw_line(1619168400000, "close", 1619168400000+1, "close", extend="extend.right")
myCharter.draw_hline(2000, "buy now", "color.green", persistance=True, name="h1")
myCharter.draw_hline(2200, "sell now", "color.red", persistance=True, name="h2")

myCharter.write_instructions()