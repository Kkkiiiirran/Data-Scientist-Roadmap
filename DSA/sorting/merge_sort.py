a = [6334, 4098, 7968, 4523, 277, 6956, 4560, 2062, 5705, 5743, 879, 5626, 9961, 491, 2995, 741, 4827]

def merge(a, left, mid, right):
    i = left
    j = mid +1
    ans = []
    while(i<=mid and j<=right):
        if(a[i]< a[j]):
            ans.append(a[i])
            i+=1
        else:
            ans.append(a[j])
            j+=1

    while(i<=mid):
        ans.append(a[i])
        i+=1

    while(j<=right):
        ans.append(a[j])
        j+=1

    for s in range(len(ans)):
        a[left] = ans[s]
        left+=1 



def merge_sort(a, left, right):
    if left>=right:
        return

    mid = (left+right)//2

    merge_sort(a, left, mid)
    merge_sort(a, mid+1, right)

    merge(a, left, mid, right)

merge_sort(a, 0, len(a)-1)
print(a)

# class Solution:

#     def merge(self,arr, l, m, r): 
#         i=l
#         j=m+1
#         ans = [0] * (r-l+1)
#         k=l
        
#         while(i<=m and j<=r):
#             if arr[i] <= arr[j]:
#                 ans[k] = arr[i]
#                 i+=1
#             else:
#                 ans[k] = arr[j]
#                 j+=1
#             k+=1
#         while(i<=m):
#             ans[k] = arr[i]
#             k+=1
#             i+=1
#         while(j<=r):
#             ans[k] = arr[j]
#             k+=1
#             j+=1
            
#         for s in range(len(ans)):
#             arr[l] = ans[s]
#             l+=1
                
                
#     def mergeSort(self,arr, l, r):

#         if l>=r:
#             return
#         mid = (l+r) // 2
#         self.mergeSort(arr, l, mid)
#         self.mergeSort(arr, mid+1, r)
#         self.merge(arr, 0, mid, r)


