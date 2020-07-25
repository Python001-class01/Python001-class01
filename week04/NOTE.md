学习笔记

#### group_by
GROUP BY语句将具有相同值的行分组为摘要行，例如“查找每个国家/地区的客户数量”。
GROUP BY语句通常与聚合函数（COUNT，MAX，MIN，SUM，AVG）一起使用，以将结果集按一列或多列分组。

#### 作业问题

```sql
SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
```

COUNT(DISTINCT order_id) order_id唯一值的数量

```python
table1.groupby('id').agg({'order_id':pd.Series.nunique()})
```

