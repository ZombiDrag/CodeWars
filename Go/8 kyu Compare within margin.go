package kata
 
import "math"



func CloseCompare(a, b, margin float64) int {
   
  if a == b || (math.Max(a,b) - math.Min(a,b) <= margin){
    return 0
  }else{
    if a < b {
		return -1
	  } else {
		return 1
    } 
  }
}