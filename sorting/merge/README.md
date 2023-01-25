# Blog Notes: Lets Take A Look at Merge Sort

## What is Merge Sort

The general idea or merge sort comes from taking a array or list of integers and turnig them into something similar to a binary tree, Lets say we have a list or and array of six integers [4,1,2,3]

 we are going to run a hot knife throught the center of the array, revealing a smaller two arrays [4,1], [2,3]
 
  then we are gonna slice it up again right at the center(assuming its an even number), until its even smaller [4],[1],[2],[3] 
  
  if this was a bigger array and they werent all inividuals at this stage we would keep slicing them up until we had a giant list of a bunch of differnt integers represented as their own node or element. 
  
  The goal is to get the smallest comparable lists so that we can work back moving everything into place

  we then take the two most adjacent, compare them, Oh is either of these numbers in the wrong place, if a number is out of place it will move into its desired position according to the sort

**Now Bear with me!!!**

I know this is getting confusing, but we are almost there, and ill break this down farther in a minute. 

OK, so we are at the comparing stage we have a [4],[1],[2],[3]

we are going to take [4],[1] 

[4] is in the wrong place because [1] is of lesser value, so we are going to change them to be in correct order and smash em back together [1,4]

now again with the other half

[2],[3] these are in the Right place, so they stay,

 now lets move up the tree and compare these to smaller segments as they want to be back to the original size later



