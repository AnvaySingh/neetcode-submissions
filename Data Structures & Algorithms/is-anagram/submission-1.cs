public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length!=t.Length)
        {
            return false;
        }

        char[] firstarray=s.ToCharArray();
        char[] secondarray=t.ToCharArray();

        Array.Sort(firstarray);
        Array.Sort(secondarray);

        return firstarray.SequenceEqual(secondarray);

    }
}
