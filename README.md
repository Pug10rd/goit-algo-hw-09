### Порівняння жадібного алгоритму та алгоритму динамічного програмування

1. **Час виконання**:
   - **Жадібний алгоритм**: має часову складність O(n), де n — це кількість монет, оскільки алгоритм проходить по списку монет лише один раз, вибираючи найбільші номінали.
   - **Алгоритм динамічного програмування**: має часову складність O(n * m), де n — сума, яку потрібно видати, а m — кількість різних номіналів. Цей алгоритм створює таблицю, в якій розраховуються найменші кількості монет для всіх сум до n.

2. **Ефективність при великих сумах**:
   - **Жадібний алгоритм** може не дати оптимальний розподіл для деяких сум, оскільки він не враховує, що використання менших монет може призвести до кращого рішення в цілому. Проте для сум, які можна точно скласти з доступних монет, цей алгоритм є дуже швидким і простим.
   - **Алгоритм динамічного програмування** завжди знаходить оптимальне рішення, але при великих сумах і кількості монет може бути ресурсомістким через необхідність заповнення великої таблиці.

3. **Висновки**:
   - **Жадібний алгоритм** підходить для швидкого отримання результатів у простих ситуаціях, де монети формують суму оптимально.
   - **Алгоритм динамічного програмування** є більш надійним для складніших ситуацій, де важливо знайти найменшу кількість монет, але вимагає більше часу та пам’яті. 
