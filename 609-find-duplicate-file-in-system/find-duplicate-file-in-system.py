class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict = defaultdict(list)

        for path in paths:
            main, *files = path.split()
            for f in files:
                fr, fn = f.split("(")
                path_dict[fn].append(main + '/' + fr)
        res = []
        for value in path_dict.values():
            if len(value) > 1:
                res.append(value)
        return res