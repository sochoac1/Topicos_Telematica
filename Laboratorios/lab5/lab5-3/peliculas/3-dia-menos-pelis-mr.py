from mrjob.job import MRJob

lista1 = []
class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        user, movie,rating,genre, date = line.split(',')
        yield date, movie

    def reducer(self, date, values):
        l = list(values)
        lista1.append([len(l), date])
        
        yield date, len(l)



if __name__ == '__main__':
    MRWordFrequencyCount.run()
    menor = 10000000000000
    fecha = ""
    for i in lista1:
        if i[0] < menor:
            menor = i[0] 
            fecha = i[1]
    print(fecha)