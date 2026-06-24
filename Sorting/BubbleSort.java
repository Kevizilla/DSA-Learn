package Sorting;

import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args){
        int[] list = {6, 3, 7, 9, 2, 11, 15, 0};
        for (int i = list.length - 1; i > 0; i--) {
            boolean swapped = false;
            for (int j = 0; j < i; j++) {
                if (list[j] > list[j + 1]) {
                    int temp = list[j];
                    list[j] = list[j + 1];
                    list[j + 1] = temp;
                    swapped = true;
                }
            }
            if(!swapped) break;
        }
        System.out.println(Arrays.toString(list));
    }
}
