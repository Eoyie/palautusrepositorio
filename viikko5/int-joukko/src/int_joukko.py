KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        
        if not kapasiteetti:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int):
            raise TypeError("Kapasiteetti ei ole int")
        elif kapasiteetti < 0:
            raise ValueError("Kapasiteetti on negatiivinen")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if not kasvatuskoko:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int):
            raise TypeError("Kasvatuskoko ei ole int")
        elif kasvatuskoko < 0:
            raise ValueError("Kasvatuskoko on negatiivinen")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.lista:
            return True
        return False

    def lisaa(self, luku):
        if self.alkioiden_lkm == 0:
            self.lista[0] = luku
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(luku):
            self.lista[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.lista) == 0:
                self.kasvata_listaa()
            return True
        return False

    def kasvata_listaa(self):
        vanha_lista = self.lista
        self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(vanha_lista)
        
    def kopioi_lista(self, vanha_lista):
        self.lista[:len(vanha_lista)] = vanha_lista[:len(vanha_lista)]
            
    def poista(self, luku):
        if luku in self.lista:
            kohta = self.lista.index(luku)
            self.lista[kohta] = 0
            self.lista = self.lista[:kohta] + self.lista[kohta + 1:] + [0]
            self.alkioiden_lkm -= 1
            return True
        return False
        
    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lista[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(eka, toka):
        yhdisteen_joukko = IntJoukko()
        eka_int_lista = eka.to_int_list()
        toka_int_lista = toka.to_int_list()

        for luku in eka_int_lista:
            yhdisteen_joukko.lisaa(luku)

        for luku in toka_int_lista:
            yhdisteen_joukko.lisaa(luku)

        return yhdisteen_joukko

    @staticmethod
    def leikkaus(eka, toka):
        leikkauksen_joukko = IntJoukko()
        eka_int_lista = eka.to_int_list()
        toka_int_lista = toka.to_int_list()

        for luku in eka_int_lista:
            if luku in toka_int_lista:
                leikkauksen_joukko.lisaa(luku)

        return leikkauksen_joukko

    @staticmethod
    def erotus(eka, toka):
        erotuksen_joukko = IntJoukko()
        eka_int_lista = eka.to_int_list()
        toka_int_lista = toka.to_int_list()

        for luku in eka_int_lista:
            if luku not in toka_int_lista:
                erotuksen_joukko.lisaa(luku)

        return erotuksen_joukko

    def __str__(self):
        return "{" + str(self.to_int_list())[1:-1] + "}"
