class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        # Sort folders lexicographically
        folder.sort()
        result = []

        for f in folder:
            # If result is empty or f is not a subfolder of the last folder in result, add it to result
            if not result or not f.startswith(result[-1] + "/"):
                result.append(f)

        return result
