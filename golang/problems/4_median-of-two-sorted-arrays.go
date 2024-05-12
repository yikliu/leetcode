/*
 * @lc app=leetcode id=4 lang=golang
 *
 * [4] Median of Two Sorted Arrays
 */
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
  m, n := len(nums1), len(nums2)
  total := m + n
  if total%2 == 1 {
    return findKth(nums1, nums2, total/2+1)
  } else {
    return (findKth(nums1, nums2, total/2) + findKth(nums1, nums2, total/2+1)) / 2
  }
}

/*
K starts with 1.
*/
func findKth(nums1 []int, nums2 []int, k int) float64 {
  m, n := len(nums1), len(nums2)
  if m > n {
    return findKth(nums2, nums1, k)
  }
  if m == 0 {
    return float64(nums2[k-1])
  }
  if k == 1 {
    return float64(min(nums1[0], nums2[0]))
  }

  i := min(m, k/2)
  j := min(n, k/2)

  if nums1[i-1] > nums2[j-1] {
    return findKth(nums1, nums2[j:n], k-j)
  } else {
    return findKth(nums1[i:m], nums2, k-i)
  }
}

func min(i int, j int) int {
  if i >= j {
    return int(j)
  } else {
    return int(i)
  }
}
