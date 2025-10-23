def solution(s):
    if len(s) % 2 == 1:
        return 0

    pairs = {')': '(', ']': '[', '}': '{'}

    def is_valid(t: str) -> bool:
        st = []
        for ch in t:
            if ch in '([{':
                st.append(ch)
            else:
                if not st or st[-1] != pairs.get(ch):
                    return False
                st.pop()
        return not st

    n = len(s)
    ans = 0
    for i in range(n):
        if is_valid(s[i:] + s[:i]):
            ans += 1
    return ans
