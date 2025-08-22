from compressor import (
    lexical_compression,
    semantic_compression,
    task_oriented_compression,
    map_reduce_compression,
    latent_compression,
    iterative_token_reduction
)

# Load input document
with open("document.txt", "r", encoding="utf-8") as f:
    document = f.read()

print("===== 🗜️ Lexical Compression =====")
print(lexical_compression(document)[:1000])

print("\n===== 🗜️ Semantic Compression =====")
print(semantic_compression(document))

print("\n===== 🗜️ Task-Oriented Compression (News Briefing) =====")
print(task_oriented_compression(document, task="news briefing"))

print("\n===== 🗜️ Map-Reduce Compression =====")
print(map_reduce_compression(document))

print("\n===== 🗜️ Latent Compression =====")
print(latent_compression(document))

print("\n===== 🗜️ Iterative Token Reduction (3 rounds) =====")
print(iterative_token_reduction(document))
