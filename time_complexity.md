## Time Complexitiy for all the tasks

- Task 0 : O(1)  
  Here the operations are independent of the size of the file, as we are only concerned with first and last record. So time complexity is unaffected by the input file size and hence it is BigO of 1 : O(1)
  
- Task 1 : O(n2)   
  Here there are two for loops, which runs on both the input files, and hence the time complexity will for worst case sceanario is BigO of n square : O(n2)

- Task 2 : O(n)    
  Here there is only one for loop with two condition check, and hence time complexity is BigO of n : O(n)

- Task 3 : O(n2 + n og n)    
  Here the solution contains two for loops, one for collecting the area codes and other for printing. Also it uses an inbuilt sorting algorithm based on Timsort, which has O(n log n) time complexity.
  
  So overall time complexity of this solution is O(n2 + n log n)

- Task 4 : O(n4)  
  Here the solution contains four different for loops, so making it a BigO of (n2)2.
