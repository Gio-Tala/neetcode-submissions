class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # need to see if we can find valid topological sort
        prereq_map = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        seen_courses = set()
        def dfs_find_loops(curr_course):
            # no prereqs
            if not prereq_map[curr_course]:
                return True
            
            # if we've alr visited a prereq
            if curr_course in seen_courses:
                return False
            
            # mark as seen, loop through prerequiste courses, 
            seen_courses.add(curr_course)
            for prereq in prereq_map[curr_course]:
                if not dfs_find_loops(prereq):
                    return False
            prereq_map[curr_course] = []
            seen_courses.remove(curr_course)
            return True
        
        for i in range(numCourses):
            if not dfs_find_loops(i):
                return False
        
        return True