#### 排序总结
<table>
    <tr>
        <th>算法</th><th>时间复杂度</th><th>空间复杂度</th><th>稳定性</th>
    </tr>
    <tr>
        <td>选择排序</td><td>O(N^2)</td><td>O(1)</td><td>不稳定</td>
    </tr>
    <tr>
        <td>冒泡排序</td><td>O(N^2)</td><td>O(1)</td><td>稳定</td>
    </tr>
    <tr>
        <td>插入排序</td><td>O(N^2)</td><td>O(1)</td><td>稳定</td>
    </tr>
    <tr>
        <td>归并排序</td><td>O(NlogN)</td><td>O(N)</td><td>稳定</td>
    </tr>
    <tr>
        <td>快速排序</td><td>O(NlogN)</td><td>O(logN)</td><td>不稳定</td>
    </tr>
    <tr>
        <td>堆排序</td><td>O(NlogN)</td><td>O(N)</td><td>不稳定</td>
    </tr>
</table>

以上是针对数的比较排序，不基于数的比较排序，如计数排序，基数排序，都是基于数据状况的排序，应用状况比较窄，根据实际情况定制。
```
稳定性是指同样值的个体之间，如果不因为排序而改变相对次序，就说这个排序是有稳定性的，否则就没有。
```
#### 工程上对排序的改进

1) 充分利用O(NlogN)和O(N^2)排序各自的优势，比如快速排序，数据基数少可以插入排序
2) 稳定性的考虑