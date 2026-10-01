class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()
        for e in emails:
            e = e.split('@')
            local = e[0].split('+')[0].replace('.','')
            local = local + '@' + e[1]
            hash_set.add(local)

        return len(hash_set)
