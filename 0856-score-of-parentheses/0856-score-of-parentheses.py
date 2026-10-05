class Solution:

    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Tracks the score at the current nesting depth

        for char in s:
            if char == "(":
                stack.append(0)  # Enter a deeper nesting level
            else:
                v = stack.pop()
                # If v is 0, it means we found an immediate "()", which scores 1.
                # Otherwise, it's (A), which scores 2 * A.
                score = max(2 * v, 1)
                stack[-1] += score

        return stack.pop()
