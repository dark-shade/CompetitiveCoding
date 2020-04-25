from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # {"domain": count}
        count_dict = {}
        final_list = []

        for cpdomain in cpdomains:
            domain_cnt = cpdomain.split()[1].split('.')
            prev = ""

            for d in domain_cnt[::-1]:
                if len(prev) > 0:
                    prev = d + "." + prev
                else:
                    prev = d
                               
                if prev not in count_dict:
                    count_dict[prev] = 0
                count_dict[prev] += int(cpdomain.split()[0])

        for domain in count_dict.keys():
            final_list.append(str(count_dict[domain]) + " " + domain)

        return final_list
        