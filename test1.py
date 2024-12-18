import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла (или другого источника)
# Замените 'data.csv' на имя вашего файла
df = pd.read_csv('data.csv')

# Проверка наличия и корректности данных
print(df.info())  # Информация о DataFrame
print(df.head())  # Предварительный просмотр первых строк

# Проверка на наличие пропусков в столбцах age и spending_score
if df['age'].isnull().any() or df['spending_score'].isnull().any():
    print("В данных есть пропуски!")
else:
    print("Пропусков нет.")

# Преобразование столбцов в числовые значения, если это необходимо
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['spending_score'] = pd.to_numeric(df['spending_score'], errors='coerce')

# Удаление строк с NaN значениями после преобразования
df.dropna(subset=['age', 'spending_score'], inplace=True)

# Построение линейного графика
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='age', y='spending_score', marker='o')

# Настройка оформления графика
plt.title('Зависимость балла по расходам от возраста сотрудников')
plt.xlabel('Возраст')
plt.ylabel('Баллы по расходам')
plt.grid(True)
plt.xticks(rotation=45)  # Поворот меток по оси X для удобства чтения
plt.tight_layout()  # Автоматическая подстройка элементов графика

# Показать график
plt.show()
