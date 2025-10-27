from collections import defaultdict,deque

def solution(tickets):
    ticket_dict = defaultdict(deque)
    
    for start,end in sorted(tickets):
        ticket_dict[start].append(end)
        
    answer = ["ICN"]
    def DFS(start):
        if len(answer) == len(tickets) + 1:
            return True
        
        if start in ticket_dict:
            for i in range(len(ticket_dict[start])):
                country = ticket_dict[start].popleft()
                answer.append(country)
                if DFS(country):
                    return True
                answer.pop()
                ticket_dict[start].append(country)
    
    DFS("ICN")
    return answer