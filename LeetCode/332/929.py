from typing import List

"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_emails = set()

        for email in emails:
            parts = email.split("@")
            local_name = ""

            for ch in parts[0]:
                if ch == ".":
                    continue
                if ch == "+":
                    break
                local_name += ch
            
            final_emails.add(local_name + "@" + parts[1])

        return len(final_emails)            
"""

class Solution:
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

obj = Solution()
n = obj.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(n)
