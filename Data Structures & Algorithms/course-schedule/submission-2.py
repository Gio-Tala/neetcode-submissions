class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        seen_courses = set()
        def dfs_no_loops(course):
            # seen
            if course in seen_courses:
                return False
            
            # no prereqs
            if not prereq_map[course]:
                return True

            # add to seen, remove
            seen_courses.add(course)
            for next_prereq in prereq_map[course]:
                if not dfs_no_loops(next_prereq):
                    return False
            seen_courses.remove(course)
            prereq_map[course] = []
            return True
        for course, _ in prerequisites:
            if not dfs_no_loops(course):
                return False

        return True