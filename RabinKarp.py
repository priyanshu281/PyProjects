class Solution:
    def search(self, pat:str, text: str, q:int):
        d=256
        m=len(pat)
        n=len(text)
        #hash value of pattern is p and text is t
        p=0
        t=0
        h=1
        for i in range(m-1):
            h=(h*d)%q  #pow(d, m-1)%q here modulo operation respects distributive property.
            #ie a%c * b%c = (a*b)%c

        for i in range(m):
            p= (p*d + ord(pat[i]))% q
            t= (t*d + ord(text[i]))% q

        for  i in range(n-m+1):
            if p==t:

                for j in range(m):
                    if pat[j] != text[i+j]:
                        break
                    else:
                        j+=1
                    if j==m:
                        print("Pattern found at index " + str(i))
            if i<  n-m:
                t= (d*(t- h*ord(text[i])) + ord(text[i+m]))%q
                if t< 0:
                    t=t+q

if __name__ == "__main__":
    txt= "GEEKS FOR GEEKS"
    pat= "GEEK"
    q=101
    s=Solution()
    s.search(pat=pat, text=txt, q=q)


