from ucimlrepo import fetch_ucirepo

# fetch dataset "recipe reviews and user feedback"
df = fetch_ucirepo(id=911)

print(df)
