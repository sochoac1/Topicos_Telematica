from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, sector

    def reducer(self, idemp, values):
        cont = 1
        l = list(values)
        v = l[0]
        for i in l:
            if i != v:
               cont += 1 

        yield idemp, cont

if __name__ == '__main__':
    MRWordFrequencyCount.run()