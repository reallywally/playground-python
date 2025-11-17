s = "abc"
t = "ahbgdc"
r = []

for i in s:
    r.append(t.find(i))
    
    is_increasing = all(b > a for a, b in zip(r, r[1:]))