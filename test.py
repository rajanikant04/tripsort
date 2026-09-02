# from tools.tavily import tavily_search
# res= tavily_search("Best travel destinations in Europe")
# print(res)

# from tools.flight_tool import search_flights
# res= search_flights("Plan a 7 days Japan trip from INDIA")
# print(res)

from backend import run_travel_agent
user_query = input("Enter your travel query: ")
res= run_travel_agent(user_query, thread_id="test_thread")
print(res['answer'])