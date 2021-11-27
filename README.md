# Отчет
## IO-bound. Проверяем ссылки на страницах Википедии
### 1 worker
#### Во время работы:
![](IO_bound_pictures/IO_OS_1w.png)
#### Результаты выполнения:
![](IO_bound_pictures/IO_results_1w.png)

### 5 workers
#### Во время работы:
![](IO_bound_pictures/IO_OS_5w.png)
#### Результаты выполнения:
![](IO_bound_pictures/IO_results_5w.png)

### 10 workers
#### Во время работы:
![](IO_bound_pictures/IO_OS_10w.png)
#### Результаты выполнения:
![](IO_bound_pictures/IO_results_10w.png)

### 100 workers
#### Во время работы:
![](IO_bound_pictures/IO_OS_100w.png)
#### Результаты выполнения:
![](IO_bound_pictures/IO_results_100w.png)

### Вывод: 
При увеличении количества воркеров время выполнения заметно уменьшается, загрузка ЦП и сети увеличиваются. Объем рабочей памяти, используемой процессом, по сравнению с 1 воркером увеличился, но для 5, 10 и 100 воркеров различается не сильно.

## CPU-bound. Генерируем монетки

### 1 worker 
#### Во время работы:
![](CPU_bound_pictures/CPU_OS_1w.png)
#### Результаты выполнения:
![](CPU_bound_pictures/CPU_results_1w.png)

### 2 workers
#### Во время работы:
![](CPU_bound_pictures/CPU_OS_2w.png)
#### Результаты выполнения:
![](CPU_bound_pictures/CPU_results_2w.png)

### 4 workers
#### Во время работы:
![](CPU_bound_pictures/CPU_OS_4w.png)
#### Результаты выполнения:
![](CPU_bound_pictures/CPU_results_4w.png)

### 5 workers
#### Во время работы:
![](CPU_bound_pictures/CPU_OS_5w.png)
#### Результаты выполнения:
![](CPU_bound_pictures/CPU_results_5w.png)

### 10 workers
#### Во время работы:
![](CPU_bound_pictures/CPU_OS_10w.png)
#### Результаты выполнения:
![](CPU_bound_pictures/CPU_results_10w.png)
### 100 workers (61 workers)
При 100 воркерах произошла ошибка, поэтому пришлось изменить на 61.
![](CPU_bound_pictures/error_100w.png)
При 61 тоже произошла ошибка - изменила на 60.
![](CPU_bound_pictures/error_61.png)
#### Во время работы:
![](CPU_bound_pictures/CPU_OS_100w.png)
#### Результаты выполнения:
![](CPU_bound_pictures/CPU_results_100w.png)

### Вывод: 
Наименьшее время выполнения было при 4 воркерах. Наибольшее - при 1 воркере. При 2, 5, 10 и 60 время выполнения было примерно одинаковым. 
