class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = dict()
        for dep,des in tickets:
            if dep in flights:
                flights[dep].append(des)
            else:
                flights[dep] = [des]

        for dep in flights:
            flights[dep].sort(reverse = True)
        print(flights)


        # ans = ["JFK"]
        # end = 0
        # curr = "JFK"

        # while True:
        #     try:
        #         curr = flights[curr]
        #     except:
        #         break
        #     if curr == []:
        #         break

        #     if len(curr) >= 1:
        #         curr = curr.pop()
                
        #     ans += [curr]

        def dfs(airport):
            while airport in flights and flights[airport]:
                next_airport = flights[airport].pop()
                dfs(next_airport)

            ans.append(airport)

        ans = []
        dfs("JFK")

        return ans[::-1]

            
        