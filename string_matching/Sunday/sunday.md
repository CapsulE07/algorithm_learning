 Sunday算法由Daniel M.Sunday在1990年提出，它的思想跟BM算法很相似：

只不过Sunday算法是从前往后匹配，在匹配失败时关注的是文本串中参加匹配的最末位字符的下一位字符。
如果该字符没有在模式串中出现则直接跳过，即移动位数 = 匹配串长度 + 1；
否则，其移动位数 = 模式串中最右端的该字符到末尾的距离+1。
————————————————
版权声明：本文为CSDN博主「v_JULY_v」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/v_july_v/article/details/7041827


平均性能的时间复杂度为O(n)； 
最差情况的时间复杂度为O(n * m)。


匹配原理： 
从前往后匹配： 
- 如果遇到不匹配情况判断母串 dest 参与匹配的最后一位的下一位字符，如果该字符出现在模板串 pattern 中，选择最右出现的位置进行对齐； 
- 否则直接跳过该匹配区域。
————————————————
版权声明：本文为CSDN博主「Wonder233」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wonder233/article/details/79035403

```
输入: haystack, needle
Init: i=0, j=0
while i<=len(haystack)-len(needle):
    j=0
    while j<len(needle) and haystack[i+j] equals needle[j]:
        j=j+1
    if j equals len(needle):
        return i
    else
        increase i...
```