class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_parts = address.split('.')
        new_address = '[.]'.join(address_parts)
        return new_address