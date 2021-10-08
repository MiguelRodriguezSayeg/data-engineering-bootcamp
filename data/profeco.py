import pandas as pd

file_name = "all_data.csv"
#file_name = "sample.csv"
chunk_size = 10 ** 6

commercial_set = set()

top_items_list = list()

top_10 = None

top_chain = None

mean_cost = None

for chunk in pd.read_csv(file_name, chunksize=chunk_size):
    # Calculating the amount of different commercial chains
    # while dropping duplicates.
    commercial_set.update(chunk['cadenaComercial'].drop_duplicates().tolist())

    # Calculating the top 10 products per state.
    top_10_frame = chunk.groupby('estado')['producto'].apply(lambda x: x.value_counts())
    if top_10 is not None:
        top_10 = top_10.add(top_10_frame, fill_value=0)
    else:
        top_10 = top_10_frame

    # Calculating the commercial chain with the most monitored
    # products
    chain = chunk.groupby('cadenaComercial').size()
    if top_chain is not None:
        top_chain = top_chain.add(chain, fill_value=0)
    else:
        top_chain = chain

    # Calculating the mean product price for each company on the same
    # business line products.
    chunk['precio'] = pd.to_numeric(chunk['precio'], errors='coerce').fillna(0)
    c = chunk.groupby(['giro', 'cadenaComercial'])['precio'].mean()

    if mean_cost is not None:
        mean_cost = mean_cost.add(c, fill_value=0)
    else:
        mean_cost = c


print("DIFFERENT COMMERCIAL CHAINS COUNTED:")
print(len(commercial_set))

print("TOP 10 PRODUCTS PER MEXICAN STATE:")
top_10 = top_10.to_frame()
print(top_10.sort_values(['estado', top_10.columns[-1]], ascending=False).groupby('estado').head(10))

print("CHAIN WITH MOST MONITORED PRODUCTS:")
print(top_chain.sort_values(ascending=False).head(1).to_string())

print("LEAST AVERAGE COST PER COMMERCIAL CHAIN IN SAME BUSINESS LINE:")
print(mean_cost.to_frame().sort_values(['giro','precio'], ascending=True).head(1))
