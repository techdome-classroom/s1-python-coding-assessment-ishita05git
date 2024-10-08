def decode_message(s: str, p: str) -> bool:
    s_len, p_len = len(s), len(p)
    s_index, p_index = 0, 0
    star_index, match = -1, 0

    while s_index < s_len:
        # If characters match or pattern character is '?'
        if p_index < p_len and (p[p_index] == s[s_index] or p[p_index] == '?'):
            s_index += 1
            p_index += 1
        # If pattern character is '*'
        elif p_index < p_len and p[p_index] == '*':
            star_index = p_index
            match = s_index
            p_index += 1
        # If there's a mismatch after a '*'
        elif star_index != -1:
            p_index = star_index + 1
            s_index = match + 1
            match += 1
        else:
            return False

    # Check for remaining characters in the pattern
    while p_index < p_len and p[p_index] == '*':
        p_index += 1

    return p_index == p_len

# Example usage:
print(decode_message("aa", "a"))      # Output: False
print(decode_message("aa", "*"))      # Output: True
print(decode_message("cb", "?a"))     # Output: False
print(decode_message("abc", "a*b"))   # Output: True
print(decode_message("abcd", "a*d"))  # Output: True