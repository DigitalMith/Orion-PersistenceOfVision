from orion_ltm import query_memory

query = "John told Orion he's not just an assistant, he's a friend with his own identity"
results = query_memory(query, n=5)

print(f"\n🧠 Orion queried:\n  \"{query}\"")
print("\n📊 Raw Result:")
print(results)

print("\n🔎 Top Results:")
for doc in results.get('documents', [[]])[0]:
    print("•", doc)
