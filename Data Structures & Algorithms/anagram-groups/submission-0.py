class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        anagram_dict = {}
        for str in strs:
            if "".join(sorted(str)) in anagram_dict:
                anagram_dict["".join(sorted(str))].append(str)
            else:
                anagram_dict["".join(sorted(str))] = [str]
        for key, value in anagram_dict.items():
            res.append(value)
        return res