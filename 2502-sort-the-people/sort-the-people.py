class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        people = [(names[i], heights[i]) for i in range(n)]

        for i in range(1, n):
            current_name, current_height = people[i]
            j = i - 1
            while j >= 0 and people[j][1] < current_height:  
                people[j + 1] = people[j]  
                j -= 1
            people[j + 1] = (current_name, current_height)  
        
        sorted_names = [person[0] for person in people]
        return sorted_names
            