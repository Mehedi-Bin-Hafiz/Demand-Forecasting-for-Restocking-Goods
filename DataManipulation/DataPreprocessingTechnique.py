from sklearn.preprocessing import MinMaxScaler

data = [[2,18]]
scaler = MinMaxScaler()
scaler.fit(data)
scaled = scaler.transform(data)
print(scaled)
