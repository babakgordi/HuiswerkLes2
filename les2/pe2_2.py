cijferICOR = 7.8
cijferPROG = 8.3
cijferCSN = 6.2
vakken = [cijferICOR, cijferPROG, cijferCSN]

gemiddelde = round(sum(vakken) / len(vakken), 1)

beloning = round((gemiddelde * 3) * 30, 1)

overzicht = 'Mijn cijfers (gemiddeld een %.1f) ' \
            'leveren een beloning van €%.1f op!' %(gemiddelde, beloning)



print(overzicht)
