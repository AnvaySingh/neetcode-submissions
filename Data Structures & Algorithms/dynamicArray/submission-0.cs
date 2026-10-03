public class DynamicArray {
    private List<int> dynamicArray;
    
    public DynamicArray(int capacity) {
        dynamicArray = new List<int>(capacity);
    }

    public int Get(int i) {
        int get = dynamicArray[i];
        return get;
    }

    public void Set(int i, int n) {
        dynamicArray[i] = n;
    }

    public void PushBack(int n) {
        if (dynamicArray.Count == dynamicArray.Capacity) {
            Resize();
        }
        dynamicArray.Add(n);
    }

    public int PopBack() {
        int len = GetSize() - 1;
        int val = dynamicArray[len];
        dynamicArray.RemoveAt(len);
        return val;
    }

    private void Resize() {
        dynamicArray.Capacity *= 2;
    }

    public int GetSize() {
        return dynamicArray.Count;
    }

    public int GetCapacity() {
        return dynamicArray.Capacity;
    }
}