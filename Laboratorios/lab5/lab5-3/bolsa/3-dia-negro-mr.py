from mrjob.job import MRJob




class MRWordFrequencyCount(MRJob):
    
    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield date, price

    def reducer(self, date, values):
        mayor = precioDiaNegro
        l = list(values)
     
        if precioDiaNegro < sum(l):
            precioDiaNegro = sum(l)
            fecha = date
            


if __name__ == '__main__':
    MRWordFrequencyCount.run()
    print("Dia negro:", fecha)