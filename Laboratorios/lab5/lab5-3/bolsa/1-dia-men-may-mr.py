from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        lista = [float(price), date]
        yield company, lista

    def reducer(self, company, values):
        l = list(values)
        may = 0
        mayDat = ""
        men = 1000000000000000000
        menDat = ""
        for i in l:
            if i[0] > may:
                if may != 0 and may < men:
                    menDat = mayDat
                    men = may
                mayDat = i[1]
                may = i[0]
            if i[0] < men:
                men = i[0]
                menDat = i[1]
        

        yield company, (menDat, mayDat)

if __name__ == '__main__':
    MRWordFrequencyCount.run()