def plsdie(num, opencount, closecount, s, ans):
    # opencount is the total number of times the parentheses will open
    # closecount is the total number of times the parentheses will close
    # num will be user input
    # s will be an iteration that'll happen all over your answer
    # ans will be the final output
    if opencount == num and closecount == num:
        ans.append(s)
        return ans
    if opencount < num:
        plsdie(num, opencount+1, closecount, s+"[", ans)
    if closecount < opencount:
        plsdie(num, opencount, closecount+1, s+"]", ans)


num = int(input("Enter a number. Just do it. Please: "))
ans = []
plsdie(num, 0, 0, "", ans)
for s in ans:
    print(s)