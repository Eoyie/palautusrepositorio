from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._viimeinen_komento = None  #Ei paras.. mutta toimii?
        
        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._palauta_viimeinen_komento)
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()
    
    def _palauta_viimeinen_komento(self):
        return self._viimeinen_komento
    
    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._viimeinen_komento = komento_olio
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.arvo = None
        
    def suorita(self):
        self.arvo = self._sovelluslogiikka.arvo()
        arvo = self.syote()
        self._sovelluslogiikka.plus(int(arvo))
        
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self.arvo)
            
class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.arvo = None
        
    def suorita(self):
        self.arvo = self._sovelluslogiikka.arvo()
        arvo = self.syote()
        self._sovelluslogiikka.miinus(int(arvo))
        
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self.arvo)
            
            
class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.arvo = None
        
    def suorita(self):
        self.arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()
        
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self.arvo)
            
            
class Kumoa:
    def __init__(self, sovelluslogiikka, viimeinen_komento):
        self._sovelluslogiikka = sovelluslogiikka
        self.viimeinen_komento = viimeinen_komento
        
    def suorita(self):
        viimeinen_komento = self.viimeinen_komento()
        viimeinen_komento.kumoa()