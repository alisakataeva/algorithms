

def native_search(text, substr):

    m = len(text)
    n = len(substr)

    for i in range(m - n + 1):

        j = 0

        while j < n and text[i+j] == substr[j]:
            j += 1
            if j == n:
                return i
    
    return False