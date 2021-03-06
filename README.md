# Numerical analysis homework

Our homework for numerical analysis UNN course

## Task 11

Решите численно задачу, указанную в Приложении 3 (уравнения и
системы ОДУ 2-го порядка и выше).
Используйте явный или неявный метод Рунге-Кутта порядка не ниже
третьего или метод Рунге-Кутта-Мерсона.
Запишите расчетные формулы метода.
Проверьте жесткость системы.
Найдите численное решение задачи, постройте его график, укажите физический смысл решения.
Затем исследуйте численно зависимость решений от вариации начальных условий задачи Коши и далее – зависимость некоторых наиболее интересных с прикладной точки зрения свойств решений от параметров системы.
При построении численных решений контролируйте локальную погрешность и (если нужно) выход на границу отрезка интегрирования.  

Задача:   

Как и в предыдущей задаче, груз массы m может совершать
прямолинейные перемещения вдоль оси абсцисс по горизонтальной плоскости
без трения. Для стабилизации положения груза используется аналогичная система, но пружина с нелинейной характеристикой отсутствует. Положение груза
в системе описывает линейное дифференциальное уравнение
m u'' + cu' + ku =0;   
u(x0) = u0 ; u'(x0) = u'0   
где u(x) – смещение груза вдоль оси абсцисс относительно положения равновесия, x – время, u0 – начальное отклонение груза и u'0 – его начальная скорость.
Решите задачу, используя те же параметры и начальные условия:
k = 2.0 H/см; с = 0.15 Н с /см2
; m = 1.0 кг, u(0) = 10 см; u'(0) = 0.
Отрезок интегрирования должен быть достаточным, чтобы выявить динамику
системы, но не менее чем 0 ≤ x ≤ 1 c.
Исследуйте численно влияние жесткости k и демпфера c на динамику положения груза. Сравните результаты (траектории) с вариантом № 3. Параметры
системы: k, c, m.   

Предыдущая задача:   

Груз массы m может совершать прямолинейные перемещения по горизонтальной плоскости вдоль оси абсцисс. Трение отсутствует. Для 
 25
стабилизации положения груза используется система с подвеской: пружина
постоянной жесткости k, демпфер с коэффициентом демпфирования c и пружина с нелинейной характеристикой k*, которые при отклонении груза от равновесного положения создают силы, восстанавливающие равновесие. Пружина
с характеристикой k создает силу, пропорциональную смещению груза, пружина с характеристикой k*– силу, пропорциональную третьей степени смещения (указанные силы действуют в направлении, противоположном смещению),
демпфер – силу, пропорциональную скорости (в направлении, противоположном скорости). 
