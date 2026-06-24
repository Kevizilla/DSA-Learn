package Sorting;

public class SelectionSort {

    public static int[] sort(int[] list) {
        for (int i = 0; i < list.length; i++) {
            int minVal = list[i];
            int minIndex = i;
            for (int j = i + 1; j < list.length; j++) {
                if (list[j] < minVal) {
                    minVal = list[j];
                    minIndex = j;
                }
            }
            if (minIndex != i) {
                list[minIndex] = list[i];
                list[i] = minVal;
            }
        }
        return list;
    }
}