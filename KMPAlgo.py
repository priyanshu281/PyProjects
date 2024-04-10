class Solution:
    def computeLPSArray(self, pat:str, m):
        ln=0
        i=1
        lps= [None]* m
        lps[0]=0
        while i< m:
            if pat[i]== pat[ln]:
                ln+=1
                lps[i]= ln
                i+=1
            elif ln>0 and pat[i] != pat[ln]:
                ln=lps[ln-1]
            else:
                lps[i]=ln
                i=i+1
        return lps
    def searchPatternUsingKMP(self, pat: str, text: str, m , n):
        i=0 #for text
        j=0 # for pattern
        lps=self.computeLPSArray(pat, m)
        while n-i > m-j: #chaggpt why is this better than i < n while condition
            if text[i] == pat[j]:
                i+=1
                j+=1
            if j==m:
                print("found:", str(i-j))
                j=lps[j-1]

            elif i < n-m and text[i] != pat[j]:

                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1


            elif i>n-m:
                break




if __name__ == "__main__":
    txt = "ABABABCABABABCABABABC"
    pat = "ABABAC"
    s=Solution()
    m=len(pat)
    n=len(txt)
    s.searchPatternUsingKMP(pat, txt, m,n)