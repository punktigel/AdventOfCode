
def get_sum(file):
    sum_1 = 0
    sum_2 = 0

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            fst, snd = line.split(',')

            fst_1, snd_1 = fst.split('-')
            fst_2, snd_2 = snd.split('-')
            
            
            if int(fst_1) <= int(fst_2) and int(snd_1) >= int(snd_2) or int(fst_1) >= int(fst_2) and int(snd_1) <= int(snd_2):
                sum_1 += 1
            
            # Part 2
            # a-b,c-d
            if int(fst_1) <= int(fst_2) and int(snd_1) >= int(fst_2):# a <= c and b >= c     c in [a,b]
                sum_2 += 1
            elif int(fst_1) <= int(snd_2) and int(snd_1) >= int(snd_2):# a <= d and b >= d     d in [a,b]
                sum_2 += 1
            elif int(fst_1) >= int(fst_2) and int(fst_1) <= int(snd_2):# a >= c and a <= d     a in [c,d]
                sum_2 += 1
            elif int(snd_1) >= int(fst_2) and int(snd_1) <= int(snd_2):# b >= c and b <= d     b in [c,d]
                sum_2 += 1
        
        print(f"Solution: \na): {sum_1}\nb): {sum_2}")

if __name__ == "__main__":
    get_sum('input.txt')