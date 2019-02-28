"""Suggests random dessert out of all the possible ingredients to combine in the
Olin dining hall."""

import random

cookies = ["chocolate chip","M&M","sugar"]
ice_creams = ["vanilla","chocolate","mint chocolate-chip","coconut","raspberry"]
sodas = ["coke","lemonade","powerade","iced tea","sprite","ginger ale"]

desserts = []

for cookie in cookies:
    for ice_cream in ice_creams:
        desserts.append(ice_cream + " ice cream/" + cookie + " cookie sandwich")

for ice_cream in ice_creams:
    for pb in [" with peanut butter",""]:
        desserts.append(ice_cream + " milkshake" + pb)

for ice_cream in ice_creams:
    for soda in sodas:
        desserts.append(soda + " float with " + ice_cream + " ice cream")

choice = random.choice(desserts)
print(choice)
