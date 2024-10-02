class Anagram:
    def func(self,s1,s2):
        f1 = {}
        f2 = {}
        if len(s1) != len(s2):
            return False
        for i in s1:
            if i in f1:
                f1[i] += 1
            else:
                f1[i] = 1
        for i in s2:
            if i in f2:
                f2[i] += 1
            else:
                f2[i] = 1
        for j in f1:
            if j not in f2:
                return False
            else:
                return True
obj = Anagram()
s1 = "samba"
s2 = "ambs"
print(obj.func(s1,s2))