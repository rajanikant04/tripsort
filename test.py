# from tools.tavily import tavily_search

# res= tavily_search("Best travel destinations in Europe")
# print(res)

from tools.flight_tool import search_flights
res= search_flights("Plan a 7 days Japan trip from INDIA")
print(res)