import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame
df = pd.read_csv('updated_dataset.csv')

plt.figure(figsize=(10, 5))

plt.plot(df['Year'], df['PriceLinen'], marker='o', label='Price of Linen')

plt.plot(df['Year'], df['PriceCoat'], marker='o', label='Price of Coat')

plt.plot(df['Year'], df['TheoreticalLinen'], marker='x', linestyle='--', label='Adjusted Price of Linen')

plt.title('Exchange Value of Linen and Coat')
plt.xlabel('Year')
plt.ylabel('Price')

plt.legend()

plt.show()
#plt.savefig('price_of_linen_over_years.png')
