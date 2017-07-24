from tkinter import *

def pretvori_niz(niz):
    rezultat=''
    znotraj_korena = False
    stevilo='0123456789'
    stevilo_oklepajev=0
    
    for x in niz:
        if x == '√':
            znotraj_korena = True

            koren=niz.index(x)
            if koren==0:
                rezultat += '('
            elif niz[koren-1] in stevilo:
                rezultat += '*('
            elif niz[koren-1] == '%':
                rezultat += '*('
            else:
                rezultat += '('

        elif x == '(' and znotraj_korena == True:
            rezultat += '('
            stevilo_oklepajev += 1

        elif x == ')' and znotraj_korena == True:
            if stevilo_oklepajev > 1:
                rezultat += ')'
                stevilo_oklepajev -= 1
            elif stevilo_oklepajev == 1:
                stevilo_oklepajev -= 1
                rezultat += ')**(1/2))'
                znotraj_korena = False

        elif x == '%' and znotraj_korena == True:
            if stevilo_oklepajev == 0:
                rezultat += ')**(1/2)' + '%'
                
                znotraj_korena = False
            else:
                rezultat += '%' 
                
        elif x in stevilo and znotraj_korena == True:
            rezultat += x

        elif x == '.' and znotraj_korena == True:
            rezultat += x
            
        elif x not in stevilo and znotraj_korena==True:
            if stevilo_oklepajev == 0:
                znotraj_korena=False
                rezultat += ')'+'**(1/2)'+x
            else:
                rezultat += x
                
        else:
            rezultat+=x
    if znotraj_korena == True:
        return rezultat + ')'+'**(1/2)'
    else:
        return rezultat
            
            

class kalkulator:

    def __init__(self):
        
        okno = Tk()
        okno.title('Kalkulator')
        okno.configure(background = 'white')
        okno.resizable(0, 0)
        #onemogoča povečanje okna

        
        self.error = False
        #ta oznaka self.error je ustvarjena za primere napak
        #uporabnik bo za preklic Error-ja uporabil le Clear
        #na drugih mestih bomo učinek preklicali
        
        self.string = StringVar()

        e = Entry(okno, textvariable = self.string, width = 30,
                bd = 10, bg = 'white', justify = RIGHT, font = 'Helvetica 15 bold')
        e.grid(row = 0, columnspan = 6)
        e.bind('<KeyPress>', self.keyPress)
        e.focus()
        #focus usmeri začetno dogajanje


        #bg = background color
        #bd = border
        Button(okno, text = "=", bg = 'light blue', width = 14, height = 2, command = lambda: self.enačaj()).grid(row = 3,column = 5,rowspan = 2, sticky = 'NWNESWSE')
        Button(okno, text = 'Clear', width = 5, height = 2, command = lambda: self.počisti_vse()).grid(row = 1, column = 5, sticky = 'NWNESWSE')
        Button(okno, text = '<-', width = 5, height = 2, command = lambda: self.pobriši_zadnji_element()).grid(row = 2, column = 5, sticky = 'NWNESWSE')
        Button(okno, text = "+", width = 5, height = 2, command = lambda: self.dodaj_vrednost('+')).grid(row = 3, column = 3, sticky = 'NWNESWSE')
        Button(okno, text = "*", width = 5, height = 2, command = lambda: self.dodaj_vrednost('*')).grid(row = 4, column = 3, sticky = 'NWNESWSE')
        Button(okno, text = "-", width = 5, height = 2, command = lambda: self.dodaj_vrednost('-')).grid(row = 3, column = 4, sticky = 'NWNESWSE')
        Button(okno, text = "/", width = 5, height = 2, command = lambda: self.dodaj_vrednost('/')).grid(row = 4, column = 4, sticky = 'NWNESWSE') 
        Button(okno, text = "%", width = 5, height = 2, command = lambda: self.dodaj_vrednost('%')).grid(row = 4, column = 2, sticky = 'NWNESWSE')
        Button(okno, text = "7", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(7)).grid(row = 1, column = 0, sticky = 'NWNESWSE')
        Button(okno, text = "8", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(8)).grid(row = 1, column = 1, sticky = 'NWNESWSE')
        Button(okno, text = "9", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(9)).grid(row = 1, column = 2, sticky = 'NWNESWSE')
        Button(okno, text = "4", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(4)).grid(row = 2, column = 0, sticky = 'NWNESWSE')
        Button(okno, text = "5", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(5)).grid(row = 2, column = 1, sticky = 'NWNESWSE')
        Button(okno, text = "6", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(6)).grid(row = 2, column = 2, sticky = 'NWNESWSE')
        Button(okno, text = "1", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(1)).grid(row = 3, column = 0, sticky = 'NWNESWSE')
        Button(okno, text = "2", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(2)).grid(row = 3, column = 1, sticky = 'NWNESWSE')
        Button(okno, text = "3", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(3)).grid(row = 3, column = 2, sticky = 'NWNESWSE')
        Button(okno, text = ".", width = 5, height = 2, command = lambda: self.dodaj_vrednost('.')).grid(row = 4, column = 0, sticky = 'NWNESWSE')
        Button(okno, text = "0", bg = 'light blue', width = 5, height = 2, command = lambda: self.dodaj_vrednost(0)).grid(row = 4, column = 1, sticky = 'NWNESWSE')
        Button(okno, text = "(", width = 5, height=2, command = lambda: self.dodaj_vrednost('(')).grid(row = 1, column = 3, sticky = 'NWNESWSE')
        Button(okno, text = ")", width = 5, height=2, command = lambda: self.dodaj_vrednost(')')).grid(row = 1, column = 4, sticky = 'NWNESWSE')
        Button(okno, text = "√", width = 5, height=2, command = lambda: self.dodaj_vrednost('√')).grid(row = 2, column = 3, sticky = 'NWNESWSE')
        Button(okno, text = "^", width = 5, height=2, command = lambda: self.dodaj_vrednost('^')).grid(row = 2, column = 4, sticky = 'NWNESWSE')

        #z opcijo sticky lahko lepo razporedimo gumbe; 'NWNESWSE' so smeri neba

        
        okno.mainloop()


    #za vrnitev trenutne vrednosti niza uporabimo string.get
    #za nastavitev trenutne vrednosti niza pa uporabimo string.set

   
    def počisti_vse(self):
        self.string.set('')
        self.error = False

    def pobriši_zadnji_element(self):
        if(not self.error):
            self.string.set(self.string.get()[0 : -1])

    

    def enačaj(self):
        #začetni rezultat bo postavljen na nič, operacijo bomo postavili na try
        #poskušal bo ovrednotiti niz, če mu ne bo uspelo, vrne napako Error
        #pomagamo si s funkcijo Eval
        #Eval() evaluates the passed string as a Python expression and returns the result

        rezultat=''
        vpisano = self.string.get()
        if '√' in vpisano:
            vpisano = pretvori_niz(vpisano)

        if '^' in vpisano:
            vpisano = vpisano.replace('^', '**')

        if '%' in vpisano:
            vpisano = vpisano.replace('%','*0.01')
            
        try:
            rezultat = eval(vpisano)
        except:
            self.error = True
            rezultat = 'Error'
                
        self.string.set(rezultat)

    def dodaj_vrednost(self, vrednost):
        if(not self.error):
            self.string.set(self.string.get() + (str(vrednost)))

    def keyPress(self, event):
        return 'break'
        #ob pritisku na tipkovnico ne izpiše ničesar
        
        
kalkulator()
