package Sorting;

import java.util.Arrays;

class SelectionSort {
    public static void main(String[] args){
        int[] list = {5, 13, 2, 8 ,11 ,9, 14};
        for(int i = 0; i < list.length; i++){
            int minVal =  list[i];
            int minIndex = i;
            for(int j = i+1; j < list.length; j++){
                if(list[j] < minVal){
                    minVal = list[j];
                    minIndex = j;
                }
            }
            if(minVal == list[i]){
                continue;
            }
            else {
                list[minIndex] = list[i];
                list[i] = minVal;
            }
        }
        System.out.println(Arrays.toString(list));
    }
}
