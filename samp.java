import java.util.HashSet;

public class samp{
public static void main(String[] args) {
    String arr[] = {"java","Python","C","C"};
    // boolean flag= false;
    // for(int i=0;i<arr.length;i++){
    //     for(int j = i+1;j<arr.length;j++){
    //         if(arr[i]==arr[j]){
    //             System.out.println("Duplicate");
    //             flag = true;
    //         }
    //     }
    // }
    // if (flag == false){
    //     System.out.println("No duplicates");
    // }
    HashSet <String> has = new HashSet<>();
    for (String i : arr){
        System.out.println(has.add(i));
    } 
    
}
}