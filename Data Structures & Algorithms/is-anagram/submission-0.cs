public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char,int> checkanagram=new Dictionary<char,int>();

        if(s.Length!=t.Length)
        {
            return false;
        }

        foreach(char c in s)
        {
            if(checkanagram.ContainsKey(c))
            {
                checkanagram[c]++;
            }
            else
            {
                checkanagram[c]=1;
            }
        }

        foreach(char a in t)
        {
            if(checkanagram.ContainsKey(a))
            {
                checkanagram[a]--;
                if(checkanagram[a]<0)
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }

        foreach(var check in checkanagram)
        {
            if(check.Value!=0)
            {
                return false;
            }
        }

        return true;
    }
}
