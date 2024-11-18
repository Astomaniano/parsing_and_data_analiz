import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('prices.csv')

# Предположим, что столбец, который нужно обработать, называется 'price'
# Удаляем '₽/мес' и преобразуем в целое число
df['Price'] = df['Price'].str.replace('₽/мес.', '').str.replace(' ', '').astype(int)

# Сохраняем обработанные данные в новый CSV файл
df.to_csv('cleaned_prices.csv', index=False)