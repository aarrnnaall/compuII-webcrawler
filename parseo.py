from HTMLParser import HTMLParser 

class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        cont_sinesp = ' '.join(data.split()) 
        if cont_sinesp != "" and cont_sinesp[0:6] != 'jQuery' and cont_sinesp[0:6] != 'window' and cont_sinesp[0:6] != '(funct':
            if cont_sinesp[0:6] != '!funct' and cont_sinesp[0:2] != '/*' and cont_sinesp[0:4] != '.orb':
                if cont_sinesp[0:3] != '.ve' and cont_sinesp[0:4] != 'func' and cont_sinesp[0:3] != 'var':
                    if cont_sinesp[0:2] != "//":
                        print(cont_sinesp) 
