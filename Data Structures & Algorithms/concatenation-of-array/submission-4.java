class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[2 * nums.length];

        int index = 0;

        // First copy
        for (int i = 0; i < nums.length; i++) {
            ans[i] = nums[i];
            index++;
        }

        // Second copy
        for (int i = 0; i < nums.length; i++) {
            ans[index] = nums[i];
            index++;
        }

        return ans;
    }
}




