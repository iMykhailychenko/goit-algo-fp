# goit-algo-fp

З симуляції методом Монте-Карло зі 1000 000 ітерацій, можемо помітити наступне:

Ймовірності, обчислені за допомогою симуляції методом Монте-Карло, зазвичай близькі до теоретичних ймовірностей для кожного можливого результату.

Розбіжності між ймовірностями, отриманими в результаті симуляції Монте-Карло, та теоретичними ймовірностями відносно невеликі для більшості результатів.

Загалом, симуляція Монте-Карло надає розумну оцінку ймовірностей різних результатів кидання двох кубиків, з помилками, що зазвичай перебувають у прийнятних межах. Однак, для більш точних результатів, особливо для рідкісних подій, може знадобитися більша кількість ітерацій. Як бачимо, для 1000 000 ітерацій точність доволі висока


![Chart](/docs/task7.png)


|   Total |   Монте-Карло (%) |   Probability (%) |
|--------:|------------------:|------------------:|
|       2 |            2.7885 |              2.78 |
|       3 |            5.5479 |              5.56 |
|       4 |            8.3717 |              8.33 |
|       5 |           11.1112 |             11.11 |
|       6 |           13.881  |             13.89 |
|       7 |           16.6989 |             16.67 |
|       8 |           13.8484 |             13.89 |
|       9 |           11.1039 |             11.11 |
|      10 |            8.3226 |              8.33 |
|      11 |            5.5722 |              5.56 |
|      12 |            2.7537 |              2.78 |