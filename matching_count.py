def count(s1, s2):
    char_of_s1=set(s1)
    char_of_s2=set(s2)    
    common_char= char_of_s1 & char_of_s2
    print("Matching Characters: ",len(common_char))
s1="abgfhij2@1"
s2="@1khgabop"
count(s1,s2)