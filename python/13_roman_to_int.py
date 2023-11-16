class Solution:
    """
        Converrt roman to integer. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    """
    def romanToInt(self, s: str) -> int:
        mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special_cases = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        mapper['special_cases'] = special_cases
      
        items = list(s)
        result = 0
        while len(items):
            if ''.join(items[:2]) in mapper['special_cases']:
                result += mapper['special_cases'][''.join(items[:2])]
                del items[:2]
                
            elif items[0] in mapper:
                result += mapper[items[0]]
                del items[0]
                
        return result
        
        
if __name__ == '__main__':
    solution = Solution()
    s = "III" # 3
    print(solution.romanToInt(s))
    
    s = "LVIII" # 58
    print(solution.romanToInt(s))
    
    s = s = "MCMXCIV" # 1994
    print(solution.romanToInt(s))
    