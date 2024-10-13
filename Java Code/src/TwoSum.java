import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        // Initialize with load factor 1 to avoid rehashing
        Map<Integer, Integer> map = new HashMap<>(nums.length, 1.0f);

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            Integer complementIndex = map.get(complement);

            if (complementIndex != null) {
                return new int[] { complementIndex, i };
            }

            map.put(nums[i], i);
        }

        // If no solution is found (this should not happen according to problem constraints)
        throw new IllegalArgumentException("No two sum solution");
    }
}
