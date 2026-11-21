from tracemalloc import start


n=10
end=100
start=0
length=10
power=2

L1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
L2 = ["a","b","c","d","e","f","g","h","i","j"]
L3 = ["cc","dd","ee","ff","gg","hh","ii","jj","kk","ll"]
for x,y,z in zip(L1,L2,L3):
        print(x,y,z)