import operator
class Nmeetings:
    def maximumMeetings( n, start, end):
        # code here
        meetings = []
        for i in range(len(start)):
            meetings += [(start[i], end[i], i)]
        answer = 1
        last = meetings[0][1]
        meetings = sorted(meetings, key = operator.itemgetter(1, 2))
        for i in range(1, len(meetings)):
            if meetings[i][0] > last:
                last = meetings[i][1]
                answer = answer + 1
                print(answer)
            else:
                pass
        return answer
    if __name__== "__main__":
        start=[1,3,0,5,8,5]
        end=[2,4,6,7,9,9]
        n=len(start)
        

        print(maximumMeetings(n,start,end))
