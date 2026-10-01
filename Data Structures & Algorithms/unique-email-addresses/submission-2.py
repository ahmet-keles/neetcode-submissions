class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mp = set()
        for e in emails:
            e = e.split('@')
            local = e[0].split('+')[0].replace('.','')
            local = local + '@' + e[1]
            mp.add(local)

        return len(mp)
