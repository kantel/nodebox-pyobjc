import pprint


fontFamilies = fontfamilies(flat=False)
# pprint.pprint(fontFamilies)


# filter all fixed width fonts
fixed = []
flatFonts = fontfamilies(flat=True)
for fontRec in flatFonts:
    if u'fixedpitch' in fontRec.traitnames:
        fixed.append( fontRec )
pprint.pprint( fixed )

print "font families:", len(fontFamilies)
print "fonts:", len(flatFonts)
print "fixed width fonts:", len(fixed)